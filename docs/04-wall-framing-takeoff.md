# Chapter 4 · Wall & Framing Takeoff

## Why Accurate Framing Counts Matter
Framing lumber is usually the largest material cost on a residential project. Overestimating ties up the builder’s cash and our yard inventory; underestimating causes costly backorders and emergency deliveries. A consistent counting method keeps Ritter Lumber competitive and reliable.

## Key Concepts
- **Stud Types:** Common studs, king studs, jack (trimmer) studs, cripple studs (above/below openings), and blocking pieces all serve specific roles.
- **Plates:** Bottom plates (treated on slab), single top plates, and double top plates tie the walls together. Linear footage is based on wall length plus laps at corners.
- **Headers:** Built-up members sized per span and load; often listed in structural notes (e.g., “(2) 2x10 for 3'-0" opening”). Record counts by size.
- **Corners & Intersections:** Add studs for California corners or ladder blocks; note what detail the plan calls out.

## Diagram Reference
![Wall framing components](img/wall-framing-section.svg)
The diagram shows a section of exterior wall with labeled components: bottom plate on slab, double top plate, common studs at 16" O.C., a window opening with king studs, jack studs supporting a double 2x10 header, cripple studs above the header, and blocking at mid-height. Use it to visualize how many pieces each opening requires.

## Step-by-Step Takeoff Process
1. **List Wall Segments:** Create a table with wall ID, length, height, and stud spacing. Include bearing vs non-bearing distinction if spacing or members change.
2. **Calculate Common Studs:** Use `number of studs = (wall length / spacing) + 1`. Round up to the next whole stud. Example: 16'-3" wall @ 16" O.C. ⇒ 195"/16" = 12.19 ⇒ 13 studs.
3. **Adjust for Corners & Intersections:** Add studs per detail (typically +2 per exterior corner, +1 per tee intersection for ladder blocking).
4. **Account for Openings:** Subtract the studs displaced by the opening width, but add king and jack studs per side plus cripples as required.
5. **Take Off Plates:** Bottom and double top plates use the same wall length. Multiply total wall length by number of plates (usually three runs) and convert to board feet/linear feet. Remember treated plate requirements against slab.
6. **Count Headers:** For each opening, record width, required header size, and quantity. If the structural schedule specifies engineered lumber (LVL, PSL), note that substitution when pricing.
7. **Record Blocking:** Fire blocking, horizontal shear panels, and backing for cabinets/handrails must be estimated. Use linear footage or count per bay as specified.

## Worked Example: 24' x 36' Rectangle with Openings
- **Inputs:** Exterior walls 2x6 @ 16" O.C., walls are 8'-0" tall. Front wall (36') has one 3'-0" entry door (`D1`) and two 3050 windows (`W2`). Side walls (24') each have one 3050 window.

### Common Studs
- Perimeter length = 2×36' + 2×24' = 120'.
- Stud count per wall:
  - 36' wall: (432"/16") + 1 = 27 + 1 = 28 studs.
  - 24' wall: (288"/16") + 1 = 18 + 1 = 19 studs.
- Total before adjustments: 2×28 + 2×19 = 94 studs.

### Openings Adjustments
- Entry door: opening width 3' ⇒ remove (3'/1.333') ≈ 2 studs, but add 2 king + 2 jack + 3 cripple = net +5 studs.
- Each 3050 window: width 3' ⇒ remove ≈2 studs, add 2 king + 2 jack + 2 cripple = +4 studs each.
- After four windows: base 94 - (4×2) + (4×4) = 94 - 8 + 16 = 102 studs.
- Add corner studs: assume 3-stud corners ⇒ +2 studs per corner beyond existing studs: 4 corners ×2 = +8. Adjusted total = 110 studs.

### Plates
- Total wall length 120'. For bottom plate: 120' (treated). For double top plate: 2 × 120' = 240'. Combined linear footage = 360'. Add 10% waste ⇒ 396'. Convert to board count (assuming 16' boards): 396'/16' ≈ 25 boards (round to 26 for waste).

### Headers
- Entry door: structural note calls for (2) 2x10. Record 1 header set.
- Windows: (2) 2x8 for each 3' span per schedule. Record 4 header sets.

Document these results in your worksheet before moving to the next wall section.

## Tips & Common Mistakes
- **Tip:** Use a spreadsheet template with formulas for stud spacing and plate counts to reduce math errors.
- **Tip:** Note wall heights above 8'-0". Taller walls increase stud length options (10', 12') and affect pricing.
- **Mistake:** Forgetting to add extra studs for partition tee intersections; without them, drywall backing is missing on site.
- **Mistake:** Double-counting treated bottom plates on interior bearing walls that sit on slabs—confirm whether they require treated lumber.

## Recap
You now have a repeatable process for calculating studs, plates, and headers while accounting for corners and openings. In the next chapter you will apply similar rigor to roof framing.