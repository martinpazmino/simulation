# Task 1 Execution Plan: Simulation in AEC, Project Assignment I

> **Sources:** Graphify knowledge graph (`data/.parsed/graphify-out/merged-graph.json`, 97 nodes, built with Gemini), `data/.parsed/gh_summary.md`, plus a few targeted line greps of the parsed assignment and lectures 3 and 5 where the graph held only node names.
> **Citation keys:** **[A1]** 1st Assignment · **[L1]** Lecture 1 (Intro / Project Intro) · **[L2]** Lecture 2 (Theoretical foundations) · **[L3]** Lecture 3 (BPS part 1, energy) · **[L5]** Lecture 5 (KPIs: energy, solar, daylight) · **[R1]–[R10]** papers in `data/papers/`.

> ⚠️ **Deadline check:** [A1] gives the due date and presentation date as **11.11.2026**, which is before today (12.11.2026). Check the actual deadline on Moodle before planning the schedule.

---

## 1. Task 1 Scope & Deliverables  [A1]

**Goal:** Build a simulation-based model of a building in Rhino/Grasshopper, define the high-performance criteria (HPC), assign specialist roles, and plan an integrated approach to collaboration and analysis.

| # | Sub-task | Required content |
|---|---|---|
| 1 | **Building context** | Type/function; geometry and layout (plan, orientation, façade, window-to-wall ratio); construction materials (thermal properties, insulation, reflectivity); windows (number, size, glazing, U-value, placement); environment (site, shading, neighbours); building systems (HVAC, setpoints, window operation, internal mass); occupancy (people, schedules, usage) |
| 2 | **Simulation inputs** (design variables) | Insulation thickness; shading devices/façade; material properties; window properties/size/placement; HVAC strategies and setpoints |
| 3 | **Boundary conditions** | Weather/climate data; setpoints and HVAC assumptions; internal loads; ventilation rates and schedules; lighting and shading assumptions |
| 4 | **Design and collaboration process** | Roles (Solar, Thermal-comfort, Shading, Daylighting, Energy, User-comfort specialist); responsibilities (which HPC each role simulates); collaboration methods; design and simulation schedule with milestones |
| 5 | **HPC** | One measurable KPI per specialist (for example EUI, DA/sDA/glare, operative temperature/PMV, solar irradiance/PV area) |
| 6 | **Simulations and analysis** | Model in Rhino/GH → plugins → run → collect each HPC → analyse individually and together → trade-offs and synergies → overall performance → reflection on integrated design |

**Deliverables (PDF via Moodle, in English):**
- **Written report:** at most 4 pages / 2000 words, worth **7 portfolio points**. Sections: introduction; building context; model description (inputs, boundary conditions, scales); HPC table; roles; process flow or timeline; assumptions; **equations with explanations**; results; links between the simulations; graphics (3D, plots); reflections; references.
- **Final presentation:** at most 10 minutes, worth **3 portfolio points**.
- **Functional scripts:** `.gh` and `.3dm`.
- **Tools:** Rhino 8 + Grasshopper + Ladybug Tools [A1, L1].

---

## 2. Theoretical & Mathematical Basis

### 2.1 Simulation fundamentals  [L1, L2]
- **Model:** a simplified representation or "twin" of a real system. **Simulation:** the use of models to represent a system's physical characteristics, operation and control [L1].
- **Deterministic vs. stochastic:** a deterministic model has no randomness, so identical inputs always give identical outputs. EnergyPlus and Radiance runs are deterministic. A stochastic model includes randomness and depends on past states, as in the occupant-behaviour models of [R5] [L2].
- **System theory and systems thinking:** treat energy, daylight, solar and comfort as one coupled system. This is the basis of the "interconnections" section of the report [L2, L1].
- **BPS:** evaluates building performance under real-life conditions (Hensen & Lamberts 2011; Mahdavi 2020) [L3].

### 2.2 Energy  [L3, L5]
- **Conduction heat flow:**
  $Q_{cond,total} = U \cdot A \cdot (T_{outdoor} - T_{indoor})$
  where U is the thermal transmittance in W/m²K and A is the surface area in m² [L3].
