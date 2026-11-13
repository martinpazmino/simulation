# Grasshopper summary: prototyp_b1.ghx

Total objects: 444

## Plugins / libraries
-   ()
- Bifocals  (Marc Syp)
- Grasshopper 8.35.26251.13001 (Robert McNeel & Associates)
- Sasquatch  (Scott Overall, SHoP Architects)

## Groups
- PV Simulation
- Stockwerke auf passende Höhe schieben
- Grundrisse der Stockwerke erstellen
- 1 Meter entfernte Punkte auf die Grundrisse legen
- Decken und Böden
- Flächen für die Elemente erstellen
- Rahmen erstellen für Fensterfront
- Das anzuschließen ist wegen Rechenpower gefährlich
- Boden
- Decke
- Fenster
- Wandpanel
- Fensterrahmen
- Slider zum Einstellen
- PV Panel
- Verschattende Umgebung
- Point
- Rectangle
- XY Plane
- Multiplication
- Multiplication
- Explode
- List Item
- Series
- List Item
- Series
- Divide Curve
- Divide Curve
- Remove Last Item
- Remove First Item
- Line
- Remove Last Item
- Remove First Item
- Line
- Explode Tree
- Explode Tree
- Merge
- Extrude
- Unit Z
- Point
- Merge
- List Item
- Series
- Series
- Rectangle
- Multiplication
- Multiplication
- Split List
- Move
- Unit Z
- Series
- Reverse List
- Reverse List
- Divide Curve
- Multiplication
- Multiplication
- Addition
- Line
- Split List
- Reverse List
- Reverse List
- Shift List
- Extrude
- Unit Z
- Multiplication
- Move
- Unit Z
- Boundary Surfaces
- Boundary Surfaces
- Rectangle
- Curve
- Custom Preview
- Colour Swatch
- Custom Preview
- Colour Swatch
- Offset Curve
- Multiplication
- Merge
- Loft
- Custom Preview
- Colour Swatch
- Curve
- Explode
- List Item
- List Item
- Move
- Unit Z
- Multiplication
- End Points
- End Points
- Merge
- PolyLine
- List Item
- End Points
- End Points
- Merge
- PolyLine
- Boundary Surfaces
- Boundary Surfaces
- Custom Preview
- Colour Swatch
- Custom Preview
- Colour Swatch
- Deconstruct Brep
- HB Shade
- HB Photovoltaic Properties
- HB Generation Loads
- Merge
- LB Download Weather
- HB Shade
- Text
- Boden
- Decke
- Fenster
- Wandpanel
- Fensterrahmen
- Umlegen auf True um PV Simulation zu starten
- HB Generation Loads
- LB Import EPW
- LB Cumulative Sky Matrix
- LB Incident Radiation
- LB Analysis Period
- LB SunPath
- Number
- LB Direct Sun Hours
- Merge
- Boundary Surfaces
- HB Opaque Material
- HB Opaque Material
- HB Opaque Material
- HB Opaque Material
- HB Opaque Material No Mass
- HB Opaque Construction
- HB Opaque Construction
- HB Opaque Construction
- HB Opaque Construction
- HB Opaque Construction
- HB Window Material
- HB Window Construction
- HB Window Construction Shade
- HB Shade Material
- HB Exterior Construction Subset
- HB Ground Construction Subset
- HB Interior Construction Subset
- HB Subface Subset
- HB Window Frame
- HB Room
- Cluster
- HB Construction Set by Climate
- HB ModifierSet
- HB Room
- HB ConstructionSet
- Deconstruct Brep
- HB Face
- Gene Pool
- Gene Pool
- HB Weekly Schedule
- HB Schedule to Data
- LB Hourly Plot
- HB People
- HB Lighting
- HB Equipment
- HB ProgramType
- HB Apply Setpoint Values
- HB Internal Mass
- HB Opaque Material
- HB Opaque Construction
- HB Door
- HB Window Opening
- HB Ventilation Control
- HB Model
- HB Label Faces
- HB Face Energy Attributes
- HB Aperture
- HB Add Subface
- Merge

## Component counts
- Group: 176
- Panel: 64
- Number Slider: 47
- Surface: 12
- Multiplication: 9
- Merge: 7
- List Item: 6
- Series: 5
- Unit Z: 5
- Boundary Surfaces: 5
- Custom Preview: 5
- Colour Swatch: 5
- HB Opaque Construction: 5
- Reverse List: 4
- End Points: 4
- Boolean Toggle: 4
- HB Opaque Material: 4
- Rectangle: 3
- Divide Curve: 3
- Line: 3
- Move: 3
- Point: 2
- Explode: 2
- Remove Last Item: 2
- Remove First Item: 2
- Explode Tree: 2
- Extrude: 2
- Split List: 2
- Curve: 2
- PolyLine: 2
- Deconstruct Brep: 2
- HB Shade: 2
- Gene Pool: 2
- XY Plane: 1
- Addition: 1
- Shift List: 1
- Offset Curve: 1
- Loft: 1
- HB Photovoltaic Properties: 1
- LB Download Weather: 1
- Bifocals: 1
- HB Generation Loads: 1
- LB Import EPW: 1
- LB Cumulative Sky Matrix: 1
- LB Analysis Period: 1
- LB SunPath: 1
- LB Direct Sun Hours: 1
- HB Window Material: 1
- HB Window Construction: 1
- HB Window Construction Shade: 1
- HB Shade Material: 1
- HB Exterior Construction Subset: 1
- HB Ground Construction Subset: 1
- HB Interior Construction Subset: 1
- HB Subface Subset: 1
- HB Window Frame: 1
- HB Room: 1
- HB ConstructionSet: 1
- HB Face: 1
- HB Weekly Schedule: 1
- HB Schedule to Data: 1
- LB Hourly Plot: 1
- HB People: 1
- HB Lighting: 1
- HB Equipment: 1
- HB ProgramType: 1
- HB Apply Setpoint Values: 1
- HB Internal Mass: 1
- HB Window Opening: 1
- HB Ventilation Control: 1
- HB Model: 1
- HB Label Faces: 1
- HB Face Energy Attributes: 1
- HB Aperture: 1

## Sliders
- **Länge**: value=4 range=[-1, 15]
- **Breite**: value=5 range=[-1, 15]
- **Number Slider**: value=0 range=[0, 100]
- **Länge vom Gebäude in Meter**: value=4 range=[-1, 15]
- **Breite vom Gebäude in Meter**: value=6 range=[-1, 15]
- **Stockwerke Anzahl**: value=1 range=[1, 10]
- **Stockwerkshöhe in Meter**: value=3.3 range=[2.3, 6]
- **Panelhöhe in Meter**: value=0.9 range=[0, 2]
- **Wirkungsgrad PV**: value=0.22 range=[0, 1]
- **Weitere Systemverluste**: value=0.05 range=[0, 1]
- **Number Slider**: value=1 range=[1, 12]
- **Number Slider**: value=0 range=[0, 24]
- **Number Slider**: value=1 range=[1, 31]
- **Number Slider**: value=12 range=[2, 12]
- **Number Slider**: value=23 range=[2, 24]
- **Number Slider**: value=30 range=[2, 30]
- **Number Slider**: value=100 range=[0, 100]
- **Number Slider**: value=0.5 range=[0.1, 0.5]
- **Material Thickness**: value=0.36 range=[0.1, 1.1]
- **Conductivity (W/m2K)**: value=0.19 range=[0, 2]
- **Density (kg/m3)**: value=990 range=[600, 4000]
- **Specific heat (j/kgK)**: value=1000 range=[100, 1500]
- **Material Thickness**: value=0.47 range=[0.1, 1.1]
- **Conductivity (W/m2K)**: value=0.2 range=[0, 2]
- **Density (kg/m3)**: value=1450 range=[600, 4000]
- **Specific heat (j/kgK)**: value=1000 range=[100, 1500]
- **Material Thickness**: value=0.07 range=[0.01, 1.1]
- **Conductivity (W/m2K)**: value=1.39 range=[0, 2]
- **Material Thickness**: value=0.15 range=[0.01, 1.1]
- **Conductivity (W/m2K)**: value=1.91 range=[0, 2]
- **Density (kg/m3)**: value=1733 range=[600, 4000]
- **Specific heat (j/kgK)**: value=1006 range=[100, 1500]
- **Number Slider**: value=0.4 range=[0, 1]
- **Number Slider**: value=0.6 range=[0, 1]
- **Number Slider**: value=0.12 range=[0, 0.5]
- **Number Slider**: value=0.16 range=[0, 0.5]
- **people per area**: value=0.1 range=[0.1, 2]
- **lighting watt/m2**: value=8 range=[2, 20]
- **equipment watt/m2**: value=10 range=[2, 20]
- **Number Slider**: value=20 range=[10, 30]
- **Number Slider**: value=26 range=[10, 30]
- **Number Slider**: value=5 range=[1, 10]
- **Material Thickness**: value=0.29 range=[0.01, 1.1]
- **Conductivity (W/m2K)**: value=0.16 range=[0, 2]
- **Density (kg/m3)**: value=1124 range=[600, 4000]
- **Specific heat (j/kgK)**: value=920 range=[100, 1500]
- **Number Slider**: value=0.5 range=[0, 1]

## Toggles/Buttons
- **Boolean Toggle**: true
- **Boolean Toggle**: false
- **Boolean Toggle**: true
- **Boolean Toggle**: true

## Panels (user text)
- ****: 1000
- ****: 1000
- ****: 1
- ****: 2
- ****: 0
- ****: 2
- ****: 3500
- ****: 1
- ****: 1
- ****: 1
- ****: 1
- ****: 1000
- ****: 1000
- ****: 0
- ****: 2
- ****: 2
- ****: 1
- ****: 1000
- ****: -50
- ****: 2
- ****: 2
- ****: 0
- ****: 1000
- ****: 0
- ****: Double click to edit panel content…
- ****: 1
- ****: https://www.climate.onebuilding.org/WMO_Region_6_Europe/DEU_Germany/BY_Bayern/DEU_BY_Munich-Theresienwiese.108650_TMYx.zip
- ****: 0
- ****: 0.96
- ****: 1.10
- ****: Double click to edit panel content…
- ****: Double click to edit panel content…
- ****: Double click to edit panel content…
- ****: Double click to edit panel content…
- **Panel**: Double click to edit panel content…
- **Panel**: Double click to edit panel cont_grid_size_ = 0.5 m |  | Source: Alsukkar, M., Alkhater, M., Su, Y., & Ibrahim, A. (2025). |  | Optimizing daylighting performance and energy efficiency through the |  | integration of parametric split louvers in office buildings. |  | Energy and Built Environment (in press), pp. 2-4 
- **Material Name**: sand-lime brick + ETICS
- **Material Name**: Concrete + insulation
- **Material Name**: Sand-lime brick
- **Panel**: exterior wall
- ****: Interior floor
- ****: ceiling
- ****: Fensterrahmen
- ****: Interior Wall
- **Panel**: Window
- ****: Window with shades
- ****: Window shades
- ****: exterior
- **Panel**: room 1
- **Panel**: Weekly schedule (office, Mon-Fri; Sat/Sun = 0) |  | Occupancy: 07-09 h 30 %, 09-17 h 85 %, else 0 % |  |   Source: Li et al. (2025), Building and Environment / R3, office schedule table. |  | HVAC availability: 07-19 h |  |   Source: Peinturier & Wallom (2025) / R2. |  | Daylight occupied hours: 08-17 h, Alsukkar et al
- **Panel**: People room 1
- ****: Lighting
- ****: equipment
- ****: Internal loads (office) |  | People:    0.10 ppl/m2  - Li et al. (2025), Sustainable Cities and Society (R3) |  | Lighting:  8 W/m2 (LED) - range 5-18 W/m2, Algburi et al. (2025), |  |            Results in Engineering, doi:10.1016/j.rineng.2025.105475 (R7) |  | Equipment: 10 W/m2      - range 8-25 W/m2, Algburi et
- ****: room programm
- **Panel**: APPLY HEATING & COOLING SETPOINTS |  | Heating setpoint: 20 °C (constant) |  | Cooling setpoint: 26 °C (constant) |  |  |  | Heating: Peinturier & Wallom (2025) evaluate a reduced heating |  | setpoint of 19 °C as an energy-saving measure; 20 °C is adopted |  | as the base case. |  |   Energy & Buildings, doi:10.1016/j.enbuild
- **Material Name**: Timber
- ****: Door
- **Min interior temp**: 22
- **Max outside temp**: 30
- **Max interior temp**: 25
- **Min outside temp**: 15
- **Panel**: NATURAL VENTILATION CONTROL (HB Ventilation Control) |  | Windows open only when: |  |   Indoor temp.  22–25 °C |  |   Outdoor temp. 15–30 °C |  |  |  | Logic: window opening driven by indoor/outdoor temperature |  | during occupancy, following the window-control strategy of |  | Neves et al. (2025), who open windows when oper
- **Panel**: Double click to edit panel content…

