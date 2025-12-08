#!/usr/bin/env python3
"""
Upgrade the Excel workbook into a Field Takeoff Pack with:
- Step-by-step instructions
- Embedded diagrams
- Cross-references to PDF manual
- Tips and common mistakes
"""

from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.drawing.image import Image as XLImage
from openpyxl.utils import get_column_letter
import os
import subprocess
import sys

# Paths
script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.dirname(script_dir)
excel_path = os.path.join(repo_root, 'templates', 'worksheet.xlsx')
img_dir = os.path.join(repo_root, 'docs', 'img')
temp_dir = os.path.join(repo_root, 'tmp')

# Create temp directory for converted images
os.makedirs(temp_dir, exist_ok=True)

def convert_svg_to_png(svg_path, png_path, width=400):
    """Convert SVG to PNG using cairosvg or rsvg-convert"""
    try:
        # Try using rsvg-convert (from librsvg2-bin)
        subprocess.run([
            'rsvg-convert',
            '-w', str(width),
            svg_path,
            '-o', png_path
        ], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            # Try using cairosvg
            import cairosvg
            cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=width)
            return True
        except ImportError:
            print(f"Warning: Could not convert {svg_path} - install librsvg2-bin or cairosvg")
            return False

def add_bordered_box(ws, start_row, start_col, end_row, end_col, title, fill_color="E7E6E6"):
    """Add a bordered box with title"""
    thin_border = Border(
        left=Side(style='thin'),
        right=Side(style='thin'),
        top=Side(style='thin'),
        bottom=Side(style='thin')
    )
    
    title_fill = PatternFill(start_color=fill_color, end_color=fill_color, fill_type="solid")
    
    # Merge title cell if multi-column
    if end_col > start_col:
        ws.merge_cells(start_row=start_row, start_column=start_col, 
                      end_row=start_row, end_column=end_col)
    
    title_cell = ws.cell(row=start_row, column=start_col)
    title_cell.value = title
    title_cell.font = Font(bold=True, size=11)
    title_cell.fill = title_fill
    title_cell.alignment = Alignment(horizontal='center', vertical='center')
    title_cell.border = thin_border
    
    # Add borders to all cells in the box
    for row in range(start_row, end_row + 1):
        for col in range(start_col, end_col + 1):
            ws.cell(row=row, column=col).border = thin_border

def add_instruction_text(ws, row, col, text, bold=False):
    """Add instruction text to a cell"""
    cell = ws.cell(row=row, column=col)
    cell.value = text
    cell.font = Font(bold=bold, size=10)
    cell.alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    return cell

def add_tips_box(ws, start_row, start_col, tips_list, manual_ref=""):
    """Add a tips box with bullet points"""
    # Title
    add_bordered_box(ws, start_row, start_col, start_row + len(tips_list) + 1 + (1 if manual_ref else 0), 
                    start_col + 1, "💡 TIPS & COMMON MISTAKES", "FFF2CC")
    
    # Tips
    current_row = start_row + 1
    for tip in tips_list:
        cell = ws.cell(row=current_row, column=start_col)
        cell.value = f"• {tip}"
        cell.alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
        cell.font = Font(size=9)
        ws.merge_cells(start_row=current_row, start_column=start_col, 
                      end_row=current_row, end_column=start_col + 1)
        current_row += 1
    
    # Manual reference
    if manual_ref:
        cell = ws.cell(row=current_row, column=start_col)
        cell.value = f"📖 {manual_ref}"
        cell.alignment = Alignment(horizontal='left', vertical='center')
        cell.font = Font(size=9, italic=True, color="0000FF")
        ws.merge_cells(start_row=current_row, start_column=start_col, 
                      end_row=current_row, end_column=start_col + 1)