- **U-value from layers:** use the standard relation $U = 1/(R_{si} + \sum d_i/\lambda_i + R_{se})$ to link the insulation-thickness input to U. This is a textbook relation, not an equation found in the graph; cite DIN EN ISO 6946.
- **Energy Use Intensity:**
  $EUI = E_{total}\,[\text{kWh}] / A_{floor}\,[\text{m}^2]$
  Lecture worked example: 945 kWh / (5 × 7 m × 4 floors = 140 m²) = **6.75 kWh/m²** [L5].

### 2.3 Solar / PV  [L5, GH definition]
- **Irradiance components:**
  $GHI = DNI \cdot \cos\theta_z + DHI$
  where GHI is total shortwave on a horizontal surface, DNI is the direct component and DHI is the diffuse component [L5].
- **PV yield**, matching the inputs of HB Photovoltaic Properties / HB Generation Loads (simplified PVWatts model):
  $E_{AC} \approx A_{PV} \cdot f_{active} \cdot \eta_{PV} \cdot H_{POA} \cdot (1 - L_{sys}) \cdot \eta_{inv}$
  Current definition values: η_PV = 0.22, L_sys = 0.05, η_inv = 0.96, DC/AC ratio = 1.10. H_POA is the plane-of-array irradiation from the Munich TMYx EPW.

### 2.4 Daylight  [L5] (Bushra & Hartmann 2024)
| Metric | Definition | Typical target |
|---|---|---|
| **DA** | % of occupied hours with daylight illuminance ≥ 300 (or 500) lux | Report per sensor point |
| **sDA(300/50%)** | % of floor area reaching 300 lux for ≥ 50 % of occupied hours | ≥ 55 % (nominal), ≥ 75 % (preferred) |
| **cDA** | Like DA, but partial credit between 100 and 300 lux | — |
| **UDI(100–3000 lux)** | % of occupied hours within the useful range | Maximise; above 3000 lux indicates glare/overheating risk |

### 2.5 Thermal comfort  [A1, R7]
- HPC options: operative-temperature range, PMV/PPD [A1].
- [R7] combines PMV and PPD into an **EQTC** index and uses **EnergyPlus + MLR with interaction terms + Monte Carlo** to predict energy and comfort. Cite this as the method behind trade-off and sensitivity analysis.

### 2.6 Methods from the papers (for the report's literature section)
| Ref | Method relevant to Task 1 |
|---|---|
| **R4** (Alsukkar 2025) | Parametric split louvers in Grasshopper, using Honeybee (Radiance + EnergyPlus) with **NSGA-II** to optimise daylight vs. energy. Template for the Shading/Daylighting trade-off. |
| **R3** (Li 2025) | Green Design Studio: modular multi-scale Rhino/GH platform coupling CONTAM and ANSYS Fluent. Template for collaboration through modules. |
| **R6** (Mosca 2025) | Ladybug Tools + ENVI-met for outdoor thermal comfort. Template for the context/microclimate role. |
| **R5** (Neves 2025) | Stochastic occupant-behaviour model (binary logistic regression for window operation). Justifies schedules and ventilation assumptions. |
| **R2** (Peinturier & Wallom 2025) | LOD 1–3 modelling-complexity framework vs. calibration accuracy. Justifies the chosen model detail. |
| **R1, R8** | UBEM review (CityGML/IFC/gbXML) and AutoBEM/OpenStudio vs. measured data. Supports the validation discussion. |

---

## 3. Current Grasshopper Code Audit (`gh/Prototyp B1 Gebäude.gh`)

**Size and plugins:** 271 objects. Plugins: Ladybug/Honeybee, Bifocals (labels only) and Sasquatch.

**Inputs (sliders):**

| Parameter | Value | Range |
|---|---|---|
| Building length | 4 m | — |
| Building width | 6 m | — |
| Number of storeys | 1 | 1–10 |
| Storey height | 3.3 m | — |
| Panel height | 0.9 m | — |
| PV efficiency | 0.22 | — |
| System losses | 0.05 | — |

