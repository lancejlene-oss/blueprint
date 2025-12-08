# Blueprint Takeoff Workbook

**A Complete Professional Training System for Residential Blueprint Takeoffs**

This repository contains a comprehensive training workbook that teaches lumberyard salespeople how to perform accurate manual residential blueprint takeoffs from start to finish. The system includes detailed instruction manuals, interactive Excel calculators, technical diagrams, trainer resources, and everything needed to develop competent estimators with zero outside help.

**Company:** Ritter Lumber (and similar lumberyard operations)  
**Target Audience:** New salespeople, experienced estimators, and training managers  
**Skill Level:** Beginner to intermediate (suitable for brand-new employees)  
**Region:** Optimized for Southeast Texas construction practices (adaptable to other regions)

---

## 📚 What's Included

### 1. Comprehensive Training Manual

**11-chapter workbook** covering the complete residential takeoff workflow:

- **Chapter 1:** Introduction - Purpose, learning outcomes, manual structure
- **Chapter 2:** Blueprint Orientation - Sheet types, title blocks, scales, revisions
- **Chapter 3:** Floor Plan Reading - Walls, openings, dimensions, symbols
- **Chapter 4:** Wall Framing Takeoff - Studs, plates, headers, calculations
- **Chapter 5:** Roof Takeoff - Geometry, slope factors, sheathing, shingles
- **Chapter 6:** Elevations & Siding - Façade analysis, area calculations
- **Chapter 7:** Foundation & Concrete - Slabs, footings, rebar, volumes
- **Chapter 8:** Window & Door Schedules - Tags, rough openings, framing
- **Chapter 9:** Material Conversion Tables - Quick-reference multipliers
- **Chapter 10:** Full Example House Takeoff - Step-by-step complete walkthrough
- **Chapter 11:** Master Worksheets - Printable templates for field use

**Total Content:** 610+ lines of detailed instruction, formulas, examples, and tips

### 2. Technical Diagrams

**7 production-quality SVG diagrams** illustrating key concepts:

- **plan-orientation.svg** - Blueprint navigation (title block, north arrow, scale bar, legend)
- **floor-plan-basic.svg** - Floor plan elements (walls, doors, windows, dimensions)
- **wall-framing-section.svg** - Detailed wall assembly (studs, plates, headers, blocking)
- **roof-plan-and-section.svg** - Roof geometry (plan, section, pitch calculations)
- **elevation-siding-areas.svg** - Siding calculations with area breakdown
- **foundation-plan-section.svg** - Foundation details (slab, footings, piers, rebar)
- **window-door-schedule.svg** - Schedule coordination between table and plan

All diagrams are technically accurate, based on real-world construction details, and suitable for printing.

### 3. Interactive Excel Workbook

**Comprehensive multi-sheet calculator** (`templates/worksheet.xlsx`) with 8 worksheets:

1. **Project Info** - Project details, specifications, regional notes for SE Texas
2. **Wall Framing** - Automatic stud count, plate LF, corner/intersection adds
3. **Roof Takeoff** - Slope factors, sheathing sheets, shingle bundles with waste
4. **Foundation** - Concrete volumes (CF to CY), rebar LF calculations
5. **Siding & Exterior** - Wall/gable areas, opening deductions, trim tracking
6. **Windows & Doors** - Tag-based schedule with rough openings and headers
7. **Material Summary** - Quote-ready export with pricing and extended totals
8. **Conversion Tables** - Quick reference for slopes, board feet, waste factors

**Key Features:**
- All formulas pre-loaded and tested
- Print-ready page layouts
- Color-coded for easy navigation
- Links between worksheets
- Documentation prompts throughout

### 4. Trainer's Guide

**Complete instructor manual** (`training/Trainer-Guide.md`) with:

- **6-week training program** with day-by-day lesson plans
- **Module-by-module teaching tips** and common mistake warnings
- **4 competency tests** with passing criteria and answer keys
- **Example homework assignments** for each training week
- **Evaluation checklists** for reviewing trainee work
- **Group training session formats** and exercises
- **Common training challenges** with proven solutions
- **Resource recommendations** and material lists

**Program Structure:**
- Week 1: Blueprint orientation & reading
- Week 2: Wall framing & foundation
- Week 3: Roof & exterior materials
- Week 4: Windows, doors & assembly
- Weeks 5-6: Independent practice & competency testing

### 5. Build Automation

