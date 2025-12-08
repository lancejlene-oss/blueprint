# Blueprint Takeoff Workbook - Release Notes

## Version 1.0 - December 2025

### Overview
Complete professional training system for teaching residential blueprint takeoffs to lumberyard salespeople. This release includes comprehensive documentation, interactive Excel templates, technical diagrams, and trainer resources.

---

## Contents

### Documentation (`/docs/`)

#### Core Training Manual
- **Blueprint-Takeoff-Manual.md** - Complete combined training manual (610 lines)
  - All 11 chapters in single print-ready document
  - Suitable for PDF export via Pandoc

#### Individual Chapters
1. **01-introduction.md** - Manual overview and learning objectives
2. **02-blueprint-orientation.md** - Reading plan sets, title blocks, scales
3. **03-floor-plan-reading.md** - Walls, openings, dimensions, symbols
4. **04-wall-framing-takeoff.md** - Studs, plates, headers, calculations
5. **05-roof-takeoff.md** - Slope factors, sheathing, shingles
6. **06-elevations-and-siding.md** - Exterior materials and trim
7. **07-foundation-and-concrete.md** - Slabs, footings, rebar, volume calculations
8. **08-window-and-door-schedules.md** - Reading schedules, rough openings
9. **09-material-conversion-tables.md** - Quick reference multipliers and factors
10. **10-full-example-house-takeoff.md** - Step-by-step complete example
11. **11-master-worksheets.md** - Printable takeoff templates

#### Technical Diagrams (`/docs/img/`)
All diagrams are production-quality SVG files suitable for print and web:

- **plan-orientation.svg** - Blueprint sheet navigation (title block, north arrow, scale bar, legend, revision clouds)
- **floor-plan-basic.svg** - Floor plan elements (walls, doors, windows, dimensions, room labels)
- **wall-framing-section.svg** - Detailed wall assembly (studs, plates, headers, blocking, sheathing)
- **roof-plan-and-section.svg** - Roof geometry (plan view, section, pitch diagram, slope calculations)
- **elevation-siding-areas.svg** - Siding calculation example (area breakdown, openings, waste factors)
- **foundation-plan-section.svg** - Foundation details (slab, footings, piers, rebar placement)
- **window-door-schedule.svg** - Schedule coordination (table format and plan callouts)

### Interactive Tools (`/templates/`)

#### Excel Workbook (worksheet.xlsx)
Comprehensive multi-sheet workbook with automatic calculations:

**Worksheets:**
1. **Project Info** - Project details and building specifications
   - Regional notes for Southeast Texas (slab foundations, humidity, windstorm requirements)
   
2. **Wall Framing** - Stud and plate calculators
   - Automatic stud count formulas: `(Length ÷ Spacing) + 1`
   - Corner and intersection adjustments
   - Opening calculations
   - Bottom plate and top plate linear footage
   
3. **Roof Takeoff** - Roof material estimator
   - Slope factor reference table (4:12 through 12:12 pitch)
   - Horizontal to surface area conversion
   - Sheathing sheet calculations (÷32 SF per sheet)
   - Shingle bundle estimates
   - Waste factor application
   
4. **Foundation** - Concrete volume calculator
   - Slab calculations with thickness conversion
   - Perimeter footing volumes (CF to CY)
   - Rebar linear footage
   - SE Texas specific notes (treated plates requirement)
   
5. **Siding & Exterior** - Exterior materials
   - Wall area calculations
   - Gable triangle formulas
   - Opening deductions
   - Waste percentage application
   - Trim and accessory tracking
   
6. **Windows & Doors** - Opening schedule
   - Tag-based organization
   - Rough opening specifications
   - Header size tracking
   - Quantity and pricing columns
   
7. **Material Summary** - Quote-ready export
   - Consolidated material list by category
   - Unit pricing and extended totals
   - Links to other worksheets
   - Professional presentation format
   
8. **Conversion Tables** - Quick reference
   - Stud spacing multipliers
   - Roof slope factors with degrees
   - Board feet conversions
   - Area and volume conversions
   - Typical waste factors by material

**Key Features:**
- All formulas pre-loaded and tested
- Print-ready page layouts
- Color-coded sections for easy navigation
- Documentation prompts throughout
- Southeast Texas regional considerations integrated

### Training Resources (`/training/`)

#### Trainer-Guide.md
Complete instructor's manual for teaching blueprint takeoff:

**Topics Covered:**
- 6-week training program structure
- Day-by-day lesson plans
- Module-by-module teaching tips
- Competency tests with passing criteria
- Example homework assignments
- Evaluation checklists and rubrics
- Group training session formats
- Common training challenges and solutions
- Resource recommendations

**Assessment Tools:**
- Test 1: Blueprint Reading (Week 1, 30 min, 80% pass)
- Test 2: Wall Framing (Week 2, 45 min, 85% pass)
- Test 3: Roof & Foundation (Week 3, 60 min, 85% pass)
- Test 4: Full Takeoff Competency (Week 6, 4 hours, 90% pass)

### Automation Scripts (`/scripts/`)

#### create_excel_template.py
Python script to generate the Excel workbook from scratch:
- Uses openpyxl library
- Creates all 8 worksheets
- Applies formatting and formulas
- Can be modified for customization
- Regenerate template with: `python3 scripts/create_excel_template.py`

### Build Automation (`/.github/workflows/`)

#### build-manual.yml
GitHub Actions workflow for PDF generation:
- Triggers on changes to docs/ or README
- Installs Pandoc and LaTeX (XeLaTeX)
- Generates PDF from Blueprint-Takeoff-Manual.md
- Uploads artifact: Blueprint-Takeoff-Training-Manual.pdf
- Can be triggered manually from Actions tab

---

## Usage Instructions

### For New Employees

1. **Read the manual sequentially** - Start with Chapter 1 and work through in order
2. **Practice with Excel template** - Open worksheet.xlsx and try example calculations
3. **Use the diagrams** - Reference SVG diagrams while reading relevant chapters
4. **Complete practice exercises** - Work through examples in each chapter
5. **Seek trainer guidance** - Use Trainer Guide to know what to expect from training program

### For Trainers

1. **Review Trainer-Guide.md** - Understand the 6-week program structure
2. **Prepare materials** - Gather sample plan sets, print worksheets, set up equipment
3. **Follow lesson plans** - Use day-by-day structure in weeks 1-4
4. **Administer tests** - Give competency tests at intervals specified
5. **Provide feedback** - Use evaluation checklists for consistent assessment
6. **Track progress** - Document trainee advancement through program

### For Managers

1. **Schedule training time** - Block 4-6 weeks for new salesperson onboarding
2. **Assign trainers** - Pair new employees with experienced estimators
3. **Provide resources** - Ensure access to plan sets, Excel, scale rulers, calculators
4. **Monitor competency** - Require passing scores on all tests before solo takeoffs
5. **Review takeoffs** - Spot-check early independent work for accuracy

### Generating PDF Manual Locally

**Prerequisites:**
- Pandoc installed: `sudo apt-get install pandoc`
- LaTeX engine: `sudo apt-get install texlive texlive-xetex`

**Command:**
```bash
pandoc docs/Blueprint-Takeoff-Manual.md \
  -o Blueprint-Takeoff-Training-Manual.pdf \
  --from=markdown \
  --pdf-engine=xelatex \
  --toc
```

**Output:** Professional PDF with table of contents, ready for printing and distribution

### Customizing the Excel Template

1. Open `templates/worksheet.xlsx` in Excel
2. Modify formulas, add rows, adjust formatting as needed
3. Save changes

**OR**

1. Edit `scripts/create_excel_template.py`
2. Modify Python code to change worksheets, formulas, or styling
3. Run: `python3 scripts/create_excel_template.py`
4. New template generated at `templates/worksheet.xlsx`

---

## Regional Considerations

### Southeast Texas Specifics

This workbook includes region-specific guidance for Southeast Texas construction:

**Foundation:**
- Slab-on-grade is standard (high water table prevents basements)
- Vapor barriers required under all slabs
- Perimeter footings: minimum 16" wide × 12" deep
- Treated lumber required for all bottom plates (moisture from slab)

**Structural:**
- Hurricane/windstorm requirements per local code
- Additional anchor bolts for wind resistance
- Wind-rated shingles and fasteners recommended
- Engineered connections may be required

**Materials:**
- Humidity-resistant materials preferred (mold/mildew concerns)
- Pressure-treated lumber for all ground contact
- Corrosion-resistant fasteners in coastal areas
- Consider ventilation for attics and crawlspaces

**Code References:**
- Texas Residential Construction Commission standards
- Local amendments to IRC (International Residential Code)
- Hurricane-prone region requirements
- Energy code considerations for cooling efficiency

---

## File Structure