def insert_diagram(ws, png_path, cell_ref, caption=""):
    """Insert a diagram image into the worksheet"""
    if not os.path.exists(png_path):
        return  # Skip if image doesn't exist
    
    try:
        img = XLImage(png_path)
        # Resize to fit nicely (width ~300-400 pixels)
        if img.width > 0:
            img.width = 350
            img.height = int(img.height * (350 / img.width))
        else:
            # Invalid image, skip it
            return
        ws.add_image(img, cell_ref)
    except Exception as e:
        print(f"  ⚠ Warning: Could not insert diagram {png_path}: {e}")
        return
        
        # Add caption below if provided
        if caption:
            # Parse cell ref to get row/col
            from openpyxl.utils import column_index_from_string, get_column_letter
            col_letter = ''.join([c for c in cell_ref if c.isalpha()])
            row_num = int(''.join([c for c in cell_ref if c.isdigit()]))
            
            # Add caption about 18 rows below (depending on image height)
            caption_row = row_num + max(18, int(img.height / 15))
            caption_cell = ws.cell(row=caption_row, column=column_index_from_string(col_letter))
            caption_cell.value = caption
            caption_cell.font = Font(italic=True, size=9, color="0000FF")
            caption_cell.alignment = Alignment(horizontal='left')

print("🔧 Upgrading Excel Workbook to Field Takeoff Pack...")

# Load the workbook with error handling
try:
    if not os.path.exists(excel_path):
        print(f"❌ Error: Excel file not found at {excel_path}")
        print("   Run create_excel_template.py first to create the base workbook.")
        sys.exit(1)
    
    wb = load_workbook(excel_path)
    print(f"✓ Loaded workbook: {excel_path}")
except Exception as e:
    print(f"❌ Error loading Excel file: {e}")
    print("   The file may be corrupted or open in another program.")
    sys.exit(1)

# Convert SVG diagrams to PNG
diagrams = {
    'plan-orientation': 'plan-orientation.svg',
    'floor-plan-basic': 'floor-plan-basic.svg',
    'foundation-plan-section': 'foundation-plan-section.svg',
    'wall-framing-section': 'wall-framing-section.svg',
    'roof-plan-and-section': 'roof-plan-and-section.svg',
    'elevation-siding-areas': 'elevation-siding-areas.svg',
    'window-door-schedule': 'window-door-schedule.svg',
}

png_files = {}
for key, svg_file in diagrams.items():
    svg_path = os.path.join(img_dir, svg_file)
    
    # Check if SVG file exists
    if not os.path.exists(svg_path):
        print(f"⚠ Warning: SVG file not found: {svg_path}")
        continue
    
    png_path = os.path.join(temp_dir, f'{key}.png')
    if convert_svg_to_png(svg_path, png_path):
        png_files[key] = png_path
        print(f"✓ Converted {svg_file} to PNG")
    else:
        print(f"✗ Failed to convert {svg_file}")

print("\n📝 Upgrading worksheets...")

# ==========================================
# 1. PROJECT INFO - Step 0
# ==========================================
print("  → Project Info (Step 0)")
ws = wb['Project Info']

# Insert rows at top for instructions
ws.insert_rows(1, 8)

# Add step header
step_cell = ws.cell(row=1, column=1)
step_cell.value = "STEP 0 — PLAN SETUP & ORIENTATION"
step_cell.font = Font(bold=True, size=14, color="FFFFFF")
step_cell.fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
step_cell.alignment = Alignment(horizontal='center', vertical='center')
ws.merge_cells('A1:F1')
ws.row_dimensions[1].height = 25

# Add instruction checklist
instructions = [
    "1. Verify you have the LATEST REVISION of the plan set",
    "2. Check the scale on the title block (usually 1/4\" = 1'-0\")",
    "3. Verify scale by measuring a known dimension with your scale ruler",
    "4. Note any addenda, alternates, or special conditions",
    "5. Fill in project information below before proceeding to Step 1"
]

ws.cell(row=2, column=1).value = "INSTRUCTIONS:"
ws.cell(row=2, column=1).font = Font(bold=True, size=10)

for idx, instruction in enumerate(instructions, start=3):
    cell = ws.cell(row=idx, column=1)
    cell.value = instruction
    cell.font = Font(size=9)
    cell.alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    ws.merge_cells(f'A{idx}:D{idx}')