**GitHub Actions workflow** (`.github/workflows/build-manual.yml`):
- Automatically generates PDF from markdown manual
- Triggers on changes to documentation files
- Uploads artifact: `Blueprint-Takeoff-Training-Manual.pdf`
- Can be manually triggered from Actions tab
- Includes Pandoc and LaTeX installation

---

## 🚀 Quick Start

### For New Employees

1. **Read the manual** - Start with `docs/Blueprint-Takeoff-Manual.md` (or get PDF from trainer)
2. **Open the Excel template** - Use `templates/worksheet.xlsx` to follow along with examples
3. **Review diagrams** - Reference SVG images in `docs/img/` as you read each chapter
4. **Practice calculations** - Work through all chapter examples by hand and in Excel
5. **Complete homework** - Your trainer will assign practice takeoffs from the Trainer Guide

**First Takeoff Timeline:** Most new employees can complete an independent takeoff after 4-6 weeks of training.

### For Trainers

1. **Review the Trainer Guide** - Read `training/Trainer-Guide.md` to understand the 6-week program
2. **Gather materials** - Collect sample plan sets, print worksheets, prepare equipment
3. **Follow lesson plans** - Use the day-by-day structure in Weeks 1-4
4. **Administer tests** - Give competency tests at specified intervals
5. **Provide feedback** - Use evaluation checklists for consistent assessment

**Trainer Preparation Time:** ~2-3 hours to review materials and gather plan sets before first session.

### For Managers

1. **Schedule training time** - Block 4-6 weeks for new salesperson onboarding
2. **Assign trainers** - Pair new employees with experienced estimators
3. **Provide resources** - Ensure access to plan sets, Excel, scale rulers, calculators
4. **Monitor competency** - Require passing scores on all tests before solo takeoffs
5. **Review early work** - Spot-check first few independent takeoffs for accuracy

**Expected ROI:** Trained employees can produce accurate takeoffs independently, reducing errors, returns, and senior staff review time.

---

## 📁 Repository Structure

```
blueprint/
├── .github/
│   └── workflows/
│       └── build-manual.yml         # PDF generation automation
├── docs/
│   ├── Blueprint-Takeoff-Manual.md  # Complete combined manual (610+ lines)
│   ├── 01-introduction.md           # Individual chapters for reference
│   ├── 02-blueprint-orientation.md
│   ├── 03-floor-plan-reading.md
│   ├── 04-wall-framing-takeoff.md
│   ├── 05-roof-takeoff.md
│   ├── 06-elevations-and-siding.md
│   ├── 07-foundation-and-concrete.md
│   ├── 08-window-and-door-schedules.md
│   ├── 09-material-conversion-tables.md
│   ├── 10-full-example-house-takeoff.md
│   ├── 11-master-worksheets.md
│   └── img/                         # 7 technical diagrams (SVG)
│       ├── plan-orientation.svg
│       ├── floor-plan-basic.svg
│       ├── wall-framing-section.svg
│       ├── roof-plan-and-section.svg
│       ├── elevation-siding-areas.svg
│       ├── foundation-plan-section.svg
│       ├── window-door-schedule.svg
│       └── README.md                # Diagram production notes
├── templates/
│   └── worksheet.xlsx               # Excel calculator (8 worksheets)
├── training/
│   └── Trainer-Guide.md             # Complete instructor manual
├── scripts/
│   └── create_excel_template.py     # Python script to regenerate Excel file
├── README.md                        # This file
└── release-notes.md                 # Version history and detailed contents
```

---

## 📖 How to Use This Workbook

### Typical Workflow: A Takeoff from Start to Finish

**For a new residential project, follow this sequence:**

#### 1. Project Setup (15-20 minutes)
- Receive plan set from builder
- Review all sheets for completeness
- Verify scale on architectural floor plan
- Note latest revision dates
- Fill out "Project Info" worksheet in Excel
- Highlight any alternates or special conditions

#### 2. Wall Framing Takeoff (45-60 minutes)
- Review Chapters 3 and 4 of manual
- Identify all exterior and interior walls on floor plan
- Measure wall lengths from dimension strings
- Calculate studs using formula: `(Length ÷ Spacing) + 1`
- Add corner and intersection studs per wall
- Account for window and door openings (king/jack studs)
- Calculate plate linear footage (bottom + double top)
- Record on "Wall Framing" worksheet