## Components with I/O
- Bifocals: in(Exceptions) -> out()
- Boundary Surfaces: in(Edges) -> out(Surfaces)
- Custom Preview: in(Geometry, Material) -> out()
- Deconstruct Brep: in(Brep) -> out(Faces, Edges, Vertices)
- Divide Curve: in(Curve, Count, Kinks) -> out(Points, Tangents, Parameters)
- End Points: in(Curve) -> out(Start, End)
- Explode: in(Curve, Recursive) -> out(Segments, Vertices)
- Extrude: in(Base, Direction) -> out(Extrusion)
- Line: in(Start Point, End Point) -> out(Line)
- Loft: in(Curves, Options) -> out(Loft)
- Move: in(Geometry, Motion) -> out(Geometry, Transform)
- Offset Curve: in(Curve, Distance, Plane, Corners) -> out(Curve)
- PolyLine: in(Vertices, Closed) -> out(Polyline)
- Rectangle: in(Plane, X Size, Y Size, Radius) -> out(Rectangle, Length)
- Remove First Item: in(List, Number of Items) -> out(List)
- Remove Last Item: in(List, Number of Items) -> out(List)
- Reverse List: in(List) -> out(List)
- Series: in(Start, Step, Count) -> out(Series)
- Shift List: in(List, Shift, Wrap) -> out(List)
- Split List: in(List, Index) -> out(List A, List B)
- Unit Z: in(Factor) -> out(Unit vector)
- XY Plane: in(Origin) -> out(Plane)

## Embedded scripts
### HB Shade [Shade]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2026, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create Honeybee Shade.

-



    Args:

        _geo: Rhino Brep or Mesh geometry.

        _name_: Text to set the name for the Shade and to be incorporated into

            unique Shade identifier. If the name is not provided, a random name

            will be assigned.

        attached_: Boolean to note whether the Shade is attached to other geometry.

            This is automatically set to True if the Shade is assigned to

            a parent Room, Face, Aperture or Door but will otherwise defalt

            to False. If the Shade is not easily assignable to a parent

            object but is attached to the building (eg. a parapet or large

            roof overhang), then this should be set to True. (Default: False).

        ep_constr_: Optional text for the Shade's energy construction to be looked

            up in the construction library. This can also be a custom construction

            object. If no energy construction is input here, a default will be

            assigned.

        ep_trans_sch_: Optional text for the Shade's energy transmittance schedule

            to be looked up in the schedule library. This can also be a custom

            schedule object. If no energy schedule is input here, the default will

            be always opaque.

        rad_mod_: Optional text for the Shade's radiance modifier to be looked

            up in the modifier library. This can also be a custom modifier object.

            If no radiance modifier is input here, a default will be assigned.



    Returns:

        report: Reports, errors, warnings, etc.

        shades: Honeybee shades. These can be used directly in radiance and

            energy simulations.

"""



ghenv.Component.Name = 'HB Shade'

ghenv.Component.NickName = 'Shade'

ghenv.Component.Message = '1.10.0'

ghenv.Component.Category = 'Honeybee'

ghenv.Component.SubCategory = '0 :: Create'

ghenv.Component.AdditionalHelpFromDocStrings = '5'



try:  # import the ladybug_geometry dependencies

    from ladybug_geometry.geometry3d import Face3D

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))



try:  # import the core honeybee dependencies

    from honeybee.shade import Shade

    from honeybee.shademesh import ShadeMesh

    from honeybee.typing import clean_and_id_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the ladybug_rhino dependencies

    from ladybug_rhino.togeometry import to_face3d, to_mesh3d

    from ladybug_rhino.grasshopper import all_required_inputs, longest_list, 
```
### HB Photovoltaic Properties [Photovoltaic]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2026, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>





"""

Assign photovoltaic properties to a honeybee Shade such that it will generate

electricity in energy simulations.

-



    Args:

        _shades: Honeybee Shades to which photovoltaic properties will be assigned.

        _rated_efficiency_: A number between 0 and 1 for the rated nameplate efficiency

            of the photovoltaic solar cells under standard test conditions (STC).

            _

            Standard test conditions are 1,000 Watts per square meter solar

            irradiance, 25 degrees C cell temperature, and ASTM G173-03 standard

            spectrum. Nameplate efficiencies reported by manufacturers are typically

            under STC.

            _

            Standard poly- or mono-crystalline silicon modules tend to have

            rated efficiencies in the range of 14-17%. Premium high efficiency

            mono-crystalline silicon modules with anti-reflective coatings can

            have efficiencies in the range of 18-20%. Thin film photovoltaic

            modules typically have efficiencies of 11% or less. (Default: 0.15

            for standard silicon solar cells).

        _active_fraction_: The fraction of the parent Shade geometry that is covered in active

            solar cells. This fraction includes the difference between the PV

            panel (aka. PV module) area and the active cells within the panel

            as well as any losses for how the (typically rectangular) panels

            can be arranged on the Shade geometry. When the parent Shade

            geometry represents just the solar panels, this fraction is typically

            around 0.9 given that the framing elements of the panel reduce the

            overall active area. (Default: 0.9).

        _module_type_: Text or an integer to indicate the type of solar module. This is used

            to determine the temperature coefficients used in the simulation of the

            photovoltaic modules. Choose from the three options below. If unspecified,

            the module_type will be inferred from the rated_efficiency of these

            PVProperties using the rated efficiencies listed below.

            _

                * 0 - Standard - 12% <= rated_efficiency < 18%

                * 1 - Premium - rated_efficiency >= 18%

                * 2 - ThinFilm - rated_efficiency < 12%

        _mounting_type_: Text or an integer to indicate the type of mounting and/or tracking used

            for the photovoltaic array. Note that the OneAxis options have an axis

            of rotation that is determined by the azimuth of the parent Shade

            geom
```
### LB Download Weather [DownloadEPW]
```
# Ladybug: A Plugin for Environmental Analysis (GPL)

# This file is part of Ladybug.

#

# Copyright (c) 2026, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Automatically download a .zip file from a URL where climate data resides,

unzip the file, and open .epw, .stat, and ddy weather files.

-



    Args:

        _weather_URL: Text representing the URL at which the climate data resides. 

            To open the a map interface for all publicly availabe climate data,

            use the "LB EPWmap" component.

        _folder_: An optional file path to a directory into which the weather file

            will be downloaded and unziped.  If None, the weather files will be

            downloaded to the ladybug default weather data folder and placed in

            a sub-folder with the name of the weather file location.



    Returns:

        epw_file: The file path of the downloaded epw file.

        stat_file: The file path of the downloaded stat file.

        ddy_file: The file path of the downloaded ddy file.

"""



ghenv.Component.Name = 'LB Download Weather'

ghenv.Component.NickName = 'DownloadEPW'

ghenv.Component.Message = '1.10.0'

ghenv.Component.Category = 'Ladybug'

ghenv.Component.SubCategory = '0 :: Import'

ghenv.Component.AdditionalHelpFromDocStrings = '1'



import os



try:

    from ladybug.futil import unzip_file

    from ladybug.config import folders

except ImportError as e:

    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))



try:

    from ladybug_rhino.download import download_file

    from ladybug_rhino.grasshopper import all_required_inputs, give_warning

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    # process the URL and check if it is outdated

    lone_epw = False

    _weather_URL = _weather_URL.strip()

    if _weather_URL.lower().endswith('.zip'):  # standard zip file format

        _folder_name = _weather_URL.split('/')[-1][:-4]

    elif _weather_URL.lower().endswith('.epw'):  # a lone epw file

        _folder_name = _weather_URL.split('/')[-1][:-4]

        lone_epw = True

    else: # old dept of energy URL type

        _folder_name = _weather_URL.split('/')[-2]

        if _weather_URL.endswith('/all'):

            repl_section = '{0}/all'.format(_folder_name)

            new_section = '{0}/{0}.zip'.format(_folder_name)

            _weather_URL = _weather_URL.replace(repl_section, new_section)

            _weather_URL = _weather_URL.replace(

                'www.energyplus.net/weather-download',

                'energyplus-weather.s3.amazonaws.com')

            _weather_URL = _weather_URL.replace(

                'energyplus.net/weather-download',

                '
```
### HB Shade [Shade]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2026, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create Honeybee Shade.

-



    Args:

        _geo: Rhino Brep or Mesh geometry.

        _name_: Text to set the name for the Shade and to be incorporated into

            unique Shade identifier. If the name is not provided, a random name

            will be assigned.

        attached_: Boolean to note whether the Shade is attached to other geometry.

            This is automatically set to True if the Shade is assigned to

            a parent Room, Face, Aperture or Door but will otherwise defalt

            to False. If the Shade is not easily assignable to a parent

            object but is attached to the building (eg. a parapet or large

            roof overhang), then this should be set to True. (Default: False).

        ep_constr_: Optional text for the Shade's energy construction to be looked

            up in the construction library. This can also be a custom construction

            object. If no energy construction is input here, a default will be

            assigned.

        ep_trans_sch_: Optional text for the Shade's energy transmittance schedule

            to be looked up in the schedule library. This can also be a custom

            schedule object. If no energy schedule is input here, the default will

            be always opaque.

        rad_mod_: Optional text for the Shade's radiance modifier to be looked

            up in the modifier library. This can also be a custom modifier object.

            If no radiance modifier is input here, a default will be assigned.



    Returns:

        report: Reports, errors, warnings, etc.

        shades: Honeybee shades. These can be used directly in radiance and

            energy simulations.

"""



ghenv.Component.Name = 'HB Shade'

ghenv.Component.NickName = 'Shade'

ghenv.Component.Message = '1.10.0'

ghenv.Component.Category = 'Honeybee'

ghenv.Component.SubCategory = '0 :: Create'

ghenv.Component.AdditionalHelpFromDocStrings = '5'



try:  # import the ladybug_geometry dependencies

    from ladybug_geometry.geometry3d import Face3D

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))



try:  # import the core honeybee dependencies

    from honeybee.shade import Shade

    from honeybee.shademesh import ShadeMesh

    from honeybee.typing import clean_and_id_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the ladybug_rhino dependencies

    from ladybug_rhino.togeometry import to_face3d, to_mesh3d

    from ladybug_rhino.grasshopper import all_required_inputs, longest_list, 