# Add checklist boxes
ws.cell(row=3, column=5).value = "☐ Latest revision confirmed"
ws.cell(row=4, column=5).value = "☐ Scale verified"
ws.cell(row=5, column=5).value = "☐ Windstorm/code notes checked"
for r in [3, 4, 5]:
    ws.cell(row=r, column=5).font = Font(size=9)
    ws.merge_cells(f'E{r}:F{r}')

# Manual reference
ws.cell(row=7, column=1).value = "📖 See Manual: p. 4-7 — Getting Started & Plan Orientation"
ws.cell(row=7, column=1).font = Font(italic=True, size=9, color="0000FF")
ws.merge_cells('A7:F7')

# Insert diagram
if 'plan-orientation' in png_files:
    insert_diagram(ws, png_files['plan-orientation'], 'H2', 
                  "Plan Orientation Diagram — See Manual p. 5")

# Adjust existing content (moved down 8 rows)
# Original PROJECT INFORMATION was at A3, now at A11

# ==========================================
# 2. FOUNDATION - Step 1
# ==========================================
print("  → Foundation (Step 1)")
ws = wb['Foundation']

# Insert rows for instructions
ws.insert_rows(1, 7)

# Step header
step_cell = ws.cell(row=1, column=1)
step_cell.value = "STEP 1 — FOUNDATION & SLAB TAKEOFF"
step_cell.font = Font(bold=True, size=14, color="FFFFFF")
step_cell.fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
step_cell.alignment = Alignment(horizontal='center', vertical='center')
ws.merge_cells('A1:H1')
ws.row_dimensions[1].height = 25

# Instructions
instructions = [
    "1. Locate foundation/structural sheets in the plan set",
    "2. Trace the perimeter of the slab and any interior beams",
    "3. Measure each segment and enter lengths in the table below",
    "4. Record slab thickness, beam sizes, and notes/assumptions"
]

ws.cell(row=2, column=1).value = "INSTRUCTIONS:"
ws.cell(row=2, column=1).font = Font(bold=True, size=10)

for idx, instruction in enumerate(instructions, start=3):
    cell = ws.cell(row=idx, column=1)
    cell.value = instruction
    cell.font = Font(size=9)
    cell.alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
    ws.merge_cells(f'A{idx}:E{idx}')

# Tips box
ws.cell(row=2, column=6).value = "💡 TIPS"
ws.cell(row=2, column=6).font = Font(bold=True, size=10)
ws.cell(row=2, column=6).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.merge_cells('F2:H2')

tips = [
    "Include porches and garage slabs",
    "Note any assumed beam sizes for review",
    "Remember to convert thickness to feet"
]
for idx, tip in enumerate(tips, start=3):
    cell = ws.cell(row=idx, column=6)
    cell.value = f"• {tip}"
    cell.font = Font(size=9)
    cell.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'F{idx}:H{idx}')

ws.cell(row=6, column=6).value = "📖 Manual: p. 8-10 — Foundation"
ws.cell(row=6, column=6).font = Font(italic=True, size=9, color="0000FF")
ws.merge_cells('F6:H6')

# Insert diagram
if 'foundation-plan-section' in png_files:
    insert_diagram(ws, png_files['foundation-plan-section'], 'J2',
                  "Foundation Section — Manual p. 8-10")

# ==========================================
# 3. WALL FRAMING - Step 2
# ==========================================
print("  → Wall Framing (Step 2)")
ws = wb['Wall Framing']

# Insert rows
ws.insert_rows(1, 7)

# Step header
step_cell = ws.cell(row=1, column=1)
step_cell.value = "STEP 2 — WALL FRAMING TAKEOFF"
step_cell.font = Font(bold=True, size=14, color="FFFFFF")
step_cell.fill = PatternFill(start_color="ED7D31", end_color="ED7D31", fill_type="solid")
step_cell.alignment = Alignment(horizontal='center', vertical='center')
ws.merge_cells('A1:M1')
ws.row_dimensions[1].height = 25

# Instructions
ws.cell(row=2, column=1).value = "INSTRUCTIONS:"
ws.cell(row=2, column=1).font = Font(bold=True, size=10)

instructions = [
    "1. Highlight all exterior walls on the floor plan",
    "2. Label walls W1, W2, W3... moving clockwise from front left",
    "3. Measure each wall and enter: length, height, stud spacing",
    "4. Count corners, tees, and openings (windows/doors)"
]

