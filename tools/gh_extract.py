"""Convert a .gh file to .ghx via GH_IO.dll and write a compact Markdown summary.
Usage: python tools/gh_extract.py <file.gh> <out_dir>
"""
import sys, os, re, collections
import xml.etree.ElementTree as ET

GH_IO = r"C:\Program Files\Rhino 8\Plug-ins\Grasshopper\GH_IO.dll"


def to_ghx(src, dst):
    import clr
    clr.AddReference(GH_IO)
    from GH_IO.Serialization import GH_Archive
    a = GH_Archive()
    if not a.ReadFromFile(src):
        raise RuntimeError("GH_IO could not read " + src)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(a.Serialize_Xml())


def items(chunk):
    out = {}
    for it in chunk.findall("./items/item"):
        out[it.get("name") + (it.get("index") or "")] = it
    return out


def txt(it):
    return (it.text or "").strip() if it is not None else ""


def summarize(ghx, md):
    root = ET.parse(ghx).getroot()
    objs = root.findall(".//chunk[@name='DefinitionObjects']/chunks/chunk[@name='Object']")
    counts = collections.Counter()
    sliders, panels, scripts, toggles, others, groups = [], [], [], [], [], []
    libs = set()
    for lib in root.findall(".//chunk[@name='GHALibraries']/chunks/chunk"):
        it = items(lib)
        libs.add(f"{txt(it.get('Name'))} {txt(it.get('Version'))} ({txt(it.get('Author'))})")
    for o in objs:
        name = txt(items(o).get("Name"))
        cont = o.find("./chunks/chunk[@name='Container']")
        if cont is None:
            continue
        ci = items(cont)
        nick = txt(ci.get("NickName"))
        counts[name] += 1
        label = f"{name} [{nick}]" if nick and nick != name else name
        if "Slider" in name:
            sl = cont.find(".//chunk[@name='Slider']")
            si = items(sl) if sl is not None else {}
            sliders.append(f"- **{nick}**: value={txt(si.get('Value'))} range=[{txt(si.get('Min'))}, {txt(si.get('Max'))}]")
        elif name == "Panel":
            t = txt(ci.get("UserText"))
            if t:
                panels.append(f"- **{nick}**: {t[:300].replace(chr(10), ' | ')}")
        elif name in ("Boolean Toggle", "Button"):
            toggles.append(f"- **{nick}**: {txt(ci.get('ToggleValue'))}")
        elif name == "Group":
            groups.append(nick)
        else:
            code = None
            for key in ("CodeInput", "ScriptSource", "Text", "Script"):
                for it in cont.iter("item"):
                    if it.get("name") == key and it.text and len(it.text) > 30:
                        code = it.text; break
                if code: break
            if code:
                scripts.append((label, code))
            else:
                ins = [txt(items(p).get("NickName")) for p in cont.findall("./chunks/chunk[@name='param_input']")]
                outs = [txt(items(p).get("NickName")) for p in cont.findall("./chunks/chunk[@name='param_output']")]
                if ins or outs:
                    others.append(f"- {label}: in({', '.join(ins)}) -> out({', '.join(outs)})")
    L = [f"# Grasshopper summary: {os.path.basename(ghx)}", "", f"Total objects: {len(objs)}", "",
         "## Plugins / libraries", *([f"- {l}" for l in sorted(libs)] or ["- (none)"]), "",
         "## Groups", *([f"- {g}" for g in groups if g] or ["- (none)"]), "",
         "## Component counts", *[f"- {k}: {v}" for k, v in counts.most_common()], "",
         "## Sliders", *(sliders or ["- (none)"]), "",
         "## Toggles/Buttons", *(toggles or ["- (none)"]), "",
         "## Panels (user text)", *(panels or ["- (none)"]), "",
         "## Components with I/O", *sorted(set(others)), "",
         "## Embedded scripts"]
    for label, code in scripts:
        L += [f"### {label}", "```", code.strip()[:3000], "```"]
    with open(md, "w", encoding="utf-8") as f:
        f.write("\n".join(L))


if __name__ == "__main__":
    src, out = os.path.abspath(sys.argv[1]), os.path.abspath(sys.argv[2])
    os.makedirs(out, exist_ok=True)
    ghx = os.path.join(out, os.path.splitext(os.path.basename(src))[0] + ".ghx")
    to_ghx(src, ghx)
    summarize(ghx, os.path.join(out, "gh_summary.md"))
    print("ok", ghx)
