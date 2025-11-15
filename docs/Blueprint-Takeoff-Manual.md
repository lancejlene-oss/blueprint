# Blueprint Takeoff Training Manual

**Subtitle:** A Practical Guide for Lumber & Building-Materials Salespeople  
**Company:** Ritter Lumber  
**Version:** 1.0  
**Date:** November 15, 2025

---

## Table of Contents
1. [Chapter 1 · Introduction](#chapter-1--introduction)
2. [Chapter 2 · Blueprint Orientation](#chapter-2--blueprint-orientation)
3. [Chapter 3 · Floor Plan Reading](#chapter-3--floor-plan-reading)
4. [Chapter 4 · Wall & Framing Takeoff](#chapter-4--wall--framing-takeoff)
5. [Chapter 5 · Roof Takeoff](#chapter-5--roof-takeoff)
6. [Chapter 6 · Elevations & Siding](#chapter-6--elevations--siding)
7. [Chapter 7 · Foundation & Concrete](#chapter-7--foundation--concrete)
8. [Chapter 8 · Window & Door Schedules](#chapter-8--window--door-schedules)
9. [Chapter 9 · Material Conversion Tables](#chapter-9--material-conversion-tables)
10. [Chapter 10 · Full Example House Takeoff](#chapter-10--full-example-house-takeoff)
11. [Chapter 11 · Master Worksheets](#chapter-11--master-worksheets)

---

## Chapter 1 · Introduction
### Purpose of This Manual
Ritter Lumber salespeople act as translators between architectural drawings and job-site deliveries. This manual gives a structured path for turning any residential plan set into verified material quantities, even if you have never performed a takeoff before. Each chapter builds on the previous one so that, by the end, you can complete a full takeoff, document your assumptions, and communicate confidently with builders.

### Learning Outcomes
By working through the manual in order, you will be able to:
- Interpret every sheet inside a typical home plan set and recognize the information that affects material counts.
- Read and scale floor plans, elevations, sections, and schedules without guesswork.
- Convert architectural dimensions into lumber, panel, concrete, and finish-material quantities using standard formulas.
- Spot plan revisions, alternates, and code notes that change what must be priced.
- Record takeoff decisions on printable worksheets so that another salesperson can audit your work.

### How to Use the Manual
1. **Progress sequentially.** Later chapters assume you have mastered earlier vocabulary and processes.
2. **Replicate the examples.** Rework every numeric example by hand or in a spreadsheet so the math becomes second nature.
3. **Practice on real plans.** After each chapter, pull a current Ritter Lumber plan set and find the corresponding information on those sheets.
4. **Document assumptions.** Any time you make an estimation choice (stud spacing, waste, grade changes), write it on the worksheets so the project manager knows what was priced.
5. **Leverage the diagrams.** Each chapter references diagrams housed under `docs/img/`. Even if the graphics are not printed yet, the descriptions explain the intent so you can visualize the layout.

### Manual Structure
| Chapter | Focus |
| --- | --- |
| 01 | Orientation to the manual, learning goals, and usage tips |
| 02 | Blueprint orientation: sheet types, title blocks, scales |
| 03 | Floor plan reading: walls, openings, symbols, dimension strings |
| 04 | Wall framing takeoff: studs, plates, headers, example calculations |
| 05 | Roof takeoff: geometry, slope factors, decking, shingles |
| 06 | Elevations & siding: façade analysis, siding squares, waste |
| 07 | Foundation & concrete: slabs, footings, rebar, volume math |
| 08 | Window & door schedules: interpreting tags and framing needs |
| 09 | Material conversion tables: quick-reference multipliers |
| 10 | Full example house takeoff: step-by-step quantities |
| 11 | Master worksheets: printable templates for field use |

### Tools You Will Need
- Printed or digital plan set (PDF with scale bar preferred).
- Scale ruler for paper plans; PDF measurement tool for digital sets.
- Basic calculator or spreadsheet (Excel, Sheets, or company estimating software).
- Highlighters for paper sets, or layered markups in Bluebeam/PlanSwift.
- This manual (digital or printed) and the master worksheets for recording counts.

### Success Check
Before moving to Chapter 2, confirm you can:
- Explain in your own words why documenting assumptions prevents supply disputes.
- List the plan sheets you expect in a typical residential set.
- Describe how you will keep your takeoff organized (colors, worksheets, filenames).

---

## Chapter 2 · Blueprint Orientation
### Why Orientation Matters
Before counting lumber, make sure you understand the entire plan set. Misreading a title block or skipping an addendum can cost Ritter Lumber thousands in returned materials or job delays. This chapter teaches you how to scan the drawings methodically so nothing is missed.

### Key Concepts
- **Plan Set Overview:** Site plan, floor plans, elevations, sections, details, schedules, specifications, and structural sheets all influence material counts.
- **Sheet Numbering:** Architectural sheets typically use the `A` prefix (e.g., `A1.1`), structural sheets use `S`, mechanical `M`, electrical `E`, plumbing `P`, and so on. Revisions add suffixes (e.g., `A1.1R1`).
- **Title Block Essentials:** Project name, sheet title, drawn-by initials, checked-by initials, scale, issue date, and revision history appear here—usually in the lower-right corner.
- **Orientation Cues:** North arrow, scale bar, grid lines, and legends make sure you interpret dimensions correctly.
- **Revision Clouds:** Highlighted cloud shapes plus delta symbols flag changes; always verify you are working from the latest revision noted in the title block.

### Step-by-Step Orientation Process
1. **Start with the cover sheet.** Note project name, lot number, client, and the full index of sheets.
2. **Mark current revisions.** Check the revision schedule for the latest date; initial it on your copy to confirm you saw it.
3. **Locate the site plan (usually `C` or `A0`).** Confirm orientation, setbacks, and grading notes that may drive retaining walls or fill materials.
4. **Skim architectural sheets in order.** Floor plans (`A2.x`), elevations (`A4.x`), sections (`A5.x`), details (`A6.x`), schedules (`A8.x`). Note any scope alternates called out in clouds or boxed text.
5. **Confirm structural data.** Structural notes, framing plans, and detail sheets override architectural assumptions when there is a conflict.
6. **Read general notes.** Pay attention to nailing patterns, energy code requirements, and specified materials (e.g., “all exterior walls 2x6 @ 16" O.C.”).
7. **Identify schedules and legends.** Mark their sheet numbers. You will need the window/door schedule, finish schedule, and any wall legend that describes assemblies.
8. **Verify scale.** Title block scale applies to the entire sheet unless otherwise noted. For paper prints, lay a scale ruler on a known dimension (like a labeled 10'-0" room) to confirm the scale is accurate. For PDFs, confirm the viewer is at 100% and use the measurement tool to verify.

### Diagram Reference
![Plan sheet orientation](img/plan-orientation.svg)
The diagram illustrates a sample architectural sheet showing the title block in the lower-right corner, the north arrow near the main floor plan, a scale bar below the plan, a legend outlining wall and hatch symbols, and revision clouds with delta markers along one elevation. Use it to visualize how critical navigation cues cluster around the drawing edges.

### Worked Example: Verifying Scale on Paper and PDF
1. The title block lists the main floor plan scale as 1/4" = 1'-0". A living room dimension string shows 15'-0".
2. On paper, place your architectural scale ruler set to 1/4". Align zero with one wall face; the opposite wall should land exactly at 15'. If it measures 15'-3", the print scaled up 2%. Either note the variance or reprint to correct scale.
3. In a PDF viewer (Adobe or Bluebeam), set zoom to 100%. Use the measurement tool to click wall-to-wall. If it reads 14'-10", adjust zoom until the dimension reads 15'-0" (usually ~101.5%). Lock that zoom and proceed.
4. Document the confirmation: “Scale verified 1/4"=1'-0" @ 100% zoom” or note the adjusted percentage.

### Pre-Takeoff Checklist
- [ ] Latest revision and addenda noted
- [ ] Structural sheets reviewed for overrides
- [ ] Scale verified on printed/PDF set
- [ ] Alternates and owner options highlighted
- [ ] Schedule locations bookmarked or tabbed
- [ ] General notes reviewed for material specs

### Tips & Common Mistakes
- **Tip:** Use colored sticky tabs or digital bookmarks for each sheet so you can flip between floor plans and details quickly.
- **Tip:** Circle specification sections that reference materials you supply (trusses, siding, LVLs) and copy the note onto your worksheet.
- **Mistake:** Starting a takeoff from a half-size print that was downscaled without your knowledge. Always measure a dimension before counting.
- **Mistake:** Ignoring civil or landscape sheets that call for retaining timbers or special treatments you could supply.

### Recap
A disciplined orientation prevents rework later. You now know how to interpret title blocks, confirm scales, track revisions, and locate every sheet you will touch during a takeoff. With this foundation, you are ready to read floor plans in detail.

---

## Chapter 3 · Floor Plan Reading
### Why Floor Plans Drive the Takeoff
Floor plans show every wall, opening, and symbol that determines framing, finishes, and mechanical rough-ins. Reading them accurately allows you to quantify materials and catch architectural intent before it becomes a job-site question.

### Key Concepts
- **Wall Types:** Exterior walls typically drawn with thicker line weights and hatching; interior partitions use thinner lines. Legends define whether walls are 2x4, 2x6, or specialty assemblies.
- **Openings:** Doors, windows, cased openings, and overhead doors share similar symbols with swing arcs or roller indications. Tags like `D3` or `W2` tie back to schedules.
- **Dimension Strings:** Outer strings provide overall building width/length, middle strings locate structural grids, and inner strings locate openings and interior walls. Read them from exterior to interior.
- **Symbols & Callouts:** Electrical outlets, plumbing fixtures, section cuts, and detail bubbles appear across the plan. Each symbol should be understandable using the sheet’s legend or a company standard.

### Diagram Reference
![Floor plan basics](img/floor-plan-basic.svg)
The diagram depicts a simplified first-floor plan with thick exterior walls, thinner interior partitions, swing arcs on doors, window tags (`W1`, `W2`), dual dimension strings (overall and segment), and callouts pointing to sections (`A5/2`). Grid lines `A-D` and `1-4` show how to align notes between sheets.

### Step-by-Step Reading Process
1. **Trace the Perimeter:** Highlight the exterior wall centerline. Note wall thickness changes (e.g., 2x6 front elevation, 2x4 sides).
2. **Identify Structural Walls:** Look for double-line hatching or notes like “bearing wall” that require different stud counts or beams.
3. **Mark Openings:** Circle each door and window, writing its tag next to it. Confirm swing direction so headers are sized correctly later.
4. **Read Dimension Strings:** Start with the overall dimension to confirm building size. Move inward to locate wall segments and opening centers. Record anomalies (like odd spacing) for later review.
5. **Catalog Symbols:** Use the legend to identify fixtures. Even if you do not price electrical or plumbing, knowing fixture locations helps validate room layouts and opening counts.
6. **Follow Callouts:** Section bubbles (e.g., `2/A5.1`) tell you where to find additional construction info. Tab those sheets before you start counting framing around that condition.

### Worked Example: Reading a Living Area Layout
- A 36'-0" x 24'-0" footprint has exterior walls labeled "2x6 stud wall @ 16" O.C., R-21 insulation" on the legend.
- Interior partitions are noted as "2x4 stud wall @ 16" O.C." By measuring dimension strings, you find a 12'-0" living room wall with two interior doors (`D2`) and one cased opening (`CO1`).
- Window tags `W1` (3040) and `W3` (3050) appear with centerline dimensions from the adjacent corner called out in the inner dimension string.
- Electrical symbols show a ceiling fan in the living room; while you do not price it, the symbol confirms the plan is the correct sheet (not a structural-only floor plan).

### Tips & Common Mistakes
- **Tip:** Use different highlighter colors: yellow for walls, green for windows, blue for doors. It speeds up re-checking later.
- **Tip:** When a dimension string seems off (e.g., numbers do not add up to the overall dimension), look for small jogs or wall thickness notes.
- **Mistake:** Ignoring interior step-downs or ceiling height transitions called out in bubbles; they can affect stud lengths and trim packages.
- **Mistake:** Misreading pocket doors as cased openings; check for the dashed pocket outline inside the wall.

### Self-Check Worksheet
| Item to Locate | Notes from Your Plan Set |
| --- | --- |
| Longest exterior wall length | |
| Thickest wall assembly (dimension and location) | |
| Total number of door tags | |
| Total number of window tags | |
| Dimension reference for the kitchen sink centerline | |

#### Additional Prompts
1. List three symbols you did not recognize at first and describe how you decoded them.
2. Identify any notes that change standard wall spacing or materials.
3. Mark one section callout and record the sheet and detail number it references.

### Recap
You can now read floor plans with confidence: differentiating wall types, locating openings, interpreting dimension strings, and cross-referencing symbols. This skill sets up the precise counting required in the framing chapter.

---

## Chapter 4 · Wall & Framing Takeoff
### Why Accurate Framing Counts Matter
Framing lumber is usually the largest material cost on a residential project. Overestimating ties up the builder’s cash and our yard inventory; underestimating causes costly backorders and emergency deliveries. A consistent counting method keeps Ritter Lumber competitive and reliable.

### Key Concepts
- **Stud Types:** Common studs, king studs, jack (trimmer) studs, cripple studs (above/below openings), and blocking pieces all serve specific roles.
- **Plates:** Bottom plates (treated on slab), single top plates, and double top plates tie the walls together. Linear footage is based on wall length plus laps at corners.
- **Headers:** Built-up members sized per span and load; often listed in structural notes (e.g., “(2) 2x10 for 3'-0" opening”). Record counts by size.
- **Corners & Intersections:** Add studs for California corners or ladder blocks; note what detail the plan calls out.

### Diagram Reference
![Wall framing components](img/wall-framing-section.svg)
The diagram shows a section of exterior wall with labeled components: bottom plate on slab, double top plate, common studs at 16" O.C., a window opening with king studs, jack studs supporting a double 2x10 header, cripple studs above the header, and blocking at mid-height. Use it to visualize how many pieces each opening requires.

### Step-by-Step Takeoff Process
1. **List Wall Segments:** Create a table with wall ID, length, height, and stud spacing. Include bearing vs non-bearing distinction if spacing or members change.
2. **Calculate Common Studs:** Use `number of studs = (wall length / spacing) + 1`. Round up to the next whole stud.
3. **Adjust for Corners & Intersections:** Add studs per detail (typically +2 per exterior corner, +1 per tee intersection for ladder blocking).
4. **Account for Openings:** Subtract the studs displaced by the opening width, but add king and jack studs per side plus cripples as required.
5. **Take Off Plates:** Bottom and double top plates use the same wall length. Multiply total wall length by number of plates (usually three runs) and convert to board feet/linear feet. Remember treated plate requirements against slab.
6. **Count Headers:** For each opening, record width, required header size, and quantity. If the structural schedule specifies engineered lumber (LVL, PSL), note that substitution when pricing.
7. **Record Blocking:** Fire blocking, horizontal shear panels, and backing for cabinets/handrails must be estimated. Use linear footage or count per bay as specified.

### Worked Example: 24' x 36' Rectangle with Openings
- **Inputs:** Exterior walls 2x6 @ 16" O.C., walls are 8'-0" tall. Front wall (36') has one 3'-0" entry door (`D1`) and two 3050 windows (`W2`). Side walls (24') each have one 3050 window.
- **Common Studs:** Perimeter length 120'. Stud count before adjustments 94. After opening adjustments and corner additions, total 110 studs.
- **Plates:** Total wall length 120'. Bottom plate 120' (treated). Double top plates 240'. Combined 360'; add 10% waste = 396'. Convert to board count (16' boards) ≈ 25; round up to 26 for waste.
- **Headers:** Entry door (2) 2x10, windows (2) 2x8 or (2) 2x10 per schedule. Document individually.

### Tips & Common Mistakes
- **Tip:** Use a spreadsheet template with formulas for stud spacing and plate counts to reduce math errors.
- **Tip:** Note wall heights above 8'-0". Taller walls increase stud length options (10', 12') and affect pricing.
- **Mistake:** Forgetting to add extra studs for partition tee intersections; without them, drywall backing is missing on site.
- **Mistake:** Double-counting treated bottom plates on interior bearing walls that sit on slabs—confirm whether they require treated lumber.

### Recap
You now have a repeatable process for calculating studs, plates, and headers while accounting for corners and openings. In the next chapter you will apply similar rigor to roof framing.

---

## Chapter 5 · Roof Takeoff
### Why Roof Measurements Differ from Floor Area
Roof surface area depends on slope and geometry, not just the building footprint. A quick count based on plan rectangles misses extra surface at hips, valleys, and overhangs, leading to material shortages. This chapter shows how to convert plan data into accurate decking, underlayment, and shingles.

### Key Concepts
- **Roof Geometry:** Ridges run horizontally across peak lines, hips project outward where roof planes meet, valleys run inward where planes intersect, and eaves are the lower edges with overhangs.
- **Slope vs Pitch:** Slope uses rise over run (e.g., 6" rise per 12" run). Pitch compares rise to span (e.g., 6:12 pitch equals 6:24 slope). Use slope when applying conversion factors.
- **Slope Factor:** Multiply the horizontal (plan) length by `√(rise² + run²) / run` to get roof surface length.
- **Squares & Bundles:** 1 roofing square = 100 sq ft. Asphalt shingles typically use 3 bundles per square.
- **Decking Sheets:** Standard 4'x8' OSB/plywood covers 32 sq ft. Add waste for angled cuts.

### Diagram Reference
![Roof plan and section](img/roof-plan-and-section.svg)
The diagram pairs a plan view of a simple gable roof showing ridge line, eave overhangs, and dimension strings with a section demonstrating a 6:12 slope triangle and the resulting slope factor. Valleys and hips are labeled on secondary planes to reinforce terminology.

### Step-by-Step Roof Takeoff
1. Identify roof plan sheets and slope callouts.
2. Measure horizontal areas including overhangs.
3. Apply slope factor to each plane.
4. Add waste for hips/valleys.
5. Calculate decking sheets (area ÷ 32) and add waste.
6. Convert to squares and bundles.
7. Record accessory items (ridge, drip edge, underlayment).

### Worked Example
- Footprint 24' × 36' with 1' eaves → 26' × 38' horizontal.
- Horizontal area = 988 sq ft. Slope factor 1.118.
- Surface area = 1,104 sq ft. Waste 10% ⇒ 1,214 sq ft.
- Decking sheets = 38. Shingle squares = 13 (rounded). Ridge vent 40', drip edge 135', underlayment 2 rolls.

### Tips & Common Mistakes
- **Tip:** Create a slope factor cheat sheet and tape it to your monitor for quick reference.
- **Tip:** For hips and valleys, count linear footage separately for ridge/hip cap accessories and metal valley flashing.
- **Mistake:** Forgetting to include porch roofs or garage wings with different slopes—handle each plane independently.
- **Mistake:** Using plan area without overhangs; decking and shingles extend to the eave edge, not the wall line.

### Recap
You can now translate plan geometry and slope notes into accurate roof surface areas, decking sheet counts, and shingle bundles. This ensures the framing lumber takeoff you performed feeds cleanly into the roof package.

---

## Chapter 6 · Elevations & Siding
### Why Elevations Matter
Elevations reveal vertical dimensions, cladding transitions, trim details, and special façade treatments that floor plans cannot show. Accurate siding takeoffs require understanding every wall face, gable height, and opening deduction.

### Key Concepts
- **Elevation Sheets:** Usually labeled `A4.x`. Each sheet shows front, rear, and side views with grade lines, finished floor elevations, ridge heights, and siding callouts.
- **Wall vs Gable Areas:** Wall area = width × height (plate to grade). Gable area = (base × height) / 2.
- **Siding Squares:** 1 square = 100 sq ft.
- **Openings Deduction:** Subtract the area of doors and windows; add back trim boards separately.
- **Waste Factors:** 7–10% for vinyl, higher for complex elevations.

### Diagram Reference
![Elevation siding areas](img/elevation-siding-areas.svg)
The diagram shows a front elevation with labeled width (36'), plate height (8'), gable peak height (4'), window/door dimensions, and shaded regions identifying rectangular wall areas and triangular gable areas. Break lines indicate where to subtract openings and add trim.

### Step-by-Step Siding Takeoff
1. Capture elevation dimensions.
2. Calculate rectangular wall areas.
3. Calculate gable areas.
4. Subtract openings.
5. Add waste percentage.
6. Convert to squares and record trim accessories.

### Worked Example
- Wall area 36' × 8' = 288 sq ft. Gable area = 32 sq ft.
- Openings total 50 sq ft.
- Net area = 270 sq ft. Waste 10% ⇒ 297 sq ft ⇒ 3.0 squares.
- Trim: corner posts, J-channel perimeters, starter strip along base.

### Tips & Common Mistakes
- **Tip:** Create a façade worksheet listing each elevation to keep deductions organized.
- **Tip:** When siding changes at different heights, split the calculation into zones and note transition trims.
- **Mistake:** Forgetting gable ventilation openings.
- **Mistake:** Applying the same waste to board-and-batten as to lap siding.

### Recap
You can now translate elevation dimensions into siding squares with proper deductions and waste. The next chapter extends these measurement skills to foundation and concrete work.

---

## Chapter 7 · Foundation & Concrete
### Why Concrete Quantities Need Precision
Concrete is expensive to mobilize and unforgiving if under-ordered. Accurate yardage protects the builder from cold joints and keeps Ritter Lumber’s reputation strong. This chapter covers slab-on-grade basics, volume formulas, and rebar takeoffs.

### Key Concepts
- Slab components, volume formulas, pier calculations, and rebar spacing requirements.
- Waste factors: 5% for slabs, 10% for footings/piers.

### Diagram Reference
![Foundation plan and section](img/foundation-plan-section.svg)
The diagram shows a foundation plan with a 24' × 36' slab, 12" perimeter footing, interior beam, and pier callouts, plus a section showing slab thickness, thickened edge dimensions, vapor barrier, and rebar placement.

### Step-by-Step Foundation Takeoff
1. Confirm structural notes (thickness, strength, reinforcement).
2. Calculate slab volume.
3. Calculate footings and beams.
4. Calculate pier volumes.
5. Convert totals to cubic yards and apply waste.
6. Determine rebar linear footage for each element.

### Worked Example: 20' × 24' Garage
- Slab volume = 160 cu ft.
- Perimeter footing = 132 cu ft.
- Interior beam = 36 cu ft.
- Piers = 6.28 cu ft.
- Total = 334.28 cu ft = 12.38 yd³. Waste 5% ⇒ order 13 yd³.
- Rebar totals recorded per component.

### Tips & Common Mistakes
- **Tip:** When plans lack footing dimensions, use code minimums and document assumptions.
- **Tip:** Include vapor barrier, expansion joint, and anchor bolt notes.
- **Mistake:** Forgetting to convert inches to feet before multiplying volumes.
- **Mistake:** Ignoring step footings on sloped lots.

### Recap
You can now calculate slab, footing, beam, and pier volumes, convert them to cubic yards, and determine rebar lengths. These skills feed into the full example house takeoff later in the manual.

---

## Chapter 8 · Window & Door Schedules
### Why Schedules Are Critical
Floor plans show where openings go, but schedules specify exact sizes, types, and remarks that determine framing requirements and material pricing. Reading schedules accurately prevents wrong-size units and job-site reorders.

### Key Concepts
- Tags match plan callouts.
- Schedule columns include size, type, operation, rough opening, remarks.
- Rough openings typically add 1/2" to window dimensions, 2" width and 2-1/2" height to doors.

### Diagram Reference
![Window and door schedule sample](img/window-door-schedule.svg)
The diagram shows a cropped schedule with columns for Tag, Quantity, Size, Type, Operation, RO, Remarks, plus plan callouts pointing from a floor plan window label (`W3`). It highlights how a double door references sidelights.

### Step-by-Step Schedule Process
1. Locate the schedule sheet.
2. Verify tags between plan and schedule.
3. Record framing needs per unit.
4. Group similar units for ordering.
5. Check remarks for tempered/egress requirements.
6. Document delivery or installation notes.

### Example Mini Schedule & Framing Impact
| Tag | Qty | Size (WxH) | Type | Operation | Rough Opening | Remarks |
| --- | --- | --- | --- | --- | --- | --- |
| W1 | 4 | 3040 | Vinyl single-hung | XO | 3'-0 1/2" × 4'-0 1/2" | Tempered @ Bath |
| W2 | 2 | 3050 | Vinyl picture | Fixed | 3'-0 1/2" × 5'-0 1/2" | Align heads |
| D1 | 1 | 3068 | Fiberglass entry | Inswing | 3'-2" × 6'-10 1/2" | Sidelight framing |
| D2 | 2 | 2068 | Interior hollow-core | Swing | 2'-2" × 6'-10 1/2" | Pocket kit in Bed 2 |

### Tips & Common Mistakes
- **Tip:** Create a spreadsheet filtered by tag to check that plan counts equal schedule counts.
- **Tip:** Use remarks to plan for additional trim packages or specialty hardware.
- **Mistake:** Ignoring rough opening callouts and framing walls to nominal sizes.
- **Mistake:** Missing tempered-glass requirements near doors or wet areas.

### Recap
You can now match plan tags to schedule data, determine rough openings, and capture framing adjustments. These skills ensure the framing counts from Chapter 4 align with the actual units ordered.

---

## Chapter 9 · Material Conversion Tables
Use these quick-reference tables while performing takeoffs or checking your math. They consolidate the most common conversions used by Ritter Lumber salespeople.

### Stud Counts per Linear Foot
| Stud Spacing | Studs per 10' | Studs per 100' | Formula |
| --- | --- | --- | --- |
| 16" O.C. | 8 | 75 | `(length in inches / 16) + 1` |
| 19.2" O.C. | 6 | 62 | `(length in inches / 19.2) + 1` |
| 24" O.C. | 5 | 50 | `(length in inches / 24) + 1` |

### Plate Boards per Linear Foot
| Total Wall Length (ft) | LF of Plates (×3) | 16' Boards (no waste) | Recommended Boards (+10%) |
| --- | --- | --- | --- |
| 40 | 120 | 7.5 | 9 |
| 80 | 240 | 15 | 17 |
| 120 | 360 | 22.5 | 25 |
| 160 | 480 | 30 | 33 |

### Siding Conversions
| Item | Conversion |
| --- | --- |
| Square feet to siding squares | `sq ft ÷ 100` |
| Starter strip | Perimeter of walls to be sided |
| Corner posts | Count corners × wall height |
| J-channel around openings | `(2 × width) + (2 × height)` per opening |
| Waste factor (vinyl/lap siding) | 10% simple, 12–15% complex |

### Roofing Conversions
| Item | Conversion |
| --- | --- |
| Square feet to squares | `sq ft ÷ 100` |
| Squares to bundles (3-tab/asphalt) | `squares × 3` |
| Underlayment rolls (synthetic) | `squares ÷ 10` (check manufacturer) |
| Ridge/hip cap | `ridge + hip LF + 10%` |
| Starter strip | Perimeter of eaves |

### Decking (4' × 8' Sheets)
| Roof or Floor Area (sq ft) | Sheets @ 32 sq ft | Sheets +10% Waste |
| --- | --- | --- |
| 640 | 20 | 22 |
| 960 | 30 | 33 |
| 1,280 | 40 | 44 |
| 1,600 | 50 | 55 |

Formula: `Sheets = (Area ÷ 32) × 1.10` (round up).

### Concrete Conversions
| Item | Conversion |
| --- | --- |
| Cubic feet to cubic yards | `cu ft ÷ 27` |
| 80-lb bags per cubic yard | `27 cu ft × (1 bag / 0.6 cu ft) ≈ 45 bags` |
| 60-lb bags per cubic yard | `27 ÷ 0.45 ≈ 60 bags` |

### Typical Waste Factors
| Category | Recommended Waste |
| --- | --- |
| Stud framing | 5% (cutting, damaged pieces) |
| Plates & blocking | 5% |
| Roof decking | 10% |
| Shingles | 10% simple roofs, 12% complex |
| Siding | 10% vinyl/lap, 12% board-and-batten |
| Concrete | 5% slabs, 10% footings/piers |

### Quick Reference Formulas
- **Slope Factor:** `√(rise² + run²) / run`. Common slopes: 4:12=1.054, 5:12=1.083, 6:12=1.118, 8:12=1.202.
- **Gable Area:** `(base × height) / 2`.
- **Stud Count:** `(wall length in inches / spacing) + 1 + corner/intersection extras`.
- **Header Stock:** `number of openings × header length × members per header`.

---

## Chapter 10 · Full Example House Takeoff
This chapter demonstrates a complete takeoff for a representative Ritter Lumber project. Follow each step, replicate the math, and note how every chapter connects.

### Project Description
- **Footprint:** 24' (width) × 36' (length)
- **Walls:** 8'-0" tall, exterior 2x6 @ 16" O.C., interior 2x4 @ 16" O.C.
- **Roof:** Simple gable, 6:12 slope, 1'-0" eaves.
- **Openings:**
	- Windows: (4) 3040 single-hung (W1), (2) 3050 picture (W2)
	- Doors: (1) 3068 entry (D1), (2) 2068 interior (D2), (1) 6068 patio slider (D3)
- **Foundation:** 4" slab on grade with 12" × 18" perimeter footing and one 12" × 18" interior beam along the 36' axis.
- **Finishes:** Vinyl siding, asphalt shingles, standard aluminum soffit/fascia.

### 1. Wall Framing
**Studs**
- Perimeter = 2×(24 + 36) = 120'.
- Convert to inches: 120' × 12 = 1,440".
- Stud count @ 16" O.C.: (1,440 ÷ 16) + 1 = 90 + 1 = 91 studs.
- Corner/tee additions: 4 corners ×2 extra + 4 interior tee intersections ×1 = 12 studs.
- Opening adjustments:
	- Entry door (3'): subtract 2 studs, add 2 king + 2 jack + 3 cripples = +5.
	- Patio slider (6'): subtract 4 studs, add 2 king + 2 jack + 4 cripples = +4.
	- Windows (4 × 3' + 2 × 5'): subtract (4×2 + 2×3) = 14 studs, add (6 openings ×4 studs) = +24.
- Total exterior studs = 91 + 12 - 20 + 33 = 116 studs.
- Add 5% waste ⇒ 122 studs (round to 125 for bundle ordering).

**Plates**
- Wall length 120'. Bottom plate = 120' (treated). Double top plate = 240'. Total = 360'. Add 10% waste ⇒ 396'. Using 16' boards: 396' ÷ 16' ≈ 25 boards. Order 26 treated for bottom plates, 52 SPF for top plates.

**Headers**
- Entry door: (2) 2x10 @ 3' span.
- Patio door: (2) 2x12 @ 6' span per structural note.
- W1 windows: (2) 2x8 @ 3' span (×4 units).
- W2 windows: (2) 2x10 @ 5' span (×2 units).
- Record each in the header schedule for pricing.

### 2. Roof Materials
**Surface Area**
- Horizontal dimensions include eaves: 26' × 38' = 988 sq ft.
- Slope factor (6:12) = 1.118. Surface area = 988 × 1.118 = 1,104 sq ft.
- Waste 10% ⇒ 1,214 sq ft.

**Decking**
- Sheets = 1,214 ÷ 32 = 37.9 ⇒ order 38 sheets (7/16" OSB) + 2 extra for porch tie-ins.

**Shingles**
- Squares = 1,214 ÷ 100 = 12.14 ⇒ order 13 squares (39 bundles).
- Ridge cap: ridge length 36' + 10% = 40'. Hip/valley length = 0 (simple gable). Starter/drip edge = perimeter (128') + 5% = 135'.
- Underlayment: synthetic roll covering 10 squares ⇒ 2 rolls.

### 3. Siding & Trim
**Area Calculation**
- Long walls: 36' × 8' = 288 sq ft each ⇒ 576 sq ft total.
- Short walls: 24' × 8' = 192 sq ft each ⇒ 384 sq ft total.
- Gables: each 24' base, rise from 6:12 slope over 12' run ⇒ 6'. Gable area = (24 × 6)/2 = 72 sq ft (×2) = 144 sq ft.
- Gross area = 576 + 384 + 144 = 1,104 sq ft.
- Openings area: entry door 20 sq ft, patio door 40 sq ft, windows (4 × 12 sq ft + 2 × 15 sq ft) = 78 sq ft ⇒ total 138 sq ft.
- Net area = 1,104 - 138 = 966 sq ft. Waste 10% ⇒ 1,063 sq ft.
- Squares = 1,063 ÷ 100 = 10.63 ⇒ order 11 squares vinyl siding.

**Trim & Accessories**
- Corner posts: 4 corners × 8' = 32' (order 40').
- Starter strip: wall perimeter 120'.
- J-channel around openings: sum perimeters ≈ 170'. Add 10% ⇒ 187'.
- Soffit/fascia: eave length 2×36' = 72'; rake length using slope factor: 13' sloped length × 4 sides = 52'. Total fascia = 124'.

### 4. Foundation & Concrete
- Slab area = 24' × 36' = 864 sq ft. Volume = 864 × 0.333' = 288 cu ft.
- Perimeter footing: perimeter 120', width 1', depth 1.5' ⇒ 180 cu ft.
- Interior beam along 36': width 1', depth 1.5' ⇒ 54 cu ft.
- Total = 522 cu ft ÷ 27 = 19.33 yd³. Waste 5% ⇒ 20.3 yd³ ⇒ order 21 yd³.

**Rebar**
- Perimeter footing: two #4 bars ⇒ 120' × 2 = 240', +10% = 264'.
- Interior beam: two #4 bars ⇒ 36' × 2 = 72', +10% = 79'.
- Slab mat: #3 @ 18" each way over 864 sq ft ⇒ (24'/1.5' = 16 runs × 36' = 576') + (36'/1.5' = 24 runs × 24' = 576') = 1,152', +10% = 1,267'.

### 5. Windows & Doors
| Tag | Qty | Size | RO | Notes |
| --- | --- | --- | --- | --- |
| W1 | 4 | 3040 | 3'-0 1/2" × 4'-0 1/2" | Tempered near tub at Bath 2 |
| W2 | 2 | 3050 | 3'-0 1/2" × 5'-0 1/2" | Align heads with W1 |
| D1 | 1 | 3068 | 3'-2" × 6'-10 1/2" | Fiberglass entry, includes sidelight framing |
| D2 | 2 | 2068 | 2'-2" × 6'-10 1/2" | Hollow-core swing |
| D3 | 1 | 6068 | 6'-2" × 6'-10 1/2" | Vinyl slider, tempered glass |

Frame walls per Chapter 8 guidance. Ensure header sizes match structural schedule.

### Summary Table
| Material Group | Quantity | Notes |
| --- | --- | --- |
| Exterior studs | 125 pcs (2x6x104 5/8) | Includes 5% waste |
| Plates | 26 treated 2x6x16 (bottom), 52 SPF 2x6x16 (top) | Lap corners |
| Headers | (1) (2)2x10@3', (1) (2)2x12@6', (4) (2)2x8@3', (2) (2)2x10@5' | Precut or LVL as specified |
| Roof decking | 40 sheets 7/16" OSB | Includes 5% contingency |
| Shingles | 13 squares (39 bundles) | Add ridge/starter accessories |
| Underlayment | 2 rolls synthetic | 10-square coverage each |
| Siding | 11 squares vinyl | 40' corners, 187' J-channel |
| Concrete | 21 yd³ | Includes slab, footing, beam waste |
| Rebar #4 | 343' (perimeter + beam) | Order in 20' sticks |
| Rebar #3 | 1,267' | Slab mat |
| Windows | 6 units | Tags W1, W2 |
| Exterior doors | 2 units | D1 entry, D3 slider |
| Interior doors | 2 units | D2 |

### Recap
This example connects every skill from the manual. Practice by recreating the calculations in a spreadsheet, then apply the workflow to a current customer project to cement the process.

---

## Chapter 11 · Master Worksheets
Print these worksheets (8.5" × 11" portrait) or duplicate them in your spreadsheet software. They capture every decision you make during a takeoff so another salesperson—or the builder—can audit the work.

### Wall & Framing Worksheet
| Wall ID | Location | Length (ft) | Height (ft) | Stud Spacing | Base Stud Count | Corner/Intersection Adds | Opening Adjustments | Total Studs | Bottom Plate LF | Top Plate LF | Header Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | | | |
| | | | | | | | | | | | |
| | | | | | | | | | | | |

### Roof Worksheet
| Roof Plane | Dimensions (L × W) | Slope | Horizontal Area (sq ft) | Slope Factor | Surface Area (sq ft) | Decking Sheets | Squares | Bundles | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | |
| | | | | | | | | | |

### Siding & Elevations Worksheet
| Elevation | Width (ft) | Plate Height (ft) | Gable Rise (ft) | Gross Area (sq ft) | Opening Deductions (sq ft) | Net Area (sq ft) | Waste % | Order Area (sq ft) | Squares | Trim/J-Channel Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| | | | | | | | | | | |
| | | | | | | | | | | |

### Foundation Worksheet
| Pour Segment | Dimensions (L × W × T) | Volume (cu ft) | Volume (cu yd) | Rebar Size & Spacing | Linear Feet of Rebar | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Slab | | | | | | |
| Perimeter Footing | | | | | | |
| Interior Beam | | | | | | |
| Piers | Diameter × Depth: | | | | | |

### Windows & Doors Worksheet
| Tag | Qty | Size (WxH) | Rough Opening | Header Size | Remarks (tempered, egress, grids) | Notes to Yard/Installer |
| --- | --- | --- | --- | --- | --- | --- |
| | | | | | | |
| | | | | | | |

### Material Conversion & Waste Planning
| Category | Base Quantity | Conversion Applied | Waste % | Order Quantity | Supplier Lead Time | Follow-Up Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Studs | | | | | | |
| Plates | | | | | | |
| Roof Decking | | | | | | |
| Shingles | | | | | | |
| Siding | | | | | | |
| Concrete | | | | | | |

### Usage Tips
- Fill out one worksheet per job and store the PDF in the CRM for auditing.
- Initial and date each section when complete; this proves the takeoff was reviewed.
- Attach product cut sheets or engineering letters referenced in the notes column.

These worksheets complete the manual and provide a repeatable documentation system for every takeoff.