for idx, instruction in enumerate(instructions, start=3):
    cell = ws.cell(row=idx, column=1)
    cell.value = instruction
    cell.font = Font(size=9)
    cell.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'A{idx}:F{idx}')

# Tips box
ws.cell(row=2, column=8).value = "💡 TIPS"
ws.cell(row=2, column=8).font = Font(bold=True, size=10)
ws.cell(row=2, column=8).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.merge_cells('H2:J2')

tips = [
    "Add extra studs for corners (3) and tees (2)",
    "Use header schedule for kings/jacks—don't guess",
    "Remember the '+1' in stud count formula"
]
for idx, tip in enumerate(tips, start=3):
    cell = ws.cell(row=idx, column=8)
    cell.value = f"• {tip}"
    cell.font = Font(size=9)
    cell.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'H{idx}:J{idx}')

ws.cell(row=6, column=8).value = "📖 Manual: p. 14-17 — Wall Framing"
ws.cell(row=6, column=8).font = Font(italic=True, size=9, color="0000FF")
ws.merge_cells('H6:J6')

# Insert diagram
if 'wall-framing-section' in png_files:
    insert_diagram(ws, png_files['wall-framing-section'], 'K2',
                  "Wall Section — Manual p. 14-17")

# ==========================================
# 4. ROOF TAKEOFF - Step 3
# ==========================================
print("  → Roof Takeoff (Step 3)")
ws = wb['Roof Takeoff']

# Insert rows
ws.insert_rows(1, 7)

# Step header
step_cell = ws.cell(row=1, column=1)
step_cell.value = "STEP 3 — ROOF TAKEOFF"
step_cell.font = Font(bold=True, size=14, color="FFFFFF")
step_cell.fill = PatternFill(start_color="5B9BD5", end_color="5B9BD5", fill_type="solid")
step_cell.alignment = Alignment(horizontal='center', vertical='center')
ws.merge_cells('A1:N1')
ws.row_dimensions[1].height = 25

# Instructions
ws.cell(row=2, column=1).value = "INSTRUCTIONS:"
ws.cell(row=2, column=1).font = Font(bold=True, size=10)

instructions = [
    "1. Locate roof plan and framing details",
    "2. For each roof plane, record: width, length, pitch, overhang",
    "3. Use slope factor table to calculate sheathing area",
    "4. Remember: porch and garage roofs count too!"
]

for idx, instruction in enumerate(instructions, start=3):
    cell = ws.cell(row=idx, column=1)
    cell.value = instruction
    cell.font = Font(size=9)
    cell.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'A{idx}:F{idx}')

# Tips box
ws.cell(row=2, column=8).value = "💡 TIPS"
ws.cell(row=2, column=8).font = Font(bold=True, size=10)
ws.cell(row=2, column=8).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.merge_cells('H2:J2')

tips = [
    "Include overhangs in width/length for sheathing",
    "Don't forget porch and garage roofs",
    "Add 10-15% waste for shingles"
]
for idx, tip in enumerate(tips, start=3):
    cell = ws.cell(row=idx, column=8)
    cell.value = f"• {tip}"
    cell.font = Font(size=9)
    cell.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'H{idx}:J{idx}')

ws.cell(row=6, column=8).value = "📖 Manual: p. 18-20 — Roof Takeoff"
ws.cell(row=6, column=8).font = Font(italic=True, size=9, color="0000FF")
ws.merge_cells('H6:J6')

# Insert diagram
if 'roof-plan-and-section' in png_files:
    insert_diagram(ws, png_files['roof-plan-and-section'], 'K2',
                  "Roof Plan & Pitch — Manual p. 18-20")

# ==========================================
# 5. SIDING & EXTERIOR - Step 4
# ==========================================
print("  → Siding & Exterior (Step 4)")
ws = wb['Siding & Exterior']

# Insert rows
ws.insert_rows(1, 7)