```
### HB Generation Loads [GenLoads]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Run Honeybee objects capable of generating electricity (such as Shades with PV

properties) through a quick energy simulation to obtain an estimate of

electricity production.

_

Note that this component only evaluates electricity production and not energy

consumption. Any number of Honeybee Rooms or other objects can be connected

but they will only be simulated as context shade that casts shadows on the

generator objects.

-



    Args:

        _hb_objs: An array of honeybee Rooms, Faces, Apertures, Doors or Shades to be

            included in the simulation of electricity production. This can also

            be an entire Model to be simulated. Any number of Honeybee Rooms or

            non-generating objects can be connected but they will only be

            simulated as context shade that casts shadows on the

            generator objects.

        _epw_file: Path to an .epw file on your system as a text string.

        _north_: A number between -360 and 360 for the counterclockwise difference

            between the North and the positive Y-axis in degrees.

            90 is West and 270 is East. (Default: 0).

        _inverter_eff_: A number between 0 and 1 for the load centers's inverter nominal

            rated DC-to-AC conversion efficiency. An inverter converts DC power,

            such as that output by photovoltaic panels, to AC power, such as

            that distributed by the electrical grid and is available from

            standard electrical outlets. Inverter efficiency is defined as the

            inverter's rated AC power output divided by its rated DC power

            output. (Default: 0.96).

        _dc_to_ac_size_: A positive number (typically greater than 1) for the ratio of the

            inverter's DC rated size to its AC rated size. Typically, inverters

            are not sized to convert the full DC output under standard test

            conditions (STC) as such conditions rarely occur in reality and

            therefore unnecessarily add to the size/cost of the inverter. For a

            system with a high DC to AC size ratio, during times when the 

            DC power output exceeds the inverter's rated DC input size, the inverter

            limits the array's power output by increasing the DC operating voltage,

            which moves the arrays operating point down its current-voltage (I-V)

            curve. The default value of 1.1 is reasonable for most systems. A

            typical range is 1.1 to 1.25, although some large-scale systems have

            ratios of as high as 1.5. The optimal value depends on the 
```
### LB Import EPW [ImportEPW]
```
# Ladybug: A Plugin for Environmental Analysis (GPL)

# This file is part of Ladybug.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Import climate data from a standard .epw file.



-



    Args:

        _epw_file: An .epw file path on your system as a string.

        

    Returns:

        location: A Ladybug Location object describing the location data in the

            weather file.

        dry_bulb_temperature: The houlry dry bulb temperature, in C.

            Note that this is a full numeric field (i.e. 23.6) and not an integer

            representation with tenths. Valid values range from 70 C to

            70 C. Missing value for this field is 99.9.

        dew_point_temperature: The hourly dew point temperature, in C.

            Note that this is a full numeric field (i.e. 23.6) and not an integer

            representation with tenths. Valid values range from 70 C to

            70 C. Missing value for this field is 99.9.

        relative_humidity: The hourly Relative Humidity in percent.

            Valid values range from 0% to 110%. Missing value for this field is 999.

        wind_speed: The hourly wind speed in m/sec.

            Values can range from 0 to 40. Missing value is 999.

        wind_direction: The hourly wind direction in degrees.

            The convention is North=0.0, East=90.0, South=180.0, West=270.0.

            If wind is calm for the given hour, the direction equals zero.

            Values can range from 0 to 360. Missing value is 999.

        direct_normal_rad: The hourly Direct Normal Radiation in Wh/m2.

            Direc Normal Radiation is the amount of solar radiation in Wh/m2

            received directly from the solar disk on a surface perpendicular

            to the sun's rays. Missing values are (9999).

        diffuse_horizontal_rad: The hourly Diffuse Horizontal Radiation in Wh/m2.

            Diffuse Horizontal Radiation is the amount of solar radiation in

            Wh/m2 received from the sky (excluding the solar disk) on a

            horizontal surface. Missing values are (9999).

        global_horizontal_rad: The hourly Global Horizontal Radiation in Wh/m2.

            Global Horizontal Radiation is the total amount of direct and

            diffuse solar radiation in Wh/m2 received on a horizontal surface.

            It is not currently used inbEnergyPlus calculations. It should

            have a minimum value of 0; missing value for this field is 9999.

        horizontal_infrared_rad: The Horizontal Infrared Radiation Intensity in Wh/m2.

            If it is missing, EnergyPlus calculates it from the Opaque Sky Cover

            field. It should have a minimum value of 0; missing value is 9999.

        direct_normal_ill: The
```
### LB Cumulative Sky Matrix [SkyMatrix]
```
# Ladybug: A Plugin for Environmental Analysis (GPL)

# This file is part of Ladybug.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Get a matrix containing radiation values from each patch of a sky dome.

_

Creating this matrix is a necessary pre-step before doing incident radiation

analysis with Rhino geometry or generating a radiation rose.

_

This component uses Radiance's gendaymtx function to calculate the radiation

for each patch of the sky. Gendaymtx is written by Ian Ashdown and Greg Ward.

Morere information can be found in Radiance manual at:

http://www.radiance-online.org/learning/documentation/manual-pages/pdfs/gendaymtx.pdf

-



    Args:

        north_: A number between -360 and 360 for the counterclockwise

            difference between the North and the positive Y-axis in degrees.

            90 is West and 270 is East. This can also be Vector for the

            direction to North. (Default: 0)

        _location: A ladybug Location that has been output from the "LB Import EPW"

            component or the "LB Construct Location" component.

        _direct_rad: An annual hourly DataCollection of Direct Normal Radiation such

            as that which is output from the "LB Import EPW" component or the

            "LB Import STAT" component.

        _diffuse_rad: An annual hourly DataCollection of Diffuse Horizontal Radiation

            such as that which is output from the "LB Import EPW" component or

            the "LB Import STAT" component.

        _hoys_: A number or list of numbers between 0 and 8760 that respresent

            the hour(s) of the year for which to generate the sky matrix. The

            "LB Calculate HOY" component can output this number given a month,

            day and hour. The "LB Analysis Period" component can output a

            list of HOYs within a certain hour or date range. By default,

            the matrix will be for the entire year.

        high_density_: A Boolean to indicate whether the higher-density Reinhart sky

            matrix should be generated (True), which has roughly 4 times the sky

            patches as the (default) original Tregenza sky (False). Note that,

            while the Reinhart sky has a higher resolution and is more accurate,

            it will result in considerably longer calculation time for incident

            radiation studies. The difference in sky resolution can be observed

            with the "LB Sky Dome" component. (Default: False).

        _ground_ref_: A number between 0 and 1 to note the average ground reflectance

            that is associated with the sky matrix. (Default: 0.2).

        _folder_: The folder in which the Radiance commands are executed to

            produce the sky matrix. If
```
### LB Analysis Period [AnalysisPeriod]
```
# Ladybug: A Plugin for Environmental Analysis (GPL)

# This file is part of Ladybug.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create an Analysis Period to describe a slice of time during the year.



-



    Args:

        _start_month_: Start month (1-12).

        _start_day_: Start day (1-31).

        _start_hour_: Start hour (0-23).

        _end_month_: End month (1-12).

        _end_day_: End day (1-31).

        _end_hour_: End hour (0-23).

        _timestep_: An integer number for the number of time steps per hours.

            Acceptable inputs include: 1, 2, 3, 4, 5, 6, 10, 12, 15, 20, 30, 60

    

    Returns:

        period: Analysis period.

        hoys: List of dates in this analysis period.

        dates: List of hours of the year in this analysis period.

"""



ghenv.Component.Name = 'LB Analysis Period'

ghenv.Component.NickName = 'AnalysisPeriod'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'Ladybug'

ghenv.Component.SubCategory = '1 :: Analyze Data'

ghenv.Component.AdditionalHelpFromDocStrings = '2'



try:

    import ladybug.analysisperiod as ap

except ImportError as e:

    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))



try:

    from ladybug_rhino.grasshopper import wrap_output, turn_off_old_tag

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))

turn_off_old_tag(ghenv.Component)





anp = ap.AnalysisPeriod(

    _start_month_, _start_day_, _start_hour_,

    _end_month_, _end_day_, _end_hour_, _timestep_)



if anp:

    period = anp

    dates = wrap_output(anp.datetimes)

    hoys = anp.hoys
```
### LB SunPath [Sunpath]
```
# Ladybug: A Plugin for Environmental Analysis (GPL)

# This file is part of Ladybug.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Output a Sunpath (aka. sun plot) graphic into the Rhino scene.

-

The component also outputs sun vectors that can be used for solar access

analysis and shading design.

-



    Args:

        north_: A number between -360 and 360 for the counterclockwise

            difference between the North and the positive Y-axis in degrees.

            90 is West and 270 is East. This can also be Vector for the

            direction to North. (Default: 0)

        _location: A ladybug Location that has been output from the "LB Import EPW"

            component or the "LB Construct Location" component.

        hoys_: A number or list of numbers between 0 and 8760 that represent the

            hour of the year at which to evaluate the sun position. The

            "LB Calculate HOY" component can output this number given a month,

            day and hour. The "LB Analysis Period" component can output a

            list of HOYs within a certain hour or date range.

        dl_saving_: An optional analysis period for daylight saving time.

            If None, no daylight saving time will be used. (Default: None)

        solar_time_: A boolean to indicate if the input hours should be treated

             as solar time instead of standard or daylight time. (Default: False)

        _center_pt_: A point for the center of the sun path. (Default: (0, 0, 0))

        _scale_: A number to set the scale of the sun path. The default is 1,

            which corresponds to a radius of 100 meters in the current Rhino

            model's unit system.

        projection_: Optional text for the name of a projection to use from the sky

            dome hemisphere to the 2D plane. If None, a 3D sun path will be drawn

            instead of a 2D one. (Default: None) Choose from the following:

                * Orthographic

                * Stereographic

        daily_: Boolean to note whether the sunpath should display only one daily

            arc for each unique day in the input hoys_ (True) or whether the

            output sun path geometry should be for the entire year, complete

            with analemmas for all sun-up hours and a daily arc for each

            month (False). (Default: False)

        data_: Optional HourlyContinuousCollection objects, which will be used

            to generate colors that align with each of the sun_pts. This data

            can also be used along with the statement_ below to select out

            sun positions that meet certain conditions.

        statement_: A conditional statement as a string (e.g. a > 25).

            .   

            The variable
```
### LB Direct Sun Hours [DirectSunHours]
```
# Ladybug: A Plugin for Environmental Analysis (GPL)

# This file is part of Ladybug.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Calculate the number of hours of direct sunlight received by geometry using sun

vectors obtained from the "LB SunPath" component.

_

Such direct sun calculations can be used for shadow studies of outdoor enviroments

or can be used to estimate glare potential from direct sun on the indoors.

_

Note that this component uses the CAD environment's ray intersection methods,

which can be fast for geometries with low complexity but does not scale well

for complex geometries or many test points. For such complex studies,

honeybee-radiance should be used.

-



    Args:

        _vectors: Sun vectors from the "LB SunPath" component, which will be used

            to determine the number of hours of direct sunlight received by the

            test _geometry.

        _timestep_: A positive integer for the number of timesteps per hour at

            which the "LB SunPath" component generated sun vectors. This is used

            to correctly interpret the time duration represented by each of

            the input sun vectors. (Default: 1 for 1 vector per hour).

        _geometry: Rhino Breps and/or Rhino Meshes for which direct sun analysis

            will be conducted. If Breps are input, they will be subdivided using

            the _grid_size to yeild individual points at which analysis will

            occur. If a Mesh is input, direct sun analysis analysis will be

            performed for each face of this mesh instead of subdividing it.

        context_: Rhino Breps and/or Rhino Meshes representing context geometry

            that can block sunlight to the test _geometry.

        _grid_size: A positive number in Rhino model units for the size of grid

            cells at which the input _geometry will be subdivided for direct sun

            analysis. The smaller the grid size, the higher the resolution of

            the analysis and the longer the calculation will take.  So it is

            recommended that one start with a large value here and decrease

            the value as needed. However, the grid size should usually be

            smaller than the dimensions of the smallest piece of the _geometry

            and context_ in order to yield meaningful results.

        _offset_dist_: A number for the distance to move points from the surfaces

            of the input _geometry.  Typically, this should be a small positive

            number to ensure points are not blocked by the mesh but it can be

            equal to zero when geo_block_ is False. (Default: 10 cm when

            geo_block_ is True and zero when geo_block_ is False).

        geo_block_: Set
```
### HB Opaque Material [OpaqueMat]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a standard opaque material, which can be plugged into the "HB Opaque

Construction" component.

-



    Args:

        _name_: Text to set the name for the material and to be incorporated into

            a unique material identifier.

        _thickness: Number for the thickness of the material layer [m].

        _conductivity: Number for the thermal conductivity of the material [W/m-K].

        _density: Number for the density of the material [kg/m3].

        _spec_heat: Number for the specific heat of the material [J/kg-K].

        _roughness_: Text describing the relative roughness of the material.

            Must be one of the following: 'VeryRough', 'Rough', 'MediumRough',

            'MediumSmooth', 'Smooth', 'VerySmooth'. (Default: 'MediumRough').

        _therm_absp_: A number between 0 and 1 for the fraction of incident long

            wavelength radiation that is absorbed by the material. (Default: 0.9).

        _sol_absp_: A number between 0 and 1 for the fraction of incident solar

            radiation absorbed by the material. (Default: 0.7).

        _vis_absp_: A number between 0 and 1 for the fraction of incident

            visible wavelength radiation absorbed by the material.

            Default value is the same as the _sol_absp_.



    Returns:

        mat: A standard opaque material that can be assigned to a Honeybee

            Opaque construction.

"""



ghenv.Component.Name = "HB Opaque Material"

ghenv.Component.NickName = 'OpaqueMat'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "5"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.material.opaque import EnergyMaterial

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    # set the default material properties

    _roughness_ = 'MediumRough' if _roughness_ is None else _roughness_

    _therm_absp_ = 0.9 if _therm_absp_ is None else _therm_absp_

    _sol_absp_ = 0.7 if _sol_absp_ is None else _sol_absp_

    name =
```
### HB Opaque Material [OpaqueMat]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a standard opaque material, which can be plugged into the "HB Opaque

Construction" component.

-



    Args:

        _name_: Text to set the name for the material and to be incorporated into

            a unique material identifier.

        _thickness: Number for the thickness of the material layer [m].

        _conductivity: Number for the thermal conductivity of the material [W/m-K].

        _density: Number for the density of the material [kg/m3].

        _spec_heat: Number for the specific heat of the material [J/kg-K].

        _roughness_: Text describing the relative roughness of the material.

            Must be one of the following: 'VeryRough', 'Rough', 'MediumRough',

            'MediumSmooth', 'Smooth', 'VerySmooth'. (Default: 'MediumRough').

        _therm_absp_: A number between 0 and 1 for the fraction of incident long

            wavelength radiation that is absorbed by the material. (Default: 0.9).

        _sol_absp_: A number between 0 and 1 for the fraction of incident solar

            radiation absorbed by the material. (Default: 0.7).

        _vis_absp_: A number between 0 and 1 for the fraction of incident

            visible wavelength radiation absorbed by the material.

            Default value is the same as the _sol_absp_.



    Returns:

        mat: A standard opaque material that can be assigned to a Honeybee

            Opaque construction.

"""