There are also two "Länge/Breite" sliders (4 / 5) for the context or PV field, plus one unused 0–100 slider. The weather file is the Munich-Theresienwiese TMYx EPW, loaded through *LB Download Weather*. A Boolean toggle is set to **false**, so the run is off.

**Core logic:**
1. **Geometry:** an XY plane and a rectangle become storey outlines, which are moved to the storey heights.
2. **Façade division:** each outline is divided into points 1 m apart and split into floor, ceiling, window, wall-panel and window-frame surfaces (Divide Curve, Series, List Item, Loft, Boundary Surfaces, Extrude).
3. **Preview:** Custom Preview and Colour Swatch.
4. **Honeybee:** *HB Shade* ×2 (PV panels and the shading context) → *HB Photovoltaic Properties* → *HB Generation Loads* (an EnergyPlus PV electricity estimate).

One group is labelled *"Das anzuschließen ist wegen Rechenpower gefährlich"* ("connecting this is risky because of computing power"), so a heavy component is deliberately left unconnected.

**Outputs today:** Geometry preview and a PV generation estimate, if the toggle is switched on.

**Gaps for Task 1:**
- [ ] No **HB Room / HB Model**. The walls and windows are plain Rhino surfaces, so energy, daylight and comfort cannot be simulated.
- [ ] No **constructions/materials** (U-values, insulation thickness) and no **window-to-wall-ratio parameter**.
- [ ] No **programs, schedules, loads, setpoints or HVAC** (boundary conditions, sub-task 3).
- [ ] No **daylight analysis** (sensor grid, annual daylight, DA/sDA/UDI).
- [ ] No **thermal-comfort analysis** (operative temperature, PMV, adaptive comfort).
- [ ] No **solar irradiance study** (LB Incident Radiation / cumulative sky matrix) for the PV-area HPC.
- [ ] No **EUI** output or post-processing, no result legends or plots, and no CSV/HPC export.
- [ ] No **parametric variants** (shading depth, insulation, window-to-wall ratio) and no batch or optimisation loop.
- [ ] The building is very small (4 × 6 m, 1 storey) and orientation is not a parameter.

---

## 4. Step-by-Step Implementation Plan

### Phase 0: Setup (Day 1)
- [ ] Confirm the deadline on Moodle and save the original as `gh/Prototyp_B1_v0_original.gh` (back-up).
- [ ] Check that Ladybug Tools ≥ 1.8 is installed, and that the EnergyPlus and Radiance paths work (*LB Versioner* / *HB Check*).
- [ ] Assign the 6 specialist roles and set up a shared folder (Teams/OneDrive) with a `results/` CSV convention and a weekly meeting.

### Phase 1: Building context and parameters (sub-tasks 1–2)
- [ ] Fix the building type: office or mixed-use, plus 3–4 storeys so EUI and daylight are meaningful.
- [ ] Add sliders for **orientation (0–360°)**, **window-to-wall ratio (0.2–0.8)**, **shading depth (0–1 m)**, **insulation thickness (0.05–0.30 m)** and **glazing U/SHGC**.
- [ ] Replace the façade surfaces with *HB Room from Solid* per storey and add *HB Apertures by Ratio* (window-to-wall ratio).
- [ ] Turn the existing surrounding-context *HB Shade* into a proper context model of neighbouring buildings.

### Phase 2: Boundary conditions (sub-task 3)
- [ ] Weather: reuse the Munich TMYx EPW and add the design-day `.ddy` file.
- [ ] Constructions: *HB Opaque Construction* (layers λ, d → U) and *HB Window Construction*. Apply them with *HB Apply Construction Set*.
- [ ] Program: *HB Program Type* (office), people density, lighting and equipment loads (W/m²), schedules (Mon–Fri 08–18).
- [ ] Setpoints and HVAC: heating 20 °C, cooling 26 °C, *HB Ideal Air* (or natural ventilation with *HB Window Opening*, citing [R5]).
- [ ] Record every assumption in a `Panel` so it can go into the report's assumptions table.