# Step header
step_cell = ws.cell(row=1, column=1)
step_cell.value = "STEP 4 — SIDING, SOFFIT, FASCIA & EXTERIOR TRIM"
step_cell.font = Font(bold=True, size=14, color="FFFFFF")
step_cell.fill = PatternFill(start_color="A5A5A5", end_color="A5A5A5", fill_type="solid")
step_cell.alignment = Alignment(horizontal='center', vertical='center')
ws.merge_cells('A1:K1')
ws.row_dimensions[1].height = 25

# Instructions
ws.cell(row=2, column=1).value = "INSTRUCTIONS:"
ws.cell(row=2, column=1).font = Font(bold=True, size=10)

instructions = [
    "1. Use each elevation (Front, Rear, Left, Right)",
    "2. Measure wall width, height, and gable rise if applicable",
    "3. Subtract windows/doors based on siding type",
    "4. Calculate linear feet for trim, fascia, soffit"
]

for idx, instruction in enumerate(instructions, start=3):
    cell = ws.cell(row=idx, column=1)
    cell.value = instruction
    cell.font = Font(size=9)
    cell.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'A{idx}:E{idx}')

# Tips box
ws.cell(row=2, column=7).value = "💡 TIPS"
ws.cell(row=2, column=7).font = Font(bold=True, size=10)
ws.cell(row=2, column=7).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.merge_cells('G2:I2')

tips = [
    "Add 10% waste for siding",
    "Don't subtract small openings < 10 SF",
    "Measure trim/fascia separately for each edge"
]
for idx, tip in enumerate(tips, start=3):
    cell = ws.cell(row=idx, column=7)
    cell.value = f"• {tip}"
    cell.font = Font(size=9)
    cell.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'G{idx}:I{idx}')

ws.cell(row=6, column=7).value = "📖 Manual: p. 21-23 — Siding"
ws.cell(row=6, column=7).font = Font(italic=True, size=9, color="0000FF")
ws.merge_cells('G6:I6')

# Insert diagram
if 'elevation-siding-areas' in png_files:
    insert_diagram(ws, png_files['elevation-siding-areas'], 'J2',
                  "Elevation Areas — Manual p. 21-23")

# ==========================================
# 6. WINDOWS & DOORS - Step 5
# ==========================================
print("  → Windows & Doors (Step 5)")
ws = wb['Windows & Doors']

# Insert rows
ws.insert_rows(1, 7)

# Step header
step_cell = ws.cell(row=1, column=1)
step_cell.value = "STEP 5 — WINDOWS & DOORS TAKEOFF"
step_cell.font = Font(bold=True, size=14, color="FFFFFF")
step_cell.fill = PatternFill(start_color="FFC000", end_color="FFC000", fill_type="solid")
step_cell.alignment = Alignment(horizontal='center', vertical='center')
ws.merge_cells('A1:H1')
ws.row_dimensions[1].height = 25

# Instructions
ws.cell(row=2, column=1).value = "INSTRUCTIONS:"
ws.cell(row=2, column=1).font = Font(bold=True, size=10)

instructions = [
    "1. Use the window/door schedule FIRST—don't scale from plans",
    "2. Record each unit: ID, size, type, quantity",
    "3. Note special requirements: tempered, impact-rated, shapes",
    "4. Verify counts by cross-checking schedule vs elevations"
]

for idx, instruction in enumerate(instructions, start=3):
    cell = ws.cell(row=idx, column=1)
    cell.value = instruction
    cell.font = Font(size=9)
    cell.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'A{idx}:E{idx}')

# Tips box
ws.cell(row=2, column=6).value = "💡 TIPS"
ws.cell(row=2, column=6).font = Font(bold=True, size=10)
ws.cell(row=2, column=6).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.merge_cells('F2:H2')

tips = [
    "Always use the schedule, not floor plan dimensions",
    "Check for conflicting tags on elevations",
    "Note special glass requirements"
]
for idx, tip in enumerate(tips, start=3):
    cell = ws.cell(row=idx, column=6)
    cell.value = f"• {tip}"
    cell.font = Font(size=9)
    cell.alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'F{idx}:H{idx}')