ghenv.Component.Name = "HB Opaque Material"

ghenv.Component.NickName = 'OpaqueMat'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "5"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.material.opaque import EnergyMaterial

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    # set the default material properties

    _roughness_ = 'MediumRough' if _roughness_ is None else _roughness_

    _therm_absp_ = 0.9 if _therm_absp_ is None else _therm_absp_

    _sol_absp_ = 0.7 if _sol_absp_ is None else _sol_absp_

    name =
```
### HB Opaque Material [OpaqueMat]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a standard opaque material, which can be plugged into the "HB Opaque

Construction" component.

-



    Args:

        _name_: Text to set the name for the material and to be incorporated into

            a unique material identifier.

        _thickness: Number for the thickness of the material layer [m].

        _conductivity: Number for the thermal conductivity of the material [W/m-K].

        _density: Number for the density of the material [kg/m3].

        _spec_heat: Number for the specific heat of the material [J/kg-K].

        _roughness_: Text describing the relative roughness of the material.

            Must be one of the following: 'VeryRough', 'Rough', 'MediumRough',

            'MediumSmooth', 'Smooth', 'VerySmooth'. (Default: 'MediumRough').

        _therm_absp_: A number between 0 and 1 for the fraction of incident long

            wavelength radiation that is absorbed by the material. (Default: 0.9).

        _sol_absp_: A number between 0 and 1 for the fraction of incident solar

            radiation absorbed by the material. (Default: 0.7).

        _vis_absp_: A number between 0 and 1 for the fraction of incident

            visible wavelength radiation absorbed by the material.

            Default value is the same as the _sol_absp_.



    Returns:

        mat: A standard opaque material that can be assigned to a Honeybee

            Opaque construction.

"""



ghenv.Component.Name = "HB Opaque Material"

ghenv.Component.NickName = 'OpaqueMat'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "5"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.material.opaque import EnergyMaterial

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    # set the default material properties

    _roughness_ = 'MediumRough' if _roughness_ is None else _roughness_

    _therm_absp_ = 0.9 if _therm_absp_ is None else _therm_absp_

    _sol_absp_ = 0.7 if _sol_absp_ is None else _sol_absp_

    name =
```
### HB Opaque Construction [OpaqueConstr]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create an EnergyPlus opaque construction. Material inputs can be either the

identifiers of materials within the library or a custom material made with any

of the EnergyPlus Material components.

_

Note that the _materials should be ordered from outermost (exterior) layer to the

innermost (interior) layer.

-



    Args:

        _name_: Text to set the name for the Construction and to be incorporated

            into a unique Construction identifier.

        _materials: List of materials in the construction (from exterior to interior).

            These materials can be either fully-detailed material objects built

            with the material components or text for a material identifier to be

            looked up in the opaque material library.  Note that a native Grasshopper

            "Merge" component can be used to help order the materials correctly

            for the input here.



    Returns:

        constr: An opaque construction that can be assigned to Honeybee

            Faces or ConstructionSets.

"""



ghenv.Component.Name = "HB Opaque Construction"

ghenv.Component.NickName = 'OpaqueConstr'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "4"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.construction.opaque import OpaqueConstruction

    from honeybee_energy.lib.materials import opaque_material_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    name = clean_and_id_ep_string('OpaqueConstruction') if _name_ is None else \

        clean_ep_string(_name_)



    material_objs = []

    for material in _materials:

        if isinstance(material, str):

            material = opaque_material_by_identifier(material)

        material_objs.append(material)



    constr = OpaqueConstruction(name, material_objs)

    if _name_ is not None:

        constr.display_name = _name_
```
### HB Opaque Construction [OpaqueConstr]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create an EnergyPlus opaque construction. Material inputs can be either the

identifiers of materials within the library or a custom material made with any

of the EnergyPlus Material components.

_

Note that the _materials should be ordered from outermost (exterior) layer to the

innermost (interior) layer.

-



    Args:

        _name_: Text to set the name for the Construction and to be incorporated

            into a unique Construction identifier.

        _materials: List of materials in the construction (from exterior to interior).

            These materials can be either fully-detailed material objects built

            with the material components or text for a material identifier to be

            looked up in the opaque material library.  Note that a native Grasshopper

            "Merge" component can be used to help order the materials correctly

            for the input here.



    Returns:

        constr: An opaque construction that can be assigned to Honeybee

            Faces or ConstructionSets.

"""



ghenv.Component.Name = "HB Opaque Construction"

ghenv.Component.NickName = 'OpaqueConstr'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "4"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.construction.opaque import OpaqueConstruction

    from honeybee_energy.lib.materials import opaque_material_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    name = clean_and_id_ep_string('OpaqueConstruction') if _name_ is None else \

        clean_ep_string(_name_)



    material_objs = []

    for material in _materials:

        if isinstance(material, str):

            material = opaque_material_by_identifier(material)

        material_objs.append(material)



    constr = OpaqueConstruction(name, material_objs)

    if _name_ is not None:

        constr.display_name = _name_
```
### HB Opaque Construction [OpaqueConstr]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create an EnergyPlus opaque construction. Material inputs can be either the

identifiers of materials within the library or a custom material made with any

of the EnergyPlus Material components.

_

Note that the _materials should be ordered from outermost (exterior) layer to the

innermost (interior) layer.

-



    Args:

        _name_: Text to set the name for the Construction and to be incorporated

            into a unique Construction identifier.

        _materials: List of materials in the construction (from exterior to interior).

            These materials can be either fully-detailed material objects built

            with the material components or text for a material identifier to be

            looked up in the opaque material library.  Note that a native Grasshopper

            "Merge" component can be used to help order the materials correctly

            for the input here.



    Returns:

        constr: An opaque construction that can be assigned to Honeybee

            Faces or ConstructionSets.

"""



ghenv.Component.Name = "HB Opaque Construction"

ghenv.Component.NickName = 'OpaqueConstr'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "4"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.construction.opaque import OpaqueConstruction

    from honeybee_energy.lib.materials import opaque_material_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    name = clean_and_id_ep_string('OpaqueConstruction') if _name_ is None else \

        clean_ep_string(_name_)



    material_objs = []

    for material in _materials:

        if isinstance(material, str):

            material = opaque_material_by_identifier(material)

        material_objs.append(material)



    constr = OpaqueConstruction(name, material_objs)

    if _name_ is not None:

        constr.display_name = _name_
```
### HB Opaque Construction [OpaqueConstr]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create an EnergyPlus opaque construction. Material inputs can be either the

identifiers of materials within the library or a custom material made with any

of the EnergyPlus Material components.

_

Note that the _materials should be ordered from outermost (exterior) layer to the

innermost (interior) layer.

-



    Args:

        _name_: Text to set the name for the Construction and to be incorporated

            into a unique Construction identifier.

        _materials: List of materials in the construction (from exterior to interior).

            These materials can be either fully-detailed material objects built

            with the material components or text for a material identifier to be

            looked up in the opaque material library.  Note that a native Grasshopper

            "Merge" component can be used to help order the materials correctly

            for the input here.



    Returns:

        constr: An opaque construction that can be assigned to Honeybee

            Faces or ConstructionSets.

"""



ghenv.Component.Name = "HB Opaque Construction"

ghenv.Component.NickName = 'OpaqueConstr'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "4"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.construction.opaque import OpaqueConstruction

    from honeybee_energy.lib.materials import opaque_material_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    name = clean_and_id_ep_string('OpaqueConstruction') if _name_ is None else \

        clean_ep_string(_name_)



    material_objs = []

    for material in _materials:

        if isinstance(material, str):

            material = opaque_material_by_identifier(material)

        material_objs.append(material)



    constr = OpaqueConstruction(name, material_objs)

    if _name_ is not None:

        constr.display_name = _name_
```
### HB Window Material [WindowMat]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a simple window material to describe an entire glazing system, including

glass, gaps, and frame. This material can be plugged into the "HB Window

Construction" component.

-



    Args:

        _name: Text to set the name for the material and to be incorporated into

            a unique material identifier.

        _u_factor: A number for the U-factor of the glazing system [W/m2-K]

            including standard air gap resistances on either side of the

            glazing system.

        _shgc: A number between 0 and 1 for the solar heat gain coefficient

            of the glazing system. This includes both directly transmitted solar

            heat as well as solar heat that is absorbed by the glazing system and

            conducts towards the interior.

        _t_vis_: A number between 0 and 1 for the visible transmittance of the

            glazing system. (Default: 0.6).



    Returns:

        mat: A window material that describes an entire glazing system, including

            glass, gaps, and frame and can be assigned to a Honeybee Window

            construction.

"""



ghenv.Component.Name = 'HB Window Material'

ghenv.Component.NickName = 'WindowMat'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '1 :: Constructions'

ghenv.Component.AdditionalHelpFromDocStrings = '6'



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.material.glazing import EnergyWindowMaterialSimpleGlazSys

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    # set the default material properties

    _t_vis_ = 0.6 if _t_vis_ is None else _t_vis_

    name = clean_and_id_ep_string('WindowMaterial') if _name_ is None else \

        clean_ep_string(_name_)



    # create the material

    mat = EnergyWindowMaterialSimpleGlazSys(name, _u_factor, _shgc, _t_vis_)

    if _name_ is not None:

        mat.display_name = _name_
```
### HB Window Construction [WindowConstr]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create an EnergyPlus window construction. Material inputs can be either the

identifiers of materials within the library or a custom material made with any

of the EnergyPlus Material components.

_

Note that the _materials should be ordered from outermost (exterior) layer to the

innermost (interior) layer.

-



    Args:

        _name_: Text to set the name for the Construction and to be incorporated

            into a unique Construction identifier.

        _materials: List of materials in the construction (from exterior to interior).

            These materials can be either fully-detailed material objects built

            with the material components or text for a material identifier to be

            looked up in the window material library. Note that a native Grasshopper

            "Merge" component can be used to help order the materials correctly

            for the input here.

        frame_: An optional window frame material to denote the frame that surrounds

            the window construction. Frame materials can be created using the

            "HB Window Frame" component.



    Returns:

        constr: A window construction that can be assigned to Honeybee

            Apertures or ConstructionSets.

"""



ghenv.Component.Name = "HB Window Construction"

ghenv.Component.NickName = 'WindowConstr'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "4"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.construction.window import WindowConstruction

    from honeybee_energy.lib.materials import window_material_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    name = clean_and_id_ep_string('WindowConstruction') if _name_ is None else \

        clean_ep_string(_name_)



    material_objs = []

    for material in _materials:

        if isinstance(material, str):

            material = window_material_by_identifier(material)

        material_objs.append(material)



    constr 
```
### HB Window Construction Shade [WindowConstrShd]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create an EnergyPlus window construction that includes shades/blinds or a dynamically-

controlled glass pane.

_

The result can be assigned to any Aperture or ConstructionSet just like any other

WindowConstruction.

-



    Args:

        _name_: Text to set the name for the Construction and to be incorporated

            into a unique Construction identifier.

        _win_constr: A WindowConstruction object that serves as the "switched off"

            version of the construction (aka. the "bare construction"). The

            shade material and shade location will be used to modify this

            starting construction. This can also be text for a construction

            identifier to be looked up in the window construction library.

        _shd_material: An Shade Material or an Blind Material that serves as the

            shading layer for this construction. This can also be a Glass Material,

            which will indicate that the WindowConstruction has a dynamically-

            controlled glass pane like an electrochromic window assembly. This

            can also be text for a material identifier to be looked up in the

            window material library.

        _shd_location_: Text to indicate where in the window assembly the shade material

            is located. (Default: "Interior"). Choose from the following 3 options:

            * Interior

            * Between

            * Exterior

            Note that the WindowConstruction must have at least one gas gap to use

            the "Between" option. Also note that, for a WindowConstruction with more

            than one gas gap, the "Between" option defalts to using the inner gap

            as this is the only option that EnergyPlus supports.

        _control_type_: An integer or text to indicate how the shading device is controlled,

            which determines when the shading is “on” or “off.” (Default: "AlwaysOn").

             Choose from the options below (units for the values of the corresponding

             setpoint are noted in parentheses next to each option):

             0 = AlwaysOn

             1 = OnIfHighSolarOnWindow (W/m2)

             2 = OnIfHighHorizontalSolar (W/m2)

             3 = OnIfHighOutdoorAirTemperature (C)

             4 = OnIfHighZoneAirTemperature (C)

             5 = OnIfHighZoneCooling (W)

             6 = OnNightIfLowOutdoorTempAndOffDay (C)

             7 = OnNightIfLowInsideTempAndOffDay (C)

             8 = OnNightIfHeatingAndOffDay (W)

        setpoint_: A number that corresponds to the specified control_type. This can

            be a value i
