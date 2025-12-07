#!/usr/bin/env python3
"""
Regenerate Excel workbook as Field Takeoff Pack WITHOUT merged cells.
Uses only borders, fills, fonts, and column widths for formatting.
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

# Create temp directory
os.makedirs(temp_dir, exist_ok=True)

def convert_svg_to_png(svg_path, png_path, width=350):
    """Convert SVG to PNG"""
    try:
        subprocess.run([
            'rsvg-convert',
            '-w', str(width),
            svg_path,
            '-o', png_path
        ], check=True, capture_output=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            import cairosvg
            cairosvg.svg2png(url=svg_path, write_to=png_path, output_width=width)
            return True
        except ImportError:
            print(f"Warning: Could not convert {svg_path} - install librsvg2-bin or cairosvg")
            return False

def insert_diagram(ws, png_path, cell_ref):
    """Insert diagram image WITHOUT placing it in merged cells"""
    if not os.path.exists(png_path):
        return False
    
    try:
        img = XLImage(png_path)
        # Resize appropriately
        target_width = 280
        if img.width > 0:
            scale = target_width / img.width
            img.width = target_width
            img.height = int(img.height * scale)
        ws.add_image(img, cell_ref)
        return True
    except Exception as e:
        print(f"  Warning: Could not insert {png_path}: {e}")
        return False

print("🔧 Regenerating Excel Workbook without merged cells...")

# Load workbook
if not os.path.exists(excel_path):
    print(f"Error: {excel_path} not found")
    print("Run create_excel_template.py first")
    sys.exit(1)

wb = load_workbook(excel_path)
print(f"✓ Loaded workbook")

# Convert SVG diagrams to PNG
diagrams = {
    'plan-orientation': 'plan-orientation.svg',
    'foundation-plan-section': 'foundation-plan-section.svg',
    'wall-framing-section': 'wall-framing-section.svg',
    'roof-plan-and-section': 'roof-plan-and-section.svg',
    'elevation-siding-areas': 'elevation-siding-areas.svg',
    'window-door-schedule': 'window-door-schedule.svg',
}

png_files = {}
for key, svg_file in diagrams.items():
    svg_path = os.path.join(img_dir, svg_file)
    if not os.path.exists(svg_path):
        print(f"⚠ Warning: {svg_path} not found")
        continue
    
    png_path = os.path.join(temp_dir, f'{key}.png')
    if convert_svg_to_png(svg_path, png_path):
        png_files[key] = png_path
        print(f"✓ Converted {svg_file}")

print("\n📝 Upgrading worksheets (NO MERGED CELLS)...")

# Remove any existing merged cells from all sheets
for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    # Get list of merged cell ranges
    merged_ranges = list(ws.merged_cells.ranges)
    # Unmerge all
    for merged_range in merged_ranges:
        ws.unmerge_cells(str(merged_range))
    print(f"  → Unmerged {len(merged_ranges)} cell ranges from '{sheet_name}'")

# Common styles
header_font = Font(bold=True, size=14, color="FFFFFF")
subheader_font = Font(bold=True, size=11)
instruction_font = Font(size=9)
tip_font = Font(size=9)
ref_font = Font(italic=True, size=9, color="0000FF")

thin_border = Border(
    left=Side(style='thin'),
    right=Side(style='thin'),
    top=Side(style='thin'),
    bottom=Side(style='thin')
)

# ==========================================
# 1. PROJECT INFO - Step 0
# ==========================================
print("\n  → Project Info (Step 0)")
ws = wb['Project Info']
ws.insert_rows(1, 10)

# Step header (NO MERGE - just make column A wide)
ws.cell(row=1, column=1).value = "STEP 0 — PLAN SETUP & ORIENTATION"
ws.cell(row=1, column=1).font = header_font
ws.cell(row=1, column=1).fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
ws.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')
ws.row_dimensions[1].height = 25
ws.column_dimensions['A'].width = 60

# Instructions
ws.cell(row=3, column=1).value = "INSTRUCTIONS:"
ws.cell(row=3, column=1).font = subheader_font

ws.cell(row=4, column=1).value = "1. Verify you have the LATEST REVISION of the plan set"
ws.cell(row=4, column=1).font = instruction_font

ws.cell(row=5, column=1).value = "2. Check the scale on the title block (usually 1/4\" = 1'-0\")"
ws.cell(row=5, column=1).font = instruction_font

ws.cell(row=6, column=1).value = "3. Verify scale by measuring a known dimension with your scale ruler"
ws.cell(row=6, column=1).font = instruction_font

ws.cell(row=7, column=1).value = "4. Note any addenda, alternates, or special conditions"
ws.cell(row=7, column=1).font = instruction_font

ws.cell(row=8, column=1).value = "5. Fill in project information below before proceeding to Step 1"
ws.cell(row=8, column=1).font = instruction_font

# Checklist
ws.cell(row=4, column=2).value = "☐ Latest revision confirmed"
ws.cell(row=4, column=2).font = instruction_font
ws.column_dimensions['B'].width = 30

ws.cell(row=5, column=2).value = "☐ Scale verified"
ws.cell(row=5, column=2).font = instruction_font

ws.cell(row=6, column=2).value = "☐ Windstorm/code notes checked"
ws.cell(row=6, column=2).font = instruction_font

# Manual reference
ws.cell(row=9, column=1).value = "📖 See Manual: p. 4-7 — Getting Started & Plan Orientation"
ws.cell(row=9, column=1).font = ref_font

# Insert diagram to the right (column D)
if 'plan-orientation' in png_files:
    insert_diagram(ws, png_files['plan-orientation'], 'D3')
    ws.cell(row=3, column=4).value = "Plan Orientation Diagram"
    ws.cell(row=3, column=4).font = Font(italic=True, size=9)
    ws.column_dimensions['D'].width = 35

# ==========================================
# 2. FOUNDATION - Step 1
# ==========================================
print("  → Foundation (Step 1)")
ws = wb['Foundation']
ws.insert_rows(1, 9)

# Step header
ws.cell(row=1, column=1).value = "STEP 1 — FOUNDATION & SLAB TAKEOFF"
ws.cell(row=1, column=1).font = header_font
ws.cell(row=1, column=1).fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
ws.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')
ws.row_dimensions[1].height = 25
ws.column_dimensions['A'].width = 50

# Instructions
ws.cell(row=3, column=1).value = "INSTRUCTIONS:"
ws.cell(row=3, column=1).font = subheader_font

ws.cell(row=4, column=1).value = "1. Locate foundation/structural sheets in the plan set"
ws.cell(row=4, column=1).font = instruction_font

ws.cell(row=5, column=1).value = "2. Trace the perimeter of the slab and any interior beams"
ws.cell(row=5, column=1).font = instruction_font

ws.cell(row=6, column=1).value = "3. Measure each segment and enter lengths in the table below"
ws.cell(row=6, column=1).font = instruction_font

ws.cell(row=7, column=1).value = "4. Record slab thickness, beam sizes, and notes/assumptions"
ws.cell(row=7, column=1).font = instruction_font

# Tips (column B)
ws.cell(row=3, column=2).value = "💡 TIPS:"
ws.cell(row=3, column=2).font = subheader_font
ws.cell(row=3, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.column_dimensions['B'].width = 40

ws.cell(row=4, column=2).value = "• Include porches and garage slabs"
ws.cell(row=4, column=2).font = tip_font
ws.cell(row=4, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=5, column=2).value = "• Note any assumed beam sizes for review"
ws.cell(row=5, column=2).font = tip_font
ws.cell(row=5, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=6, column=2).value = "• Remember to convert thickness to feet"
ws.cell(row=6, column=2).font = tip_font
ws.cell(row=6, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=7, column=2).value = "📖 Manual: p. 8-10 — Foundation"
ws.cell(row=7, column=2).font = ref_font
ws.cell(row=7, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

# Insert diagram
if 'foundation-plan-section' in png_files:
    insert_diagram(ws, png_files['foundation-plan-section'], 'D3')
    ws.cell(row=3, column=4).value = "Foundation Section Diagram"
    ws.cell(row=3, column=4).font = Font(italic=True, size=9)
    ws.column_dimensions['D'].width = 35

# ==========================================
# 3. WALL FRAMING - Step 2
# ==========================================
print("  → Wall Framing (Step 2)")
ws = wb['Wall Framing']
ws.insert_rows(1, 9)

# Step header
ws.cell(row=1, column=1).value = "STEP 2 — WALL FRAMING TAKEOFF"
ws.cell(row=1, column=1).font = header_font
ws.cell(row=1, column=1).fill = PatternFill(start_color="ED7D31", end_color="ED7D31", fill_type="solid")
ws.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')
ws.row_dimensions[1].height = 25
ws.column_dimensions['A'].width = 50

# Instructions
ws.cell(row=3, column=1).value = "INSTRUCTIONS:"
ws.cell(row=3, column=1).font = subheader_font

ws.cell(row=4, column=1).value = "1. Highlight all exterior walls on the floor plan"
ws.cell(row=4, column=1).font = instruction_font

ws.cell(row=5, column=1).value = "2. Label walls W1, W2, W3... moving clockwise from front left"
ws.cell(row=5, column=1).font = instruction_font

ws.cell(row=6, column=1).value = "3. Measure each wall and enter: length, height, stud spacing"
ws.cell(row=6, column=1).font = instruction_font

ws.cell(row=7, column=1).value = "4. Count corners, tees, and openings (windows/doors)"
ws.cell(row=7, column=1).font = instruction_font

# Tips
ws.cell(row=3, column=2).value = "💡 TIPS:"
ws.cell(row=3, column=2).font = subheader_font
ws.cell(row=3, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.column_dimensions['B'].width = 40

ws.cell(row=4, column=2).value = "• Add extra studs for corners (3) and tees (2)"
ws.cell(row=4, column=2).font = tip_font
ws.cell(row=4, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=5, column=2).value = "• Use header schedule for kings/jacks—don't guess"
ws.cell(row=5, column=2).font = tip_font
ws.cell(row=5, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=6, column=2).value = "• Remember the '+1' in stud count formula"
ws.cell(row=6, column=2).font = tip_font
ws.cell(row=6, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=7, column=2).value = "📖 Manual: p. 14-17 — Wall Framing"
ws.cell(row=7, column=2).font = ref_font
ws.cell(row=7, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

# Insert diagram
if 'wall-framing-section' in png_files:
    insert_diagram(ws, png_files['wall-framing-section'], 'N3')
    ws.cell(row=3, column=14).value = "Wall Section Diagram"
    ws.cell(row=3, column=14).font = Font(italic=True, size=9)
    ws.column_dimensions['N'].width = 35

# ==========================================
# 4. ROOF TAKEOFF - Step 3
# ==========================================
print("  → Roof Takeoff (Step 3)")
ws = wb['Roof Takeoff']
ws.insert_rows(1, 9)

# Step header
ws.cell(row=1, column=1).value = "STEP 3 — ROOF TAKEOFF"
ws.cell(row=1, column=1).font = header_font
ws.cell(row=1, column=1).fill = PatternFill(start_color="5B9BD5", end_color="5B9BD5", fill_type="solid")
ws.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')
ws.row_dimensions[1].height = 25
ws.column_dimensions['A'].width = 50

# Instructions
ws.cell(row=3, column=1).value = "INSTRUCTIONS:"
ws.cell(row=3, column=1).font = subheader_font

ws.cell(row=4, column=1).value = "1. Locate roof plan and framing details"
ws.cell(row=4, column=1).font = instruction_font

ws.cell(row=5, column=1).value = "2. For each roof plane, record: width, length, pitch, overhang"
ws.cell(row=5, column=1).font = instruction_font

ws.cell(row=6, column=1).value = "3. Use slope factor table to calculate sheathing area"
ws.cell(row=6, column=1).font = instruction_font

ws.cell(row=7, column=1).value = "4. Remember: porch and garage roofs count too!"
ws.cell(row=7, column=1).font = instruction_font

# Tips
ws.cell(row=3, column=2).value = "💡 TIPS:"
ws.cell(row=3, column=2).font = subheader_font
ws.cell(row=3, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.column_dimensions['B'].width = 40

ws.cell(row=4, column=2).value = "• Include overhangs in width/length for sheathing"
ws.cell(row=4, column=2).font = tip_font
ws.cell(row=4, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=5, column=2).value = "• Don't forget porch and garage roofs"
ws.cell(row=5, column=2).font = tip_font
ws.cell(row=5, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=6, column=2).value = "• Add 10-15% waste for shingles"
ws.cell(row=6, column=2).font = tip_font
ws.cell(row=6, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=7, column=2).value = "📖 Manual: p. 18-20 — Roof Takeoff"
ws.cell(row=7, column=2).font = ref_font
ws.cell(row=7, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

# Insert diagram
if 'roof-plan-and-section' in png_files:
    insert_diagram(ws, png_files['roof-plan-and-section'], 'P3')
    ws.cell(row=3, column=16).value = "Roof Plan & Pitch Diagram"
    ws.cell(row=3, column=16).font = Font(italic=True, size=9)
    ws.column_dimensions['P'].width = 35

# ==========================================
# 5. SIDING & EXTERIOR - Step 4
# ==========================================
print("  → Siding & Exterior (Step 4)")
ws = wb['Siding & Exterior']
ws.insert_rows(1, 9)

# Step header
ws.cell(row=1, column=1).value = "STEP 4 — SIDING, SOFFIT, FASCIA & EXTERIOR TRIM"
ws.cell(row=1, column=1).font = header_font
ws.cell(row=1, column=1).fill = PatternFill(start_color="A5A5A5", end_color="A5A5A5", fill_type="solid")
ws.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')
ws.row_dimensions[1].height = 25
ws.column_dimensions['A'].width = 50

# Instructions
ws.cell(row=3, column=1).value = "INSTRUCTIONS:"
ws.cell(row=3, column=1).font = subheader_font

ws.cell(row=4, column=1).value = "1. Use each elevation (Front, Rear, Left, Right)"
ws.cell(row=4, column=1).font = instruction_font

ws.cell(row=5, column=1).value = "2. Measure wall width, height, and gable rise if applicable"
ws.cell(row=5, column=1).font = instruction_font

ws.cell(row=6, column=1).value = "3. Subtract windows/doors based on siding type"
ws.cell(row=6, column=1).font = instruction_font

ws.cell(row=7, column=1).value = "4. Calculate linear feet for trim, fascia, soffit"
ws.cell(row=7, column=1).font = instruction_font

# Tips
ws.cell(row=3, column=2).value = "💡 TIPS:"
ws.cell(row=3, column=2).font = subheader_font
ws.cell(row=3, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.column_dimensions['B'].width = 40

ws.cell(row=4, column=2).value = "• Add 10% waste for siding"
ws.cell(row=4, column=2).font = tip_font
ws.cell(row=4, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=5, column=2).value = "• Don't subtract small openings < 10 SF"
ws.cell(row=5, column=2).font = tip_font
ws.cell(row=5, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=6, column=2).value = "• Measure trim/fascia separately for each edge"
ws.cell(row=6, column=2).font = tip_font
ws.cell(row=6, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=7, column=2).value = "📖 Manual: p. 21-23 — Siding"
ws.cell(row=7, column=2).font = ref_font
ws.cell(row=7, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

# Insert diagram
if 'elevation-siding-areas' in png_files:
    insert_diagram(ws, png_files['elevation-siding-areas'], 'L3')
    ws.cell(row=3, column=12).value = "Elevation Areas Diagram"
    ws.cell(row=3, column=12).font = Font(italic=True, size=9)
    ws.column_dimensions['L'].width = 35

# ==========================================
# 6. WINDOWS & DOORS - Step 5
# ==========================================
print("  → Windows & Doors (Step 5)")
ws = wb['Windows & Doors']
ws.insert_rows(1, 9)

# Step header
ws.cell(row=1, column=1).value = "STEP 5 — WINDOWS & DOORS TAKEOFF"
ws.cell(row=1, column=1).font = header_font
ws.cell(row=1, column=1).fill = PatternFill(start_color="FFC000", end_color="FFC000", fill_type="solid")
ws.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')
ws.row_dimensions[1].height = 25
ws.column_dimensions['A'].width = 50

# Instructions
ws.cell(row=3, column=1).value = "INSTRUCTIONS:"
ws.cell(row=3, column=1).font = subheader_font

ws.cell(row=4, column=1).value = "1. Use the window/door schedule FIRST—don't scale from plans"
ws.cell(row=4, column=1).font = instruction_font

ws.cell(row=5, column=1).value = "2. Record each unit: ID, size, type, quantity"
ws.cell(row=5, column=1).font = instruction_font

ws.cell(row=6, column=1).value = "3. Note special requirements: tempered, impact-rated, shapes"
ws.cell(row=6, column=1).font = instruction_font

ws.cell(row=7, column=1).value = "4. Verify counts by cross-checking schedule vs elevations"
ws.cell(row=7, column=1).font = instruction_font

# Tips
ws.cell(row=3, column=2).value = "💡 TIPS:"
ws.cell(row=3, column=2).font = subheader_font
ws.cell(row=3, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
ws.column_dimensions['B'].width = 40

ws.cell(row=4, column=2).value = "• Always use the schedule, not floor plan dimensions"
ws.cell(row=4, column=2).font = tip_font
ws.cell(row=4, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=5, column=2).value = "• Check for conflicting tags on elevations"
ws.cell(row=5, column=2).font = tip_font
ws.cell(row=5, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=6, column=2).value = "• Note special glass requirements"
ws.cell(row=6, column=2).font = tip_font
ws.cell(row=6, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

ws.cell(row=7, column=2).value = "📖 Manual: p. 24-25 — Schedules"
ws.cell(row=7, column=2).font = ref_font
ws.cell(row=7, column=2).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")

# Insert diagram
if 'window-door-schedule' in png_files:
    insert_diagram(ws, png_files['window-door-schedule'], 'J3')
    ws.cell(row=3, column=10).value = "Schedule Example Diagram"
    ws.cell(row=3, column=10).font = Font(italic=True, size=9)
    ws.column_dimensions['J'].width = 35

# ==========================================
# 7. MATERIAL SUMMARY - Step 6
# ==========================================
print("  → Material Summary (Step 6)")
ws = wb['Material Summary']
ws.insert_rows(1, 12)

# Step header
ws.cell(row=1, column=1).value = "STEP 6 — FINAL MATERIAL SUMMARY (READY TO QUOTE)"
ws.cell(row=1, column=1).font = header_font
ws.cell(row=1, column=1).fill = PatternFill(start_color="C00000", end_color="C00000", fill_type="solid")
ws.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')
ws.row_dimensions[1].height = 25
ws.column_dimensions['A'].width = 60

# Completion checklist
ws.cell(row=3, column=1).value = "COMPLETION CHECKLIST:"
ws.cell(row=3, column=1).font = subheader_font

ws.cell(row=4, column=1).value = "☐ Foundation sheet completed"
ws.cell(row=4, column=1).font = instruction_font

ws.cell(row=5, column=1).value = "☐ Wall framing sheet completed"
ws.cell(row=5, column=1).font = instruction_font

ws.cell(row=6, column=1).value = "☐ Roof sheet completed"
ws.cell(row=6, column=1).font = instruction_font

ws.cell(row=7, column=1).value = "☐ Siding & exterior sheet completed"
ws.cell(row=7, column=1).font = instruction_font

ws.cell(row=8, column=1).value = "☐ Windows & doors sheet completed"
ws.cell(row=8, column=1).font = instruction_font

ws.cell(row=9, column=1).value = "☐ All assumptions noted for customer/engineer review"
ws.cell(row=9, column=1).font = instruction_font

ws.cell(row=11, column=1).value = "✅ When complete, this summary is ready to key into the quoting system"
ws.cell(row=11, column=1).font = Font(bold=True, size=10, color="008000")

ws.cell(row=12, column=1).value = "📖 See Manual: p. 26-27 — Complete Example & Final Checks"
ws.cell(row=12, column=1).font = ref_font

# ==========================================
# 8. TIPS & REFERENCES SHEET
# ==========================================
print("  → Creating Tips & References sheet")

if 'Tips & References' in wb.sheetnames:
    del wb['Tips & References']

ws = wb.create_sheet('Tips & References', 0)

# Title
ws.cell(row=1, column=1).value = "📚 BLUEPRINT TAKEOFF - TIPS & MANUAL QUICK REFERENCE"
ws.cell(row=1, column=1).font = Font(bold=True, size=14, color="FFFFFF")
ws.cell(row=1, column=1).fill = PatternFill(start_color="203764", end_color="203764", fill_type="solid")
ws.cell(row=1, column=1).alignment = Alignment(horizontal='left', vertical='center')
ws.row_dimensions[1].height = 30
ws.column_dimensions['A'].width = 50

# Introduction
ws.cell(row=2, column=1).value = "This workbook follows a 7-step process (Steps 0-6). Work through each tab in order."
ws.cell(row=2, column=1).font = Font(size=10)
ws.cell(row=2, column=1).alignment = Alignment(wrap_text=True)
ws.row_dimensions[2].height = 30

# Table header
ws.cell(row=4, column=1).value = "Step & Topic"
ws.cell(row=4, column=1).font = Font(bold=True, size=11)
ws.cell(row=4, column=1).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
ws.cell(row=4, column=1).border = thin_border

ws.cell(row=4, column=2).value = "Excel Sheet"
ws.cell(row=4, column=2).font = Font(bold=True, size=11)
ws.cell(row=4, column=2).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
ws.cell(row=4, column=2).border = thin_border
ws.column_dimensions['B'].width = 20

ws.cell(row=4, column=3).value = "Manual Pages"
ws.cell(row=4, column=3).font = Font(bold=True, size=11)
ws.cell(row=4, column=3).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
ws.cell(row=4, column=3).border = thin_border
ws.column_dimensions['C'].width = 15

ws.cell(row=4, column=4).value = "When to Use"
ws.cell(row=4, column=4).font = Font(bold=True, size=11)
ws.cell(row=4, column=4).fill = PatternFill(start_color="D9E1F2", end_color="D9E1F2", fill_type="solid")
ws.cell(row=4, column=4).border = thin_border
ws.column_dimensions['D'].width = 45

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
    ws.cell(row=idx, column=1).border = thin_border
    ws.cell(row=idx, column=1).alignment = Alignment(wrap_text=True)
    
    ws.cell(row=idx, column=2).value = sheet
    ws.cell(row=idx, column=2).font = Font(size=10, color="0000FF")
    ws.cell(row=idx, column=2).border = thin_border
    
    ws.cell(row=idx, column=3).value = pages
    ws.cell(row=idx, column=3).font = Font(size=10, italic=True)
    ws.cell(row=idx, column=3).border = thin_border
    
    ws.cell(row=idx, column=4).value = when
    ws.cell(row=idx, column=4).font = Font(size=9)
    ws.cell(row=idx, column=4).alignment = Alignment(wrap_text=True)
    ws.cell(row=idx, column=4).border = thin_border

# General tips section
current_row = len(references) + 7

ws.cell(row=current_row, column=1).value = "💡 GENERAL TIPS FOR ALL TAKEOFFS"
ws.cell(row=current_row, column=1).font = Font(bold=True, size=12)
ws.cell(row=current_row, column=1).fill = PatternFill(start_color="FFF2CC", end_color="FFF2CC", fill_type="solid")
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
    ws.row_dimensions[current_row].height = 20
    current_row += 1

# Set print area and page setup for all sheets
for sheet_name in wb.sheetnames:
    ws = wb[sheet_name]
    ws.page_setup.orientation = ws.ORIENTATION_LANDSCAPE
    ws.page_setup.paperSize = ws.PAPERSIZE_LETTER
    ws.page_setup.fitToWidth = 1
    ws.page_setup.fitToHeight = False

print("\n💾 Saving workbook...")

try:
    wb.save(excel_path)
    print(f"✅ Workbook saved successfully (NO MERGED CELLS)")
    print(f"   Location: {excel_path}")
except Exception as e:
    print(f"❌ Error saving: {e}")
    sys.exit(1)

print(f"\n📋 Summary:")
print(f"   • Removed ALL merged cells from entire workbook")
print(f"   • Added step-by-step instructions to 8 sheets")
print(f"   • Embedded {len(png_files)} diagrams")
print(f"   • Added manual page references")
print(f"   • Created 'Tips & References' sheet")
print(f"   • All formatting uses borders, fills, and column widths only")
print(f"\n✅ Excel file should now open without errors!")