ws.cell(row=6, column=6).value = "📖 Manual: p. 24-25 — Schedules"
ws.cell(row=6, column=6).font = Font(italic=True, size=9, color="0000FF")
ws.merge_cells('F6:H6')

# Insert diagram
if 'window-door-schedule' in png_files:
    insert_diagram(ws, png_files['window-door-schedule'], 'I2',
                  "Schedule Example — Manual p. 24-25")

# ==========================================
# 7. MATERIAL SUMMARY - Step 6
# ==========================================
print("  → Material Summary (Step 6)")
ws = wb['Material Summary']

# Insert rows
ws.insert_rows(1, 11)

# Step header
step_cell = ws.cell(row=1, column=1)
step_cell.value = "STEP 6 — FINAL MATERIAL SUMMARY (READY TO QUOTE)"
step_cell.font = Font(bold=True, size=14, color="FFFFFF")
step_cell.fill = PatternFill(start_color="C00000", end_color="C00000", fill_type="solid")
step_cell.alignment = Alignment(horizontal='center', vertical='center')
ws.merge_cells('A1:F1')
ws.row_dimensions[1].height = 25

# Completion checklist
ws.cell(row=2, column=1).value = "COMPLETION CHECKLIST:"
ws.cell(row=2, column=1).font = Font(bold=True, size=10)

checklist = [
    "☐ Foundation sheet completed",
    "☐ Wall framing sheet completed",
    "☐ Roof sheet completed",
    "☐ Siding & exterior sheet completed",
    "☐ Windows & doors sheet completed",
    "☐ All assumptions noted for customer/engineer review"
]

for idx, item in enumerate(checklist, start=3):
    cell = ws.cell(row=idx, column=1)
    cell.value = item
    cell.font = Font(size=9)
    ws.merge_cells(f'A{idx}:C{idx}')

ws.cell(row=9, column=1).value = "✅ When complete, this summary is ready to key into the quoting system"
ws.cell(row=9, column=1).font = Font(bold=True, size=10, color="008000")
ws.merge_cells('A9:F9')

ws.cell(row=10, column=1).value = "📖 See Manual: p. 26-27 — Complete Example & Final Checks"
ws.cell(row=10, column=1).font = Font(italic=True, size=9, color="0000FF")
ws.merge_cells('A10:F10')

# ==========================================
# 8. NEW SHEET: Tips & References
# ==========================================
print("  → Creating Tips & References sheet")

# Create new worksheet
if 'Tips & References' in wb.sheetnames:
    del wb['Tips & References']

ws = wb.create_sheet('Tips & References', 0)  # Insert at beginning

# Title
ws.cell(row=1, column=1).value = "📚 TIPS & MANUAL QUICK REFERENCE"
ws.cell(row=1, column=1).font = Font(bold=True, size=16, color="FFFFFF")
ws.cell(row=1, column=1).fill = PatternFill(start_color="203764", end_color="203764", fill_type="solid")
ws.cell(row=1, column=1).alignment = Alignment(horizontal='center', vertical='center')
ws.merge_cells('A1:D1')
ws.row_dimensions[1].height = 30

# Introduction
ws.cell(row=2, column=1).value = "This workbook follows a 7-step process (Steps 0-6). Work through each tab in order."
ws.cell(row=2, column=1).font = Font(size=10)
ws.cell(row=2, column=1).alignment = Alignment(wrap_text=True)
ws.merge_cells('A2:D2')
ws.row_dimensions[2].height = 30

# Reference table header
ws.cell(row=4, column=1).value = "Topic"
ws.cell(row=4, column=1).font = Font(bold=True, size=11)
ws.cell(row=4, column=1).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

ws.cell(row=4, column=2).value = "Excel Sheet"
ws.cell(row=4, column=2).font = Font(bold=True, size=11)
ws.cell(row=4, column=2).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

ws.cell(row=4, column=3).value = "Manual Pages"
ws.cell(row=4, column=3).font = Font(bold=True, size=11)
ws.cell(row=4, column=3).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

ws.cell(row=4, column=4).value = "When to Use"
ws.cell(row=4, column=4).font = Font(bold=True, size=11)
ws.cell(row=4, column=4).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")