```
### HB Shade Material [ShadeMat]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a material for a shade layer in a window construction (like a roller shade).

This material can be plugged into the "HB Window Construction" component.

_

Reflectance and emissivity properties are assumed to be the same on both sides of

the shade. Shades are considered to be perfect diffusers.

-



    Args:

        _name: Text to set the name for the material and to be incorporated into

            a unique material identifier.

        _thickness: Number for the thickness of the shade layer in meters.

        _transmittance_:  Number between 0 and 1 for the transmittance of both solar

            radiation and visible light through the shade. (Default: 0.4, which

            is typical of a white diffusing shade).

        _reflectance_: Number between 0 and 1 for the reflectance of both solar

            radiation and visible light off of the shade. (Default: 0.5,

            which is typical of a white diffusing shade).

        _t_infrared_: Long-wave hemisperical transmittance of the shade. (Default: 0).

        _emissivity_: Number between 0 and 1 for the infrared hemispherical

            emissivity of the shade. (Default: 0.9, which is typical of most

            diffusing shade materials).

        _conductivity_: Number for the thermal conductivity of the shade in

            W/m-K. (Default: 0.05, typical of cotton shades).

        _dist_to_glass_: A number between 0.001 and 1.0 for the distance between the

            shade and neighboring glass layers [m]. (Default: 0.05 (50 mm)).

        _open_mult_: Factor between 0 and 1 that is multiplied by the area at the top,

            bottom and sides of the shade for air flow calculations. (Default: 0.5).

        _permeability_: The fraction of the shade surface that is open to air flow.

            Must be between 0 and 0.8. (Default: 0 for no permeability).



    Returns:

        mat: A material for a shade layer in a window construction (like a roller

            shade) that can be assigned to a Honeybee Window construction.

"""



ghenv.Component.Name = 'HB Shade Material'

ghenv.Component.NickName = 'ShadeMat'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '1 :: Constructions'

ghenv.Component.AdditionalHelpFromDocStrings = '6'



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.material.shade import E
```
### HB Exterior Construction Subset [ExteriorSubset]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a list of exterior constructions that can be used to edit or create a

ConstructionSet object.

-



    Args:

        _exterior_wall_: A construction object for exterior walls (or text for

            the identifier of the construction within the library).

        _exterior_roof_: A construction object for exterior roofs (or text for

            the identifier of the construction within the library).

        _exposed_floor_: A construction object for exposed floors (or text for

            the identifier of the construction within the library).

    

    Returns:

        exterior_set: A list of exterior constructions that can be used to edit

            or create a ConstructionSet object.

"""



ghenv.Component.Name = "HB Exterior Construction Subset"

ghenv.Component.NickName = 'ExteriorSubset'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '0 :: Basic Properties'

ghenv.Component.AdditionalHelpFromDocStrings = "4"



try:  # import honeybee_energy dependencies

    from honeybee_energy.construction.opaque import OpaqueConstruction

    from honeybee_energy.lib.constructions import opaque_construction_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:

    from ladybug_rhino.grasshopper import turn_off_old_tag

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))

turn_off_old_tag(ghenv.Component)





def opaque_constr(construction, input_name):

    """Get an OpaqueConstrucion from the library if it's a string."""

    if isinstance(construction, str):

        return opaque_construction_by_identifier(construction)

    else:

        assert isinstance(construction, OpaqueConstruction), \

            'Expected OpaqueConstruction for {}. Got {}'.format(

                input_name, type(construction))

    return construction





# go through each input construction

if _exterior_wall_ is not None:

    _exterior_wall_ = opaque_constr(_exterior_wall_, '_exterior_wall_')

if _exterior_roof_ is not None:

    _exterior_roof_ = opaque_constr(_exterior_roof_, '_exterior_roof_')

if _exposed_floor_ is not None:

    _exposed_floor_ = opaque_constr(_exposed_floor_, '_exposed_floor_')





# return the final list from the component

exterior_set = [_exterior_wall_, _exterior_roof_, _exposed_floor_]
```
### HB Ground Construction Subset [GroundSubset]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a list of ground constructions that can be used to edit or create a

ConstructionSet object.

-



    Args:

        _ground_wall_: A construction object for underground walls (or text for

            the identifier of the construction within the library).

        _ground_roof_: A construction object for underground roofs (or text for

            the identifier of the construction within the library).

        _ground_floor_: A construction object for ground-contact floors (or text

            for the identifier of the construction within the library).

    

    Returns:

        ground_set: A list of ground constructions that can be used to edit

            or create a ConstructionSet object.

"""



ghenv.Component.Name = "HB Ground Construction Subset"

ghenv.Component.NickName = 'GroundSubset'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '0 :: Basic Properties'

ghenv.Component.AdditionalHelpFromDocStrings = "4"



try:  # import honeybee_energy dependencies

    from honeybee_energy.construction.opaque import OpaqueConstruction

    from honeybee_energy.lib.constructions import opaque_construction_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import turn_off_old_tag

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))

turn_off_old_tag(ghenv.Component)





def opaque_constr(construction, input_name):

    """Get an OpaqueConstrucion from the library if it's a string."""

    if isinstance(construction, str):

        return opaque_construction_by_identifier(construction)

    else:

        assert isinstance(construction, OpaqueConstruction), \

            'Expected OpaqueConstruction for {}. Got {}'.format(

                input_name, type(construction))

    return construction





# go through each input construction

if _ground_wall_ is not None:

    _ground_wall_ = opaque_constr(_ground_wall_, '_ground_wall_')

if _ground_roof_ is not None:

    _ground_roof_ = opaque_constr(_ground_roof_, '_ground_roof_')

if _ground_floor_ is not None:

    _ground_floor_ = opaque_constr(_ground_floor_, '_ground_floor_')





# return the final list from the component

ground_set = [_ground_wall_, _ground_roof_, _ground_floor_]
```
### HB Interior Construction Subset [InteriorSubset]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a list of interior constructions that can be used to edit or create a

ConstructionSet object.

-



    Args:

        _interior_wall_: A construction object for interior walls (or text for

            the identifier of the construction within the library).

        _ceiling_: A construction object for ceilings (or text for the identifier of

            the construction within the library).

        _interior_floor_: A construction object for interior floors (or text for

            the identifier of the construction within the library).

        _interior_window_: A construction object for all apertures with a Surface

            boundary condition. This can also be text for the identifier of the

            construction within the library.

        _interior_door_: A construction object for all opaque doors with a Surface

            boundary condition. This can also be text for the identifier of the

            construction within the library.

        _int_glass_door_: A construction object for all glass doors with a Surface

            boundary condition. This can also be text for the identifier of the

            construction within the library.

    

    Returns:

        interior_set: A list of interior constructions that can be used to edit

            or create a ConstructionSet object.

"""



ghenv.Component.Name = 'HB Interior Construction Subset'

ghenv.Component.NickName = 'InteriorSubset'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '0 :: Basic Properties'

ghenv.Component.AdditionalHelpFromDocStrings = '4'



try:  # import honeybee_energy dependencies

    from honeybee_energy.construction.opaque import OpaqueConstruction

    from honeybee_energy.construction.window import WindowConstruction

    from honeybee_energy.construction.dynamic import WindowConstructionDynamic

    from honeybee_energy.lib.constructions import opaque_construction_by_identifier, \

        window_construction_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import give_warning, turn_off_old_tag

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))

turn_off_old_tag(ghenv.Component)





def opaque_constr(construction, input_name):

    """Get an OpaqueConstrucion from the library if it's a string."""

    if isinstance(construction, str):

        return opaque_construction_by_identifier(construction)

    else:

        asse
```
### HB Subface Subset [SubfaceSubset]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a list of exterior subface (apertures + doors) constructions that can be

used to edit or create a ConstructionSet object.

-



    Args:

        _window_: A construction object for apertures with an Outdoors boundary

            condition and a Wall face type for their parent face. This can also

            be text for the identifier of the construction within the library.

        _skylight_: A construction object for apertures with an Outdoors boundary

            condition and a RoofCeiling or Floor face type for their parent face.

            This can also be text for the identifier of the construction within

            the library.

        _operable_: A construction object for apertures with an Outdoors boundary

            condition and True is_operable property. This can also be text for

            the identifier of the construction within the library.

        _exterior_door_: A construction object for opaque doors with an Outdoors

            boundary condition and a Wall face type for their parent face. This

            can also be text for the identifier of the construction within

            the library.

        _overhead_door_: A construction object for opaque doors with an Outdoors

            boundary condition and a RoofCeiling or Floor face type for their

            parent face. This can also be text for the identifier of the construction

            within the library.

        _glass_door_: A construction object for all glass doors with an Outdoors

            boundary condition. This can also be text for the identifier of the

            construction within the library.



    Returns:

        subface_set: A list of exterior subface constructions that can be used

            to edit or create a ConstructionSet object.

"""



ghenv.Component.Name = 'HB Subface Subset'

ghenv.Component.NickName = 'SubfaceSubset'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '0 :: Basic Properties'

ghenv.Component.AdditionalHelpFromDocStrings = '4'



try:  # import honeybee_energy dependencies

    from honeybee_energy.construction.opaque import OpaqueConstruction

    from honeybee_energy.construction.window import WindowConstruction

    from honeybee_energy.construction.windowshade import WindowConstructionShade

    from honeybee_energy.construction.dynamic import WindowConstructionDynamic

    from honeybee_energy.lib.constructions import opaque_construction_by_identifier, \

        window_construction_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_
```
### HB Window Frame [WindowFrame]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a window frame matrial that can be assigned to a Window Construction by

plugging it into the frame_ input of the "HB Window Construction" component.

-



    Args:

        _name: Text to set the name for the frame material and to be incorporated into

            a unique material identifier.

        _width: Number for the width of frame in plane of window [m]. The frame

            width is assumed to be the same on all sides of window.

        _conductance: Number for the thermal conductance of the frame material measured

            from inside to outside of the frame surface (no air films) and taking

            2D conduction effects into account [W/m2-K]. Values for typical frame

            materials are as follows.

                * Aluminum with Thermal Break - 56.4 W/m2-K

                * Aluminum One-Sided (Flush) - 10.7 W/m2-K

                * Wood - 3.5 W/m2-K

                * Vinyl - 2.3 W/m2-K

        _edge_to_cent_: Number between 0 and 4 for the ratio of the glass conductance near

            the frame (excluding air films) divided by the glass conductance

            at the center of the glazing (excluding air films). This is used

            only for multi-pane glazing constructions. This ratio should

            usually be greater than 1.0 since the spacer material that separates

            the glass panes is usually more conductive than the gap between panes.

            A value of 1 effectively indicates no spacer. Values should usually be

            obtained from the LBNL WINDOW program so that the unique characteristics

            of the window construction can be accounted for. (Default: 1).

        outside_proj_: Number for the distance that the frame projects outward from the

            outside face of the glazing [m]. This is used to calculate shadowing

            of frame onto glass, solar absorbed by the frame, IR emitted and

            absorbed by the frame, and convection from frame. (Default: 0).

        inside_proj_: Number for the distance that the frame projects inward from the

            inside face of the glazing [m]. This is used to calculate solar

            absorbed by the frame, IR emitted and absorbed by the frame, and

            convection from frame. (Default: 0).

        _therm_absp_: A number between 0 and 1 for the fraction of incident long

            wavelength radiation that is absorbed by the material. (Default: 0.9).

        _sol_absp_: A number between 0 and 1 for the fraction of incident solar

            radiation absorbed by the material. (Default: 0.7).

        _vis_absp_: A number b