### Phase 3: Simulations per HPC (sub-tasks 5–6)
| Specialist | HPC (target) | GH workflow |
|---|---|---|
| Energy | **EUI** (kWh/m²a, target ≤ 100) | HB Model → *HB Model to OSM* → *HB Read Room Energy Result* → Σ / floor area |
| Solar | **Annual irradiation on roof/façade** (kWh/m²), **PV yield** (kWh/a) | *LB Cumulative Sky Matrix* + *LB Incident Radiation*; fix and connect the existing HB PV chain |
| Daylighting | **sDA(300/50%) ≥ 55 %**, **UDI 100–3000** | *HB Sensor Grid* (0.75 m) → *HB Annual Daylight* → *HB Annual Daylight Metrics* |
| Shading | **Glare (DGP < 0.35)** / shaded area % | *HB Louver Shades* parametric (after [R4]) → *HB Imageless Annual Glare* |
| Thermal comfort | **% hours operative temp. 20–26 °C** / PMV ±0.5 | *HB Annual Thermal Comfort* / *HB PMV Comfort Map* |
| User comfort | Combined comfort / UDI-overlit hours | Post-process daylight and thermal results |

- [ ] Put each run behind its own Boolean toggle, because simulations are heavy. Keep the "Rechenpower" group off during design iterations.
- [ ] Export results with *LB Write CSV* (or Panel → Data Recorder) to `results/<HPC>.csv`.

### Phase 4: Variants and trade-offs
- [ ] Define a small design matrix (≈ 8–12 variants): window-to-wall ratio {0.3, 0.5, 0.7} × shading {0, 0.5 m} × insulation {0.12, 0.24 m}. Run it with Colibri/TT Toolbox or a manual slider loop.
- [ ] Optional: run Wallacei/Octopus (NSGA-II, as in [R4]) on EUI vs. sDA.
- [ ] Plot the trade-offs: EUI vs. sDA, PV yield vs. shading, comfort hours vs. window-to-wall ratio. Name the synergies (for example, louvers lower both cooling and glare) and the conflicts (larger windows mean more daylight but higher EUI).

### Phase 5: Validation
- [ ] Sanity-check heat flow by hand using $Q = U·A·ΔT$ for one wall [L3] and compare with the E+ surface heat-flow output.
- [ ] Compare EUI with reference values for German offices (≈ 100–150 kWh/m²a) and PV yield with ≈ 950–1100 kWh/kWp·a for Munich.
- [ ] Check that the sDA grid excludes the core and that sensors sit at 0.75 m. Check the HB Model with *HB Validate Model*.
- [ ] Discuss model complexity (LOD) against accuracy, citing [R2], and the gap between simulated and measured results, citing [R8].

### Phase 6: Deliverables
- [ ] Graphics: 3D views with legends (irradiance, sDA, comfort maps), produced with *LB Capture View*.
- [ ] Report (≤ 2000 words), following the [A1] section list. Include an HPC table, a process-flow diagram, the equations from §2 and references to [L3, L5, R2, R4, R5, R7].
- [ ] Slides (≤ 10 min). Export to PDF.
- [ ] Submit `.gh` (internalised geometry) and `.3dm`, plus both PDFs, on Moodle at least 1 h before the deadline.

---

## Notes on token-saving pipeline (reproducible)
```bash
python tools/gh_extract.py "<ascii-path>/prototyp_b1.gh" data/.parsed      # GH_IO.dll → .ghx + gh_summary.md (.ghx since moved to data/.ghx/)
python -m docling.cli.main --to md --no-ocr --image-export-mode placeholder --output data/.parsed/<dir> data/<dir>
graphify extract data/.parsed --backend gemini      # re-run until no chunks fail (free tier: 5 requests/min)
graphify explain "<node>" --graph data/.parsed/graphify-out/merged-graph.json
```