#### 3. Roof Takeoff (30-45 minutes)
- Review Chapter 5 of manual
- Identify roof geometry (gable, hip, complex)
- Measure horizontal dimensions of each roof plane
- Apply slope factor from reference table
- Calculate surface area and sheathing sheets
- Estimate shingle bundles with waste factor
- Record on "Roof Takeoff" worksheet

#### 4. Foundation Takeoff (20-30 minutes)
- Review Chapter 7 of manual
- Measure slab dimensions from foundation plan
- Calculate slab volume (length × width × thickness/12)
- Measure perimeter footing linear footage
- Calculate footing volume
- Convert cubic feet to cubic yards (÷27)
- Estimate rebar based on slab area
- Record on "Foundation" worksheet
- Note SE Texas specifics (treated plates, vapor barrier)

#### 5. Siding & Exterior (30-40 minutes)
- Review Chapter 6 of manual
- Calculate each elevation's wall area (width × height)
- Calculate gable areas (width × rise ÷ 2)
- Deduct window and door openings
- Apply waste factor (10% for vinyl, 15% for lap)
- Estimate trim: fascia, soffit, corner boards
- Record on "Siding & Exterior" worksheet

#### 6. Windows & Doors (15-20 minutes)
- Review Chapter 8 of manual
- Transfer schedule from plan sheets to worksheet
- Match tags to floor plan locations
- Verify quantities (count each tag on plans)
- Note rough opening sizes
- Determine header requirements
- Record on "Windows & Doors" worksheet

#### 7. Material Summary (20-30 minutes)
- Transfer quantities from all worksheets to "Material Summary"
- Apply final waste factors where needed
- Convert units (LF to sticks, SF to squares, etc.)
- Add pricing if available
- Calculate extended totals
- Review for completeness and reasonableness

#### 8. Quality Check (10-15 minutes)
- Double-check all formulas
- Verify units are correct (LF, SF, CY, EA)
- Confirm waste factors applied
- Review notes for clarity
- Check that assumptions are documented
- Sign and date all worksheets

**Total Time:** 3-4 hours for a typical 1,500-2,000 SF home (faster with experience)

**Output:** Complete material list ready for quoting and ordering

---

## 🛠️ Generating the PDF Manual

### Local Generation

**Prerequisites:**
```bash
sudo apt-get update
sudo apt-get install pandoc texlive texlive-xetex texlive-fonts-recommended
```

**Generate PDF:**
```bash
pandoc docs/Blueprint-Takeoff-Manual.md \
  -o Blueprint-Takeoff-Training-Manual.pdf \
  --from=markdown \
  --pdf-engine=xelatex \
  --toc
```

**Output:** Professional PDF with table of contents, ready for printing and distribution

### GitHub Actions (Automatic)

The workflow at `.github/workflows/build-manual.yml` automatically:
- Installs Pandoc and LaTeX
- Generates PDF from `Blueprint-Takeoff-Manual.md`
- Uploads artifact: `Blueprint-Takeoff-Training-Manual.pdf`

**Triggers:**
- Push to main branch with changes to `docs/` or `README.md`
- Pull request with changes to documentation
- Manual workflow dispatch from Actions tab

**To download generated PDF:**
1. Go to Actions tab in GitHub
2. Select latest successful workflow run
3. Download "blueprint-takeoff-manual" artifact

---

## 🎓 Training Program Overview

### Learning Objectives

By completing this training program, new salespeople will be able to:

1. **Read and interpret** residential blueprint sets without assistance
2. **Calculate quantities** for framing, roofing, siding, and foundation materials
3. **Document assumptions** clearly using standardized worksheets
4. **Identify errors** in their own work and correct them before submission
5. **Communicate effectively** with builders about material needs and alternates
6. **Apply regional standards** specific to Southeast Texas construction

### Program Duration

**Full Training:** 4-6 weeks (varies by prior experience)

**Breakdown:**
- Week 1: Blueprint orientation and reading fundamentals
- Week 2: Wall framing calculations and foundation takeoffs
- Week 3: Roof geometry and exterior materials
- Week 4: Windows, doors, and complete takeoff assembly
- Weeks 5-6: Independent practice with trainer review and competency testing

### Competency Tests

**Four assessments measure progress:**

1. **Test 1: Blueprint Reading** (Week 1)
   - Time: 30 minutes
   - Format: Written exam with plan set
   - Passing: 80% or higher

2. **Test 2: Wall Framing** (Week 2)
   - Time: 45 minutes
   - Format: Calculation exercises
   - Passing: 85% or higher

3. **Test 3: Roof & Foundation** (Week 3)
   - Time: 60 minutes
   - Format: Calculation exercises
   - Passing: 85% or higher