```
### HB Room [Room]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create Honeybee Room from Honeybee Faces.

_

Note that each Room is mapped to a single zone in EnergyPlus/OpenStudio and

should always be a closed volume to ensure correct volumetric calculations and

avoid light leaks in Radiance simulations.

-



    Args:

        _faces: A list of honeybee Faces to be joined together into a Room.

        _name_: Text to set the name for the Room and to be incorporated into

            unique Room identifier. If the name is not provided, a random name

            will be assigned.

        _mod_set_: Text for the modifier set of the Room, which is used

            to assign all default radiance modifiers needed to create a radiance

            model. Text should refer to a ModifierSet within the library) such

            as that output from the "HB List Modifier Sets" component. This

            can also be a custom ModifierSet object. If nothing is input here,

            the Room will have a generic construction set that is not sensitive to

            the Room's climate or building energy code.

        _constr_set_: Text for the construction set of the Room, which is used

            to assign all default energy constructions needed to create an energy

            model. Text should refer to a ConstructionSet within the library) such

            as that output from the "HB List Construction Sets" component. This

            can also be a custom ConstructionSet object. If nothing is input here,

            the Room will have a generic construction set that is not sensitive to

            the Room's climate or building energy code.

        _program_: Text for the program of the Room (to be looked up in the ProgramType

            library) such as that output from the "HB List Programs" component.

            This can also be a custom ProgramType object. If no program is input

            here, the Room will have a generic office program. Note that ProgramTypes

            effectively map to OpenStudio space types upon export to OpenStudio.

        conditioned_: Boolean to note whether the Room has a heating and cooling

            system.



    Returns:

        report: Reports, errors, warnings, etc.

        room: Honeybee room. These can be used directly in energy and radiance

            simulations.

"""



ghenv.Component.Name = "HB Room"

ghenv.Component.NickName = 'Room'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'Honeybee'

ghenv.Component.SubCategory = '0 :: Create'

ghenv.Component.AdditionalHelpFromDocStrings = "2"





try:  # import the core honeybee dependencies

    from honeybee.room import 
```
### HB ConstructionSet [ConstructionSet]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a ConstructionSet object containing all energy constructions needed to

create an energy model. ConstructionSets can be assigned to Honeybee Rooms to

specify all default constructions on the Room.

-



    Args:

        _name: Text to set the name for the ConstructionSet and to be incorporated

            into a unique ConstructionSet identifier. If None, a random one will

            be genrated.

        base_constr_set_: An optional ConstructionSet object that will be used

            as the starting point for the new ConstructionSet output from this

            component. This can also be text for the name of a ConstructionSet

            within the library such as that output from the "HB Search Construction

            Sets" component. If None, the Honeybee "Generic Default Construction

            Set" will be used as the base.

        _exterior_subset_: A construction subset list from the "HB Exterior Construction

            Subset" component. Note that None values in this list correspond to

            no change to the given construction in the base_constr_set_.

        _ground_subset_: A construction subset list from the "HB Ground Construction

            Subset" component. Note that None values in this list correspond to

            no change to the given construction in the base_constr_set_.

        _interior_subset_: A construction subset list from the "HB Interior Construction

            Subset" component. Note that None values in this list correspond to

            no change to the given construction in the base_constr_set_.

        _subface_subset_: A construction subset list from the "HB Subface Subset"

            component. Note that None values in this list correspond to no

            change to the given construction in the base_constr_set_.



    Returns:

        constr_set: A ConstructionSet object that can be assigned to Honeybee

            Rooms in order to specify all default constructions on the Room.

"""



ghenv.Component.Name = "HB ConstructionSet"

ghenv.Component.NickName = 'ConstructionSet'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '0 :: Basic Properties'

ghenv.Component.AdditionalHelpFromDocStrings = "3"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.constructionset import ConstructionSet

    from honeybee_energy.
```
### HB Face [Face]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create Honeybee Face

-



    Args:

        _geo: Rhino Brep or Mesh geometry.

        _name_: Text to set the name for the Face and to be incorporated into

            unique Face identifier. If the name is not provided, a random name

            will be assigned.

        _type_: Text for the face type. The face type will be used to set the

            material and construction for the surface if they are not assigned

            through the inputs below. The default is automatically set based

            on the normal direction of the Face (up being RoofCeiling, down

            being Floor and vertically-oriented being Wall).

            Choose from the following:

                - Wall

                - RoofCeiling

                - Floor

                - AirBoundary

        _bc_: Text for the boundary condition of the face. The boundary condition

            is also used to assign default materials and constructions as well as

            the nature of heat excahnge across the face in energy simulation.

            Default is Outdoors unless all vertices of the geometry lie below

            the below the XY plane, in which case it will be set to Ground.

            Choose from the following:

                - Outdoors

                - Ground

                - Adiabatic

        ep_constr_: Optional text for the Face's energy construction to be looked

            up in the construction library. This can also be a custom OpaqueConstruction

            object. If no energy construction is input here, the face type and

            boundary condition will be used to assign a default.

        rad_mod_: Optional text for the Face's radiance modifier to be looked

            up in the modifier library. This can also be a custom modifier object.

            If no radiance modifier is input here, the face type and boundary

            condition will be used to assign a default.



    Returns:

        report: Reports, errors, warnings, etc.

        face: Honeybee faces. These can be used directly in radiance simulations

            or can be added to a Honeybee room for energy simulation.

"""



ghenv.Component.Name = "HB Face"

ghenv.Component.NickName = 'Face'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'Honeybee'

ghenv.Component.SubCategory = '0 :: Create'

ghenv.Component.AdditionalHelpFromDocStrings = "3"



try:  # import the core honeybee dependencies

    from honeybee.face import Face

    from honeybee.facetype import face_types

    from honeybee.boundarycondition import boundary_conditions

    from honeybee.typing import clean_
```
### HB Weekly Schedule [WeeklySchedule]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>





"""

Create a schedule from lists of daily values for each day of the week.

-



    Args:

        _sun: A list of 24 values that represent the schedule values at each

            hour of Sunday. This can also be a single constant value for the

            whole day.

        _mon: A list of 24 values that represent the schedule values at each

            hour of Monday. This can also be a single constant value for the

            whole day.

        _tue: A list of 24 values that represent the schedule values at each

            hour of Tuesday. This can also be a single constant value for the

            whole day.

        _wed: A list of 24 values that represent the schedule values at each

            hour of Wednesday. This can also be a single constant value for the

            whole day.

        _thu: A list of 24 values that represent the schedule values at each

            hour of Thursday. This can also be a single constant value for the

            whole day.

        _fri: A list of 24 values that represent the schedule values at each

            hour of Friday. This can also be a single constant value for the

            whole day.

        _sat: A list of 24 values that represent the schedule values at each

            hour of Saturday. This can also be a single constant value for the

            whole day.

        _holiday_: An optional list of 24 values that represent the schedule

            values at each hour of holidays. This can also be a single constant

            value for the whole day. If no values are input here, the schedule

            for Sunday will be used for all holidays.

        _summer_des_: An optional list of 24 values that represent the schedule

            values at each hour of the summer design day. This can also be a

            single constant value for the whole day. If None, the daily

            schedule with the highest average value will be used unless

            the _type_limit_ is Temperature, in which case it will be

            the daily schedule with the lowest average value.

        _winter_des_: An optional list of 24 values that represent the schedule

            values at each hour of the summer design day. This can also be a

            single constant value for the whole day. If None, the daily

            schedule with the lowest average value will be used unless

            the _type_limit_ is Temperature, in which case it will be

            the daily schedule with the highest average value.

        _name_: Text to set the name for the Schedule and to be incorporated

            into a unique Sched
```
### HB Schedule to Data [SchToData]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>





"""

Get a ladybug DataCollection representing this schedule at a given timestep.

_

This DataCollection can be used to visualize timeseries schedule values over

the entire period of a simulation using a component like the "LB Hourly Plot".

_

This DataCollection can also be used in the crafting of conditional statements

with the ladybug components. For example, making a psychrometric chart of zone

temperature/humidity for only the hours that the occupancy schedule is above a

certain threshold.

-



    Args:

        _schedule: A ScheduleRuleSet or SchedileFixedInterval for which a DataCollection

            of timeseries schedule values will be produced. This can also be the

            identifier of a Schedule to be looked up in the schedule library.

        analysis_period_: An optional AnalysisPeriod to set the start and end datetimes

            of the resulting DataCollection. The timestep of this AnalysisPeriod

            will also be used to determine the timestep of the resulting DataCollection.

        _week_start_day_: An optional text string to set the start day of the week

            of the schedule timeseries data. Default: Sunday. Choose from the following:

                * Sunday

                * Monday

                * Tuesday

                * Wednesday

                * Thursday

                * Friday

                * Saturday

        holidays_: An optional list of strings (eq: 25 Dec) to represent the holidays

            in the resulting timeseries. Holiday schedules will be used for these

            dates in the resulting timeseries.

    

    Returns:

        data: A ladybug DataCollection representing the timeseries values of the schedule.

            This can be used to visualize timeseries schedule values over the entire

            period of a simulation using a component like the "LB Hourly Plot".

"""



ghenv.Component.Name = "HB Schedule to Data"

ghenv.Component.NickName = 'SchToData'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '2 :: Schedules'

ghenv.Component.AdditionalHelpFromDocStrings = "2"





try:  # import the honeybee-energy dependencies

    from honeybee_energy.schedule.ruleset import ScheduleRuleset

    from honeybee_energy.lib.schedules import schedule_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import the ladybug dependencies

    from ladybug.dt import Date, DateTime

except ImportError as e:

    raise ImportError('\nFailed to import ladybug:\n\t{}'.format(e))



t
```
### LB Hourly Plot [HourlyPlot]
```
# Ladybug: A Plugin for Environmental Analysis (GPL)

# This file is part of Ladybug.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Ladybug; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a colored plot of any hourly data collection.

-



    Args:

        _data: A HourlyContinuousCollection or HourlyDiscontinuousCollection

            which will be used to generate the hourly plot.

        _base_pt_: An optional Point3D to be used as a starting point to generate

            the geometry of the plot (Default: (0, 0, 0)).

        _x_dim_: A number to set the X dimension of the mesh cells (Default: 1 meters).

        _y_dim_: A number to set the Y dimension of the mesh cells (Default: 4 meters).

        _z_dim_: A number to set the Z dimension of the entire chart. This will

            be used to make the colored_mesh3d of the chart vary in the Z

            dimension according to the data. The value input here should usually be

            several times larger than the x_dim or y_dim in order to be noticable

            (e.g. 100). If 0, the colored_mesh3d will simply be flat. (Default: 0).

        reverse_y_: Boolean to note whether the Y-axis of the chart is reversed

            If True, time over the course of the day will flow from the top of

            the chart to the bottom instead of the bottom to the top.

        clock_24_: Boolean to note whether the hour labels on the Y-Axis of the chart

            should be in 24-hour clock format (eg. 18:00) or they should be

            in 12-hour clock format (eg. 6PM).

        legend_par_: An optional LegendParameter object to change the display of the

            HourlyPlot. This can also be a list of legend parameters to be

            applied to the different connected _data.

        statement_: A conditional statement as a string (e.g. a > 25).

            .

            The variable of the first data collection should always be named 'a'

            (without quotations), the variable of the second list should be

            named 'b', and so on.

            .

            For example, if three data collections are connected to _data

            and the following statement is applied:

            '18 < a < 26 and b < 80 and c > 2'

            The resulting collections will only include values where the first

            data collection is between 18 and 26, the second collection is less

            than 80 and the third collection is greater than 2.

        period_: A Ladybug analysis period to be applied to all of the input _data.



    Returns:

        report: ...

        mesh: A colored mesh derived from the input _data. Multiple meshes will

            be output for several data collections are input.

        legend: Geometry representing the legend for each mesh.

        borde
