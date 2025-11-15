# Chapter 7 · Foundation & Concrete

## Why Concrete Quantities Need Precision
Concrete is expensive to mobilize and unforgiving if under-ordered. Accurate yardage protects the builder from cold joints and keeps Ritter Lumber’s reputation strong. This chapter covers slab-on-grade basics, volume formulas, and rebar takeoffs.

## Key Concepts
- **Slab Components:** Slab thickness (commonly 4"), thickened edge or perimeter footing, interior turn-down beams, and isolated piers.
- **Volume Formula:** `Volume (cu ft) = Length × Width × Thickness`. Convert to cubic yards by dividing by 27.
- **Piers:** Use `π × (diameter/2)^2 × depth` for cylindrical piers. Always convert diameter to feet.
- **Rebar Takeoff:** Determine spacing (e.g., #4 @ 12" O.C.) and multiply run lengths to get linear feet.
- **Waste Factors:** Add 5% for slab pours and 10% for footings/piers to account for spillage and pump priming.

## Diagram Reference
![Foundation plan and section](img/foundation-plan-section.svg)
The diagram shows a foundation plan with a 24' × 36' slab, 12" perimeter footing, interior beam running the long direction, and callouts for pier locations. A section illustrates slab thickness, thickened edge dimensions, vapor barrier, and rebar placement.

## Step-by-Step Foundation Takeoff
1. **Confirm Structural Notes:** Check slab thickness, footing widths, reinforcement schedules, and compressive strength (e.g., 3,500 psi). These notes override general assumptions.
2. **Calculate Slab Volume:** Convert thickness to feet (4" = 0.333'). Multiply by slab area.
3. **Calculate Footing Volume:** Multiply perimeter length by footing width and depth. Include steps or grade beams separately.
4. **Interior Beams:** Multiply beam length by width and depth.
5. **Piers:** For each pier, compute volume using the cylinder formula. Sum the volumes.
6. **Convert to Cubic Yards:** Add all cubic feet and divide by 27. Apply waste factor.
7. **Rebar Quantities:** Measure runs for perimeter #4 bars (usually two continuous bars), interior beams, and slab mats. Use spacing to convert area coverage into linear footage.

## Worked Example: Garage Slab
- **Design:** 20' × 24' slab, 4" thick. Perimeter footing 12" wide × 18" deep. One interior beam running along the 24' dimension, 12" wide × 18" deep. Four 12" diameter piers at corners, 24" deep.

### Slab Volume
- Area = 20' × 24' = 480 sq ft. Thickness = 0.333'. Volume = 480 × 0.333 = 160 cu ft.

### Perimeter Footing
- Perimeter = 2×(20 + 24) = 88'. Volume = 88' × 1' × 1.5' = 132 cu ft.

### Interior Beam
- Length = 24'. Volume = 24' × 1' × 1.5' = 36 cu ft.

### Piers
- Each pier volume = π × (1'/2)^2 × 2' = 3.14 × 0.25 × 2 = 1.57 cu ft. Four piers = 6.28 cu ft.

### Total Volume
- Sum = 160 + 132 + 36 + 6.28 = 334.28 cu ft.
- Cubic yards = 334.28 / 27 ≈ 12.38 yd³.
- Waste (5%) = 0.62 yd³. Order 13.0 yd³.

### Rebar
- Perimeter footing: two #4 bars continuous ⇒ 88' × 2 = 176'. Add 10% lap/waste = 194'.
- Interior beam: two bars ⇒ 24' × 2 = 48', +10% = 53'.
- Slab mat: #3 @ 18" each way over 480 sq ft ⇒ 20' span/1.5' spacing ≈ 13 runs × 24' = 312'; perpendicular direction: 16 runs × 20' = 320'. Total ≈ 632', +10% = 695'.

Document each component separately so drivers know pour sequence.

## Tips & Common Mistakes
- **Tip:** When plans lack footing dimensions, use building code minimums (e.g., 12" wide × 12" deep) but flag the assumption in your worksheet.
- **Tip:** Include vapor barrier, expansion joint, and anchor bolt spacing notes while you are on the foundation sheets.
- **Mistake:** Forgetting to convert inches to feet before multiplying volumes. Always check units.
- **Mistake:** Ignoring step footings on sloped lots; these increase concrete volume and labor.

## Recap
You can now calculate slab, footing, beam, and pier volumes, convert them to cubic yards, and determine rebar lengths. These skills feed into the full example house takeoff later in the manual.