4. **Test 4: Full Takeoff Competency** (Week 6)
   - Time: 4 hours (full workday)
   - Format: Complete takeoff of unfamiliar plan set
   - Passing: 90% accuracy, all worksheets complete

**Certification:** Trainees who pass all tests are certified for independent takeoff work with spot-check review.

---

## 🌎 Regional Considerations

### Southeast Texas Construction Specifics

This workbook includes region-specific guidance optimized for Southeast Texas but adaptable to other areas:

**Foundation:**
- **Slab-on-grade is standard** - High water table prevents basements and crawlspaces
- **Vapor barriers required** - 6 mil polyethylene under all slabs
- **Treated lumber for bottom plates** - Moisture from slab contact requires treated material
- **Thickened edge footings** - Typical 16" wide × 12" deep perimeter footings

**Structural:**
- **Hurricane/windstorm requirements** - Coastal proximity requires enhanced fastening
- **Additional anchor bolts** - Wind uplift resistance per local amendments to IRC
- **Wind-rated shingles** - ASTM D3161 Class H or better for high-wind areas
- **Engineered connections** - Simpson or equivalent straps and ties often required

**Materials:**
- **Humidity-resistant materials** - High humidity and heat require mold/mildew considerations
- **Corrosion-resistant fasteners** - Galvanized or stainless steel for coastal zones
- **Proper ventilation** - Attic and crawlspace ventilation critical for moisture control

**Code References:**
- Texas Residential Construction Commission standards
- Local amendments to International Residential Code (IRC)
- Hurricane-prone region requirements (ASCE 7)
- Energy code for cooling efficiency

**Adaptability:** Users in other regions should consult local building codes and replace SE Texas notes with their regional requirements in the Excel "Project Info" worksheet.

---

## 📋 Recommended Printing Formats

### For Daily Use

**Manual:**
- **Format:** PDF, 8.5" × 11" portrait
- **Binding:** 3-ring binder with tabs for each chapter
- **Quantity:** One per trainee, one for trainer's desk reference
- **Color:** Black & white acceptable, color diagrams preferred

**Worksheets:**
- **Source:** Excel "Print Area" settings already configured
- **Format:** 8.5" × 11" portrait (most worksheets) or landscape (Material Summary)
- **Quantity:** Print as needed for each project
- **Storage:** File completed worksheets with project documentation

**Diagrams:**
- **Source:** SVG files in `docs/img/`
- **Format:** 11" × 17" for training sessions (enlarged for visibility)
- **Format:** 8.5" × 11" for individual reference
- **Mounting:** Laminate for durability, post in training area

### For Training Sessions

**Trainer Guide:**
- **Format:** PDF from `training/Trainer-Guide.md`
- **Binding:** Spiral or 3-ring binder
- **Quantity:** One per trainer
- **Updates:** Re-print when adding custom content

**Practice Plan Sets:**
- **Format:** Full-size architectural prints (24" × 36") preferred
- **Alternative:** Half-size (11" × 17") acceptable if scale verified
- **Quantity:** 5-10 sets of varying complexity
- **Storage:** Flat file or rolled in tubes

---

## 🔧 Customizing for Your Organization

### Modifying the Manual

**To add company-specific content:**

1. Edit individual chapter markdown files in `docs/`
2. Add your procedures, vendor names, pricing notes
3. Regenerate combined manual:
   ```bash
   # Concatenate chapters in order
   cat docs/01-introduction.md docs/02-blueprint-orientation.md \
       [etc...] > docs/Blueprint-Takeoff-Manual.md
   ```
4. Generate PDF with Pandoc (see instructions above)

**Common customizations:**
- Add company logo to title page
- Insert vendor contact information
- Modify waste factors for your suppliers
- Add examples from your actual projects
- Update regional notes for your area

### Customizing the Excel Template

**Option 1: Direct Editing**
1. Open `templates/worksheet.xlsx` in Excel
2. Modify formulas, add rows, change formatting
3. Save and distribute updated template

**Option 2: Regenerate via Python Script**
1. Edit `scripts/create_excel_template.py`
2. Modify functions to change worksheets, formulas, colors
3. Run: `python3 scripts/create_excel_template.py`
4. New template generated at `templates/worksheet.xlsx`

**Common customizations:**
- Add your company name to header
- Modify waste factor defaults
- Add additional material categories
- Include vendor part numbers
- Integrate with your pricing database