```
### HB People [People]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a People object that can be used to create a ProgramType or be assigned

directly to a Room.

-



    Args:

        _name_: Text to set the name for the People and to be incorporated

            into a unique People identifier. If None, a unique name will

            be generated.

         _ppl_per_area: A numerical value for the number of people per square

            meter of floor area.

        _occupancy_sch: A fractional schedule for the occupancy over the course

            of the year. The fractional values in this schedule will get multiplied

            by the _people_per_area to yield a complete occupancy profile.

        _activity_sch_: A schedule for the activity of the occupants over the course

            of the year. The type limt of this schedule should be "Activity Level"

            and the values of the schedule equal to the number of Watts given off

            by an individual person in the room. If None, it will a default constant

            schedule with 120 Watts per person will be used, which is typical of

            awake, adult humans who are seated.

        latent_fraction_: An optional number between 0 and 1 for the fraction of the heat

            given off by people that is latent (as opposed to sensible). when

            unspecified, this will be autocalculated based on the activity level

            and the conditions in the room at each timestep of the simulation.

            The autocalculation therefore accounts for the change in heat loss

            through respiration and sweating that occurs at warmer temperatures

            and higher activity levels, which is generally truer to physics

            compared to a fixed number.



    Returns:

        people: A People object that can be used to create a ProgramType or

            be assigned directly to a Room.

"""



ghenv.Component.Name = "HB People"

ghenv.Component.NickName = 'People'

ghenv.Component.Message = '1.8.1'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '3 :: Loads'

ghenv.Component.AdditionalHelpFromDocStrings = "3"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

    from honeybee.altnumber import autocalculate

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:

    from honeybee_energy.load.people import People

    from honeybee_energy.lib.schedules import schedule_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:

    from 
```
### HB Lighting [Lighting]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a Lighting object that can be used to create a ProgramType or be assigned

directly to a Room.

-



    Args:

        _name_: Text to set the name for the Lighting and to be incorporated

            into a unique Lighting identifier. If None, a unique name will

            be generated.

         _watts_per_area: A numerical value for the lighting power density in

            Watts per square meter of floor area.

        _schedule: A fractional for the use of lights over the course of the year.

            The fractional values will get multiplied by the _watts_per_area to

            yield a complete lighting profile.

        _radiant_fract_: A number between 0 and 1 for the fraction of the total

            lighting load given off as long wave radiant heat.

            Default: 0.32 (representative of pendant lighting).

        _visible_fract_: A number between 0 and 1 for the fraction of the total

            lighting load given off as short wave visible light.

            Default: 0.25  (representative of pendant lighting).

        return_fract_: A number between 0 and 1 for the fraction of the total

            lighting load that goes into the zone return air (into the zone outlet

            node). Default: 0.0 (representative of pendant lighting).

        baseline_: An optional number for the baseline lighting power density in

            W/m2 of floor area. This baseline is useful to track how much

            better the installed lights are in comparison to a standard like

            ASHRAE 90.1. If set to None, it will default to 11.84029 W/m2,

            which is that ASHRAE 90.1-2004 baseline for an office.



    Returns:

        lighting: A Lighting object that can be used to create a ProgramType or

            be assigned directly to a Room.

"""



ghenv.Component.Name = "HB Lighting"

ghenv.Component.NickName = 'Lighting'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '3 :: Loads'

ghenv.Component.AdditionalHelpFromDocStrings = "3"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:

    from honeybee_energy.load.lighting import Lighting

    from honeybee_energy.lib.schedules import schedule_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise
```
### HB Equipment [Equipment]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create an Equipment object that can be used to specify equipment usage in a ProgramType.

-



    Args:

        _name_: Text to set the name for the Equipment and to be incorporated

            into a unique Equipment identifier. If None, a unique name will

            be generated.

         _watts_per_area: A numerical value for the equipment power density in

            Watts per square meter of floor area.

        _schedule: A fractional schedule for the use of equipment over the course of

            the year. The fractional values will get multiplied by the

            _watts_per_area to yield a complete equipment profile.

        radiant_fract_: A number between 0 and 1 for the fraction of the total

            equipment load given off as long wave radiant heat. (Default: 0).

        latent_fract_: A number between 0 and 1 for the fraction of the total

            equipment load that is latent (as opposed to sensible). (Default: 0).

        lost_fract_: A number between 0 and 1 for the fraction of the total

            equipment load that is lost outside of the zone and the HVAC system.

            Typically, this is used to represent heat that is exhausted directly

            out of a zone (as you would for a stove). (Default: 0).

        gas_: Set to "True" to have the output Equipment object be for GasEquipment

            (as opposed to ElectricEquipment).



    Returns:

        equip: An Equipment object that can be used to specify equipment usage in

            a ProgramType.

"""



ghenv.Component.Name = 'HB Equipment'

ghenv.Component.NickName = 'Equipment'

ghenv.Component.Message = '1.8.1'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '3 :: Loads'

ghenv.Component.AdditionalHelpFromDocStrings = '3'



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:

    from honeybee_energy.load.equipment import ElectricEquipment, GasEquipment

    from honeybee_energy.lib.schedules import schedule_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    # make a default Equipment name if none is provided

    name = clean_and_id_ep_string('Equipment') if _name_ is None else \

        clean_e
```
### HB ProgramType [ProgramType]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a ProgramType object possessing all schedules and loads defining the

usage of a space.

_

ProgramTypes can be assigned to Honeybee Rooms to specify all default schedules

and loads on the Room.

-



    Args:

        _name_: Text to set the name for the ProgramType and to be incorporated

            into a unique ProgramType identifier.

        base_program_: An optional ProgramType object that will be used as the

            starting point for the new ProgramType output from this component.

            This can also be text for the name of a ProgramType within the library

            such as that output from the "HB Search Program Types" component.

            If None, a Plenum program type will be used as the base with no loads,

            setpoints, or ventilation requirements assigned.

        _people_: A People object to describe the occupancy of the program. If None,

            no occupancy will be assumed for the program. (Default: None).

        _lighting_: A Lighting object to describe the lighting usage of the program.

            If None, no lighting will be assumed for the program. (Default: None).

        _electric_equip_: An ElectricEquipment object to describe the usage

            of electric equipment within the program. If None, no electric equipment

            will be assumed for the program. (Default: None).

        _gas_equip_: A GasEquipment object to describe the usage of gas equipment

            within the program. If None, no gas equipment will be assumed for

            the program. (Default: None).

        _hot_water_: A ServiceHotWater object to describe the usage of hot water

            within the program. If None, no hot water will be assumed for

            the program. (Default: None).

        _infiltration_: An Infiltration object to describe the outdoor air leakage of

            the program. If None, no infiltration will be assumed for the

            program. (Default: None).

        _ventilation_: A Ventilation object to describe the minimum outdoor air

            requirement of the program. If None, no ventilation requirement will

            be assumed for the program. (Default: None).

        _setpoint_: A Setpoint object to describe the temperature and humidity

            setpoints of the program.  If None, the ProgramType cannot be assigned

            to a Room that is conditioned. (Default: None).



    Returns:

        program: A ProgramType object that can be assigned to Honeybee Rooms in

            order to specify all default schedules and loads on the Room.

"""



ghenv.Component.Name = 'HB Pr
```
### HB Apply Setpoint Values [ApplySetpointVals]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Apply values for setpoints to a Room or ProgramType.

-



    Args:

        _room_or_program: Honeybee Rooms or ProgramType objects to which the input

            setpoints should be assigned. This can also be the identifier of a

            ProgramType to be looked up in the program type library. This can

            also be a Honeybee Model for which all Rooms will be assigned

            the setpoints.

        cooling_setpt_: A numerical value for a single constant temperature for

            the cooling setpoint [C].

        heating_setpt_: A numerical value for a single constant temperature for

            the heating setpoint [C].

        humid_setpt_: A numerical value for a single constant value for the

            humidifying setpoint [%].

        dehumid_setpt_: A numerical value for a single constant value for the

            dehumidifying setpoint [%].

        cutout_difference_: An optional positive number for the temperature difference between the

            cutout temperature and the setpoint temperature. Specifying a non-zero

            number here is useful for modeling the throttling range associated

            with a given setup of setpoint controls and HVAC equipment. Throttling

            ranges describe the range where a zone is slightly over-cooled or

            over-heated beyond the thermostat setpoint. They are used to avoid

            situations where HVAC systems turn on only to turn off a few minutes later,

            thereby wearing out the parts of mechanical systems faster. They can

            have a minor impact on energy consumption and can often have significant

            impacts on occupant thermal comfort, though using the default value

            of zero will often yield results that are close enough when trying

            to estimate the annual heating/cooling energy use. Specifying a value

            of zero effectively assumes that the system will turn on whenever

            conditions are outside the setpoint range and will cut out as soon

            as the setpoint is reached. (Default: 0).



    Returns:

        report: Reports, errors, warnings, etc.

        mod_obj: The input Rooms or ProgramTypes with their setpoint values edited.

"""



ghenv.Component.Name = "HB Apply Setpoint Values"

ghenv.Component.NickName = 'ApplySetpointVals'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = '3 :: Loads'

ghenv.Component.AdditionalHelpFromDocStrings = "2"



import uuid



try:

    from honeybee.model import Model

    from honeybee.room import Room

e
```
### HB Internal Mass [InternalMass]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>





"""

Assign internal thermal masses to Rooms, which can be used to account for the

effects of furniture inside Rooms or other massive building components like

staircases, hearths, etc.

_

The component accepts either Rhino geometry (representing furniture or massive

elements) or a numerical value of the mass's surface area. Several of these

components can be used in a series to descibe different internal masses made

of different materials.

_

Note that internal masses assigned this way cannot "see" solar radiation that

may potentially hit them and, as such, caution should be taken when using this

component with internal mass objects that are not always in shade. Masses are

factored into the the thermal calculations of the Room by undergoing heat

transfer with the indoor air.

-



    Args:

        _rooms: Honeybee Rooms to which internal masses should be assigned.

        _geo_or_area: A list of Rhino breps or meshes representing the surfaces of internal

            masses that are exposed to the air of the Room. Alternatively, this can

            be a number or list of numbers representing the surface area of the

            internal masses (in square meters) that are exposed to the Room air.

            _

            In the case of Rhino geometry representing the surfaces of internal

            masses, this component will determine which Room the geometry is in.

            However, geometry must lie COMPLETELY inside a single Room and

            cannot span between Rooms or span outside the building. If a geometry

            lies between two Rooms, it should be split in two along the boundary

            between the Rooms. Also note that geometries are assumed to have only

            one side exposed to the Room air so, if they are meant to represent

            a 2-sided object, the geometry should be duplicated and offset.

            _

            In the case of numbers representing the the surface area of the

            internal masses, inputs can be either a single number (which will be

            used to put internal masses into all Rooms using the specified

            surface area), or it can be a list of numbers that matches the input

            Rooms, which can be used to assign different amounts of mass surface

            area to different Rooms. All numbers are assumed to be in square meters.

        _construction: An OpaqueConstruction object that represents the material

            that the internal thermal mass is composed of. This can also be

            text for the identifier of the construction within the library.

        _name_
```
### HB Opaque Material [OpaqueMat]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a standard opaque material, which can be plugged into the "HB Opaque

Construction" component.

-



    Args:

        _name_: Text to set the name for the material and to be incorporated into

            a unique material identifier.

        _thickness: Number for the thickness of the material layer [m].

        _conductivity: Number for the thermal conductivity of the material [W/m-K].

        _density: Number for the density of the material [kg/m3].

        _spec_heat: Number for the specific heat of the material [J/kg-K].

        _roughness_: Text describing the relative roughness of the material.

            Must be one of the following: 'VeryRough', 'Rough', 'MediumRough',

            'MediumSmooth', 'Smooth', 'VerySmooth'. (Default: 'MediumRough').

        _therm_absp_: A number between 0 and 1 for the fraction of incident long

            wavelength radiation that is absorbed by the material. (Default: 0.9).

        _sol_absp_: A number between 0 and 1 for the fraction of incident solar

            radiation absorbed by the material. (Default: 0.7).

        _vis_absp_: A number between 0 and 1 for the fraction of incident

            visible wavelength radiation absorbed by the material.

            Default value is the same as the _sol_absp_.



    Returns:

        mat: A standard opaque material that can be assigned to a Honeybee

            Opaque construction.

"""



ghenv.Component.Name = "HB Opaque Material"

ghenv.Component.NickName = 'OpaqueMat'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "5"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.material.opaque import EnergyMaterial

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    # set the default material properties

    _roughness_ = 'MediumRough' if _roughness_ is None else _roughness_

    _therm_absp_ = 0.9 if _therm_absp_ is None else _therm_absp_

    _sol_absp_ = 0.7 if _sol_absp_ is None else _sol_absp_

    name =
```
### HB Opaque Construction [OpaqueConstr]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create an EnergyPlus opaque construction. Material inputs can be either the

identifiers of materials within the library or a custom material made with any

of the EnergyPlus Material components.

_

Note that the _materials should be ordered from outermost (exterior) layer to the

innermost (interior) layer.

-



    Args:

        _name_: Text to set the name for the Construction and to be incorporated

            into a unique Construction identifier.

        _materials: List of materials in the construction (from exterior to interior).

            These materials can be either fully-detailed material objects built

            with the material components or text for a material identifier to be

            looked up in the opaque material library.  Note that a native Grasshopper

            "Merge" component can be used to help order the materials correctly

            for the input here.



    Returns:

        constr: An opaque construction that can be assigned to Honeybee

            Faces or ConstructionSets.