```
blueprint/
├── .github/
│   └── workflows/
│       └── build-manual.yml         # PDF build automation
├── docs/
│   ├── Blueprint-Takeoff-Manual.md  # Combined manual (all chapters)
│   ├── 01-introduction.md           # Chapter 1
│   ├── 02-blueprint-orientation.md  # Chapter 2
│   ├── 03-floor-plan-reading.md     # Chapter 3
│   ├── 04-wall-framing-takeoff.md   # Chapter 4
│   ├── 05-roof-takeoff.md           # Chapter 5
│   ├── 06-elevations-and-siding.md  # Chapter 6
│   ├── 07-foundation-and-concrete.md# Chapter 7
│   ├── 08-window-and-door-schedules.md # Chapter 8
│   ├── 09-material-conversion-tables.md # Chapter 9
│   ├── 10-full-example-house-takeoff.md # Chapter 10
│   ├── 11-master-worksheets.md      # Chapter 11
│   └── img/
│       ├── plan-orientation.svg
│       ├── floor-plan-basic.svg
│       ├── wall-framing-section.svg
│       ├── roof-plan-and-section.svg
│       ├── elevation-siding-areas.svg
│       ├── foundation-plan-section.svg
│       ├── window-door-schedule.svg
│       └── README.md                # Diagram production notes
├── templates/
│   └── worksheet.xlsx               # Excel takeoff calculator
├── training/
│   └── Trainer-Guide.md             # Instructor manual
├── scripts/
│   └── create_excel_template.py     # Excel generator script
├── README.md                        # Repository overview
└── release-notes.md                 # This file

```

---

## Dependencies

### For PDF Generation
- **Pandoc** (≥2.0) - Document converter
- **XeLaTeX** - LaTeX engine for PDF rendering
- **texlive-fonts-recommended** - Font packages

### For Excel Template Generation
- **Python 3.x** (tested on 3.12+)
- **openpyxl** - Excel file manipulation library
  - Install: `pip install openpyxl`

### For Training Program
- **Microsoft Excel** or compatible spreadsheet software (Google Sheets, LibreOffice Calc)
- **PDF reader** (for viewing generated manual)
- **Web browser** (for viewing SVG diagrams)
- **Scale ruler** (architect's scale for physical blueprints)
- **Calculator** (scientific or phone app)

---

## Version History

### Version 1.0 (December 2025)
**Initial Release**

**Added:**
- Complete 11-chapter Blueprint Takeoff Manual
- 7 technical diagrams (SVG format)
- Comprehensive Excel workbook with 8 worksheets
- Trainer Guide with 6-week program
- Python script for Excel generation
- GitHub Actions workflow for PDF automation
- Southeast Texas regional guidance
- Full documentation and README

**Metrics:**
- 610 lines of combined manual content
- 8 interactive Excel worksheets with formulas
- 7 production-quality technical diagrams
- 14+ competency tests and homework assignments
- 4-6 week structured training program

---

## Support and Contribution

### Questions or Issues
- Review the Trainer Guide for teaching methodology questions
- Check Excel formulas in worksheet.xlsx for calculation questions
- Refer to individual chapter markdown files for content details

### Customization
This workbook can be customized for your organization:
- Edit markdown files to add company-specific procedures
- Modify Excel template via Python script or directly
- Add regional notes for your geographic area
- Adjust competency test passing scores
- Extend training schedule for your needs

### Future Enhancements
Potential additions for future versions:
- Interior materials chapter (drywall, trim, stairs)
- Electrical and plumbing rough-in guides
- Commercial takeoff adaptations
- Video tutorials and demonstrations
- Interactive web-based calculator
- Mobile app for field use

---

## License and Attribution

**Blueprint Takeoff Workbook**  
Version 1.0 - December 2025  
Developed for Ritter Lumber and lumberyard sales training

**Usage:** This workbook is intended for training purposes in the lumber and building materials industry. Organizations are free to customize and adapt it for their internal training programs.

**Attribution:** When sharing or adapting this material, please maintain attribution to the original Blueprint Takeoff Workbook project.

---

## Acknowledgments

Thanks to the construction estimating community, lumber industry professionals, and adult education specialists who contributed insights to make this training program effective and practical.

**Special Considerations:**
- Residential construction standards (IRC)
- Southeast Texas regional practices
- Lumber yard operational workflows
- Adult learning principles
- Hands-on trade education methodology

---

**For More Information:**
- See `README.md` for repository overview
- See `training/Trainer-Guide.md` for teaching instructions
- See `docs/Blueprint-Takeoff-Manual.md` for complete manual
- See `templates/worksheet.xlsx` for interactive calculator

---

**End of Release Notes v1.0**