---

## 📊 Version Information

**Current Version:** 1.0 (December 2025)

**Release Contents:**
- 11-chapter training manual (610+ lines)
- 7 technical diagrams (SVG format)
- 8-worksheet Excel calculator
- Complete trainer's guide
- Python generation script
- GitHub Actions automation

**See `release-notes.md` for:**
- Detailed version history
- Complete file inventory
- Feature descriptions
- Dependencies and requirements
- Future enhancement roadmap

---

## 💡 Tips for Success

### For New Employees

- **Take your time** - Accuracy is more important than speed
- **Show your work** - Document calculations and assumptions
- **Ask questions** - No question is too basic during training
- **Practice regularly** - Skill develops through repetition
- **Use the Excel template** - Formulas catch math errors
- **Review your work** - Always double-check before submitting

### For Trainers

- **Be patient** - Different trainees learn at different rates
- **Use real plans** - Actual projects are more engaging than contrived examples
- **Provide immediate feedback** - Correct errors while they're fresh
- **Celebrate progress** - Acknowledge improvements and milestones
- **Adapt the program** - Adjust pacing based on trainee needs
- **Share war stories** - Real-world examples illustrate why accuracy matters

### For Managers

- **Invest in training time** - Rushed training leads to costly errors
- **Provide good materials** - Quality plan sets, tools, and workspace matter
- **Set clear expectations** - Define competency requirements upfront
- **Support continuous learning** - Encourage ongoing skill development
- **Review early takeoffs** - Spot-check work until confidence is established
- **Track accuracy metrics** - Measure improvement over time

---

## 🆘 Troubleshooting

### Common Issues

**"My stud counts don't match the trainer's answer"**
- Verify you're using correct spacing (16" vs 24")
- Check that you added the "+1" in the formula
- Confirm corner and intersection adds are included
- Review window/door opening adjustments

**"The roof area calculation seems wrong"**
- Ensure you applied the slope factor (don't use horizontal area for shingles)
- Check that you're using the correct pitch (6:12 vs 12:6)
- Verify you measured the correct plane dimensions
- Confirm waste factor is applied

**"I can't verify the scale on this plan"**
- Try a different known dimension (door width, room length)
- Check if the plan was printed at a non-standard size
- Use the PDF measurement tool and adjust zoom
- Ask the builder for confirmation of plan scale

**"The Excel formulas aren't working"**
- Ensure you're entering numbers, not text (use "24" not "24 feet")
- Check that you haven't deleted rows with formulas
- Verify Excel calculated formulas (press F9 to recalculate)
- Regenerate template from Python script if corrupted

---

## 📞 Support

For questions or issues:

1. **Check the Trainer Guide** - `training/Trainer-Guide.md` has troubleshooting section
2. **Review Chapter Examples** - Each chapter has worked examples with solutions
3. **Consult Conversion Tables** - Quick reference in Chapter 9 and Excel
4. **Ask Your Trainer** - Designated trainers can answer specific questions
5. **Check Release Notes** - `release-notes.md` has detailed documentation

---

## 📄 License and Attribution

**Blueprint Takeoff Workbook**  
Version 1.0 - December 2025  
Developed for Ritter Lumber and lumberyard sales training

**Usage:** This workbook is intended for training purposes in the lumber and building materials industry. Organizations are free to customize and adapt it for their internal training programs.

**Attribution:** When sharing or adapting this material, please maintain attribution to the original Blueprint Takeoff Workbook project.

---

## 🎯 Next Steps

Ready to get started? Here's what to do:

**If you're a new employee:**
1. Download or print the manual (`docs/Blueprint-Takeoff-Manual.md` or PDF)
2. Open the Excel template (`templates/worksheet.xlsx`)
3. Read Chapter 1 to understand the training program
4. Contact your trainer to schedule your first session

**If you're a trainer:**
1. Read the Trainer Guide (`training/Trainer-Guide.md`)
2. Gather 5-10 sample plan sets of varying complexity
3. Print worksheets and prepare materials
4. Schedule Week 1 training sessions with new employees

**If you're a manager:**
1. Review the 6-week program structure
2. Assign trainers to new salespeople
3. Allocate time for training (4-6 weeks minimum)
4. Set expectations for competency test passing scores
5. Establish review process for early independent takeoffs

---

**Questions? Issues? Suggestions?**  
This is a living document. Feedback from users helps improve future versions.

**Good luck with your blueprint takeoff training! 📐📏🏗️**