# Reference data
references = [
    ("Step 0: Plan Setup & Orientation", "Project Info", "p. 4-7", "FIRST - Verify plan revision and scale"),
    ("Step 1: Foundation & Slab", "Foundation", "p. 8-10", "Measure slab perimeter, beams, footings"),
    ("Step 2: Wall Framing", "Wall Framing", "p. 14-17", "Count studs, plates, headers for all walls"),
    ("Step 3: Roof Takeoff", "Roof Takeoff", "p. 18-20", "Calculate sheathing, shingles, ridge, fascia"),
    ("Step 4: Siding & Exterior", "Siding & Exterior", "p. 21-23", "Measure siding, soffit, trim from elevations"),
    ("Step 5: Windows & Doors", "Windows & Doors", "p. 24-25", "Use schedule to count all openings"),
    ("Step 6: Material Summary", "Material Summary", "p. 26-27", "LAST - Compile all quantities for quote"),
    ("Quick Reference Tables", "Conversion Tables", "p. 9, 19", "Slope factors, stud spacing, waste factors"),
]

for idx, (topic, sheet, pages, when) in enumerate(references, start=5):
    ws.cell(row=idx, column=1).value = topic
    ws.cell(row=idx, column=1).font = Font(size=10)
    
    ws.cell(row=idx, column=2).value = sheet
    ws.cell(row=idx, column=2).font = Font(size=10, color="0000FF")
    
    ws.cell(row=idx, column=3).value = pages
    ws.cell(row=idx, column=3).font = Font(size=10, italic=True)
    
    ws.cell(row=idx, column=4).value = when
    ws.cell(row=idx, column=4).font = Font(size=9)
    ws.cell(row=idx, column=4).alignment = Alignment(wrap_text=True)

# General tips section
current_row = len(references) + 7

ws.cell(row=current_row, column=1).value = "💡 GENERAL TIPS FOR ALL TAKEOFFS"
ws.cell(row=current_row, column=1).font = Font(bold=True, size=12)
ws.cell(row=current_row, column=1).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.merge_cells(f'A{current_row}:D{current_row}')
current_row += 1

general_tips = [
    "✓ Always verify you have the latest plan revision before starting",
    "✓ Document ALL assumptions - write them in the Notes columns",
    "✓ When in doubt, call the builder/architect for clarification",
    "✓ Use the diagrams in this workbook AND the PDF manual together",
    "✓ Double-check your math - review formulas before finalizing",
    "✓ Print a copy of your takeoff and keep it with the quote for reference",
    "✓ A typical residential takeoff takes 3-4 hours - don't rush!",
]

for tip in general_tips:
    ws.cell(row=current_row, column=1).value = tip
    ws.cell(row=current_row, column=1).font = Font(size=10)
    ws.cell(row=current_row, column=1).alignment = Alignment(wrap_text=True)
    ws.merge_cells(f'A{current_row}:D{current_row}')
    ws.row_dimensions[current_row].height = 20
    current_row += 1

# Column widths
ws.column_dimensions['A'].width = 35
ws.column_dimensions['B'].width = 20
ws.column_dimensions['C'].width = 15
ws.column_dimensions['D'].width = 40

# Set print area and page setup for all sheets
for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = False

print("\n💾 Saving upgraded workbook...")

# Save the workbook with error handling
try:
    wb.save(excel_path)
    print(f"✅ Excel workbook upgraded successfully!")
except PermissionError:
    print(f"❌ Error: Could not save file - it may be open in Excel.")
    print(f"   Close the file and try again.")
    sys.exit(1)
except Exception as e:
    print(f"❌ Error saving workbook: {e}")
    sys.exit(1)
print(f"   Location: {excel_path}")
print(f"\n📋 Summary of changes:")
print(f"   • Added step-by-step instructions to all 8 sheets")
print(f"   • Embedded {len(png_files)} diagrams with captions")
print(f"   • Added manual page references throughout")
print(f"   • Created new 'Tips & References' sheet")
print(f"   • Added tips boxes and common mistakes")
print(f"   • Set up print-friendly layouts")
print(f"\n🎯 New salespeople can now work through Steps 0-6 in order!")