"""



ghenv.Component.Name = "HB Opaque Construction"

ghenv.Component.NickName = 'OpaqueConstr'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'HB-Energy'

ghenv.Component.SubCategory = "1 :: Constructions"

ghenv.Component.AdditionalHelpFromDocStrings = "4"



try:  # import the core honeybee dependencies

    from honeybee.typing import clean_and_id_ep_string, clean_ep_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the honeybee-energy dependencies

    from honeybee_energy.construction.opaque import OpaqueConstruction

    from honeybee_energy.lib.materials import opaque_material_by_identifier

except ImportError as e:

    raise ImportError('\nFailed to import honeybee_energy:\n\t{}'.format(e))



try:  # import ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





if all_required_inputs(ghenv.Component):

    name = clean_and_id_ep_string('OpaqueConstruction') if _name_ is None else \

        clean_ep_string(_name_)



    material_objs = []

    for material in _materials:

        if isinstance(material, str):

            material = opaque_material_by_identifier(material)

        material_objs.append(material)



    constr = OpaqueConstruction(name, material_objs)

    if _name_ is not None:

        constr.display_name = _name_
```
### HB Window Opening [WindowOpen]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Define the window opening properties for all operable apertures of a Room.

_

By default, the properties assigned by this component are translated into simple

ZoneVentilation objects in the resulting IIDF, which can approximate airflow

from both single-sided bouyancy-driven ventilation as well as wind-driven cross

ventilation. Bouyancy-driven flow can happen for essentially all openings while

wind-driven flow can only happen when there are pressure differences across

windows on opposite sides of a Room.

_

Simple ZoneVentilation is computed using the following formulas:

_

VentilationWind = WindCoefficient * OpeningArea * Schedule * WindSpeed

VentilationStack = StackDischargeCoefficient * OpeningArea * ScheduleValue * 

    SQRT(2 * GravityAccelration * HeightNPL * (|(TempZone - TempOutdoors)| / TempZone)) 

TotalVentilation = SQRT((VentilationWind)^2 + (VentilationStack)^2)

_

Note that the (OpeningArea) term is derived from the _fract_area_oper_ and the area

of each aperture while the (HeightNPL) term is derived from the _fract_height_oper_

and the height of each aperture.  The "NPL" stands for "Neutral Plane" and the

whole term represents the height from midpoint of lower opening to the neutral

pressure level of the window (computed as 1/4 of the height of each Aperture in

the translation from honeybee to IDF).

_

More complex airflow phenomena can be modeled by using this component in conjunction

with with the Airflow Network (AFN) component. Note that the window opening

properties assigned by this component are still relevant for such AFN simulations.

-



    Args:

        _rooms: Honeybee Room objects to which window ventilation opening properties

            will be assigned. Note that this component only assigns such properties

            to operable Apertures on the rooms. If the is_operable property

            of any of a room's apertures is not True, no opening properties

            will be assigned.

        _vent_cntrl: A Ventilation Control object from the "HB Ventilation Control"

            component, which dictates the opening behaviour of the Room's apertures.

        _fract_area_oper_: A number between 0.0 and 1.0 for the fraction of the

            window area that is operable. (Default: 0.5, typical of sliding windows).

        _fract_height_oper_: A number between 0.0 and 1.0 for the fraction

            of the distance from the bottom of the window to the top that is

            operable. (Default: 1.0, typical of windows that slide horizontally).

        _discharge_coeff_: A number between 0.0 and 1.0 that will be multipled

         
```
### HB Ventilation Control [VentControl]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a Ventilation Control object to dictate the temperature setpoints and

schedule for ventilative cooling (eg. opening windows).

_

Note the all of the default setpoints of this object are set to always perform

ventilative cooling such that one can individually decide which setpoints

are relevant to a given ventilation strategy.

-



    Args:

        min_in_temp_: A number between -100 and 100 for the minimum indoor

            temperature at which to ventilate in Celsius. Typically,

            this variable is used to initiate ventilation with values

            around room temperature above which the windows will open

            (eg. 22 C). (Default: -100 C).

        max_in_temp_: A number between -100 and 100 for the maximum indoor

            temperature at which to ventilate in Celsius. This can be

            used to set a maximum temperature at which point ventilation is

            stopped and a cooling system is turned on. (Default: 100 C).

        min_out_temp_: A number between -100 and 100 for the minimum outdoor

            temperature at which to ventilate in Celsius. This can be used

            to ensure ventilative cooling doesn't happen during the winter even

            if the Room is above the min_in_temp. (Default: -100 C).

        max_out_temp_: A number between -100 and 100 for the maximum outdoor

            temperature at which to ventilate in Celsius. This can be used

            to set a limit for when it is considered too hot outside for

            ventilative cooling. (Default: 100).

        delta_temp_: A number between -100 and 100 for the temperature differential

            in Celsius between indoor and outdoor below which ventilation

            is shut off.  This should usually be a positive number so that

            ventilation only occurs when the outdoors is cooler than the indoors.

            Negative numbers indicate how much hotter the outdoors can be than

            the indoors before ventilation is stopped. (Default: -100).

        _schedule_: An optional schedule for the ventilation over the course of

            the year. This can also be the name of a schedule to be looked up

            in the standards library. Note that this is applied on top of any

            setpoints. The type of this schedule should be On/Off and values

            should be either 0 (no possibility of ventilation) or 1 (ventilation

            possible). (Default: "Always On")



    Returns:

        vent_cntrl: HBZones with their airflow modified.

"""



ghenv.Component.Name = 'HB Ventilation Control'

ghenv.Component.NickNa
```
### HB Model [Model]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create a Honeybee Model, which can be sent for simulation.

-



    Args:

        rooms_: A list of honeybee Rooms to be added to the Model. Note that at

            least one Room is necessary to make a simulate-able energy model.

        faces_: A list of honeybee Faces to be added to the Model. Note that

            faces without a parent Room are not allowed for energy models.

        shades_: A list of honeybee Shades or ShadeMeshes to be added to the Model.

        apertures_: A list of honeybee Apertures to be added to the Model. Note

            that apertures without a parent Face are not allowed for energy models.

        doors_: A list of honeybee Doors to be added to the Model. Note

            that doors without a parent Face are not allowed for energy models.

        _name_: Text to be used for the Model name and to be incorporated into a unique

            model identifier. If no name is provided, it will be "unnamed" and

            a unique model identifier will be auto-generated.



    Returns:

        report: Reports, errors, warnings, etc.

        model: A Honeybee Model object possessing all of the input geometry

            objects.

"""



ghenv.Component.Name = 'HB Model'

ghenv.Component.NickName = 'Model'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'Honeybee'

ghenv.Component.SubCategory = '0 :: Create'

ghenv.Component.AdditionalHelpFromDocStrings = '1'



try:  # import the core honeybee dependencies

    from honeybee.shademesh import ShadeMesh

    from honeybee.model import Model

    from honeybee.typing import clean_string, clean_and_id_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the ladybug_rhino dependencies

    from ladybug_rhino.grasshopper import all_required_inputs

    from ladybug_rhino.config import units_system, tolerance, angle_tolerance

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))





def check_all_geo_none():

    """Check whether all of the geometry inputs to this component are None."""

    return all(obj_list == [] or obj_list == [None] for obj_list in

               (rooms_, faces_, shades_, apertures_, doors_))





if all_required_inputs(ghenv.Component) and not check_all_geo_none():

    # set a default name and get the Rhino Model units

    name = clean_string(_name_) if _name_ is not None else clean_and_id_string('unnamed')

    units = units_system()



    # separate shades and shade meshes

    shades, shade_meshes = [], []

    if len(shades_) != 0:

        for 
```
### HB Label Faces [LableFaces]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Lablel Honeybee faces and sub-faces with their attributes in the Rhino scene.

_

This can be used as a means to check that correct properties are assigned to

different faces and sub-faces.

-



    Args:

        _hb_objs: Honeybee Faces, Rooms or a Model to be labeled with their attributes

            in the Rhino scene.

        _attribute_: Text for the name of the attribute with which the faces or

            sub-faces should be labeled. The Honeybee "Face Attributes" component

            lists all of the core attributes of the room. Also, each Honeybee

            extension (ie. Radiance, Energy) includes its own component that lists

            the face and sub-face attributes of that extension. Default: "name".

        _txt_height_: An optional number for the height of the text in the Rhino

            scene.  The default is auto-calculated based on the dimensions of the

            input geometry.

        _font_: An optional name of a font in which the labels will display. This

            must be a font that is installed on this machine in order to work

            correctly. Default: "Arial".



    Returns:

        label_text: The text with which each of the faces or sub-faces are labeled.

        base_pts: The base point for each of the text labels.

        labels: The text objects that are displaying within the Rhino scene.

        wire_frame: A list of curves representing the outlines of the faces or

            sub-faces. This is useful for understanding which geometry elements

            each label corresponds to.

"""



ghenv.Component.Name = 'HB Label Faces'

ghenv.Component.NickName = 'LableFaces'

ghenv.Component.Message = '1.8.1'

ghenv.Component.Category = 'Honeybee'

ghenv.Component.SubCategory = '1 :: Visualize'

ghenv.Component.AdditionalHelpFromDocStrings = '4'



import math



try:  # import the ladybug_geometry dependencies

    from ladybug_geometry.geometry3d.plane import Plane

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_geometry:\n\t{}'.format(e))



try:  # import the core honeybee dependencies

    from honeybee.model import Model

    from honeybee.room import Room

    from honeybee.face import Face

    from honeybee.aperture import Aperture

    from honeybee.door import Door

    from honeybee.search import get_attr_nested

    from honeybee.units import parse_distance_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the ladybug_rhino dependencies

    from ladybug_rhino.fromgeometry import from_face3d_to_wireframe, from_plane

```
### HB Aperture [Aperture]
```
# Honeybee: A Plugin for Environmental Analysis (GPL)

# This file is part of Honeybee.

#

# Copyright (c) 2024, Ladybug Tools.

# You should have received a copy of the GNU Affero General Public License

# along with Honeybee; If not, see <http://www.gnu.org/licenses/>.

# 

# @license AGPL-3.0-or-later <https://spdx.org/licenses/AGPL-3.0-or-later>



"""

Create Honeybee Aperture

-



    Args:

        _geo: Rhino Brep or Mesh geometry.

        _name_: Text to set the name for the Aperture and to be incorporated into

            unique Aperture identifier. If the name is not provided, a random name

            will be assigned.

        operable_: Boolean to note whether the Aperture can be opened for ventilation.

            Default: False.

        ep_constr_: Optional text for the Aperture's energy construction to be looked

            up in the construction library. This can also be a custom WindowConstruction

            object. If no energy construction is input here, a default will be

            assigned based on the properties of the parent face that the Aperture

            is assigned to (ie. whether the Face is a RoofCeiling, whether it has

            a Surface boundary condition, etc.)

        rad_mod_: Optional text for the Aperture's radiance modifier to be looked

            up in the modifier library. This can also be a custom modifier object.

            If no radiance modifier is input here, a default will be assigned

            based on the properties of the parent face that the Aperture is

            assigned to (ie. whether the Face is a RoofCeiling, whether it has a

            Surface boundary condition, etc.)

    

    Returns:

        report: Reports, errors, warnings, etc.

        apertures: Honeybee apertures. These can be used directly in radiance

            simulations or can be added to a Honeybee face for energy simulation.

"""



ghenv.Component.Name = "HB Aperture"

ghenv.Component.NickName = 'Aperture'

ghenv.Component.Message = '1.8.0'

ghenv.Component.Category = 'Honeybee'

ghenv.Component.SubCategory = '0 :: Create'

ghenv.Component.AdditionalHelpFromDocStrings = "4"



try:  # import the core honeybee dependencies

    from honeybee.aperture import Aperture

    from honeybee.typing import clean_and_id_string

except ImportError as e:

    raise ImportError('\nFailed to import honeybee:\n\t{}'.format(e))



try:  # import the ladybug_rhino dependencies

    from ladybug_rhino.togeometry import to_face3d

    from ladybug_rhino.grasshopper import all_required_inputs, longest_list, \

        wrap_output

except ImportError as e:

    raise ImportError('\nFailed to import ladybug_rhino:\n\t{}'.format(e))



try:  # import the honeybee-energy extension

    from honeybee_energy.lib.constructions import window_construction_by_identifier

except ImportError as e:

    if len(ep_constr_) != 0:

        raise ValueError('ep_constr_ has been specified but honeybee-energy '

             
```