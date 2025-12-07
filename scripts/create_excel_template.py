#!/usr/bin/env python3
"""
Blueprint Takeoff Workbook Excel Template Generator
Creates a comprehensive Excel workbook with formulas for residential blueprint takeoffs
"""

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

def create_blueprint_workbook():
    """Create the complete blueprint takeoff workbook"""
    wb = Workbook()
    
    # Remove default sheet
    if 'Sheet' in wb.sheetnames:
        wb.remove(wb['Sheet'])
    
    # Create all worksheets
    create_project_info_sheet(wb)
    create_wall_framing_sheet(wb)
    create_roof_sheet(wb)
    create_foundation_sheet(wb)
    create_siding_sheet(wb)
    create_window_door_sheet(wb)
    create_material_summary_sheet(wb)
    create_conversion_tables_sheet(wb)
    
    # Save the workbook
    wb.save('/home/runner/work/blueprint/blueprint/templates/worksheet.xlsx')
    print("Excel workbook created successfully!")

def create_project_info_sheet(wb):
    """Create project information sheet"""
    ws = wb.create_sheet("Project Info", 0)
    
    # Header styling
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    header_font = Font(color="FFFFFF", bold=True, size=14)
    
    # Title
    ws['A1'] = "BLUEPRINT TAKEOFF WORKSHEET"
    ws['A1'].font = Font(bold=True, size=18)
    ws.merge_cells('A1:F1')
    
    # Project information section
    ws['A3'] = "PROJECT INFORMATION"
    ws['A3'].font = Font(bold=True, size=12, color="4472C4")
    
    labels = [
        ("A4", "Project Name:", "B4"),
        ("A5", "Job Number:", "B5"),
        ("A6", "Builder/Customer:", "B6"),
        ("A7", "Address:", "B7"),
        ("A8", "Plan Set Date:", "B8"),
        ("A9", "Revision Number:", "B9"),
        ("A10", "Takeoff By:", "B10"),
        ("A11", "Date Completed:", "B11"),
        ("A12", "Checked By:", "B12"),
    ]
    
    for label_cell, label_text, value_cell in labels:
        ws[label_cell] = label_text
        ws[label_cell].font = Font(bold=True)
        ws[value_cell].fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
    
    # Building specifications
    ws['A14'] = "BUILDING SPECIFICATIONS"
    ws['A14'].font = Font(bold=True, size=12, color="4472C4")
    
    specs = [
        ("A15", "Building Type:", "B15"),
        ("A16", "Stories:", "B16"),
        ("A17", "Foundation Type:", "B17"),
        ("A18", "Roof Type:", "B18"),
        ("A19", "Total Square Footage:", "B19"),
        ("A20", "Wall Height:", "B20"),
    ]
    
    for label_cell, label_text, value_cell in specs:
        ws[label_cell] = label_text
        ws[label_cell].font = Font(bold=True)
        ws[value_cell].fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
    
    # Regional notes for Southeast Texas
    ws['A22'] = "REGIONAL NOTES (Southeast Texas)"
    ws['A22'].font = Font(bold=True, size=12, color="4472C4")
    
    ws['A23'] = "• Slab foundations are standard (high water table)"
    ws['A24'] = "• Consider humidity-resistant materials"
    ws['A25'] = "• Windstorm requirements (hurricane zone)"
    ws['A26'] = "• Treated lumber required for bottom plates"
    ws['A27'] = "• Additional anchor bolts per wind code"
    
    # Set column widths
    ws.column_dimensions['A'].width = 25
    ws.column_dimensions['B'].width = 30
    
def create_wall_framing_sheet(wb):
    """Create wall framing calculator sheet"""
    ws = wb.create_sheet("Wall Framing")
    
    # Header
    ws['A1'] = "WALL FRAMING TAKEOFF"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:M1')
    
    # Column headers
    headers = ['Wall ID', 'Location', 'Length (ft)', 'Height (ft)', 'Stud Spacing', 
               'Base Studs', 'Corner Adds', 'Opening Adj', 'Total Studs', 
               'Bottom Plate LF', 'Top Plate LF', 'Header Notes', 'Treated?']
    
    header_fill = PatternFill(start_color="70AD47", end_color="70AD47", fill_type="solid")
    header_font = Font(color="FFFFFF", bold=True)
    
    for col, header in enumerate(headers, start=1):
        cell = ws.cell(row=3, column=col)
        cell.value = header
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center', vertical='center')
    
    # Add formulas for first 20 rows
    for row in range(4, 24):
        # Base studs formula: =(Length / Spacing) + 1
        ws[f'F{row}'] = f'=IF(C{row}="","",INT(C{row}*12/16)+1)'
        
        # Total studs: Base + Corner + Opening
        ws[f'I{row}'] = f'=IF(F{row}="","",F{row}+G{row}+H{row})'
        
        # Bottom plate LF: Length
        ws[f'J{row}'] = f'=IF(C{row}="","",C{row})'
        
        # Top plate LF: Length * 2 (double top plate)
        ws[f'K{row}'] = f'=IF(C{row}="","",C{row}*2)'
    
    # Totals row
    total_row = 24
    ws[f'A{total_row}'] = "TOTALS"
    ws[f'A{total_row}'].font = Font(bold=True)
    ws[f'I{total_row}'] = f'=SUM(I4:I23)'
    ws[f'J{total_row}'] = f'=SUM(J4:J23)'
    ws[f'K{total_row}'] = f'=SUM(K4:K23)'
    
    for col in ['I', 'J', 'K']:
        ws[f'{col}{total_row}'].font = Font(bold=True)
        ws[f'{col}{total_row}'].fill = PatternFill(start_color="FFD966", end_color="FFD966", fill_type="solid")
    
    # Instructions
    ws['A26'] = "INSTRUCTIONS:"
    ws['A26'].font = Font(bold=True, color="4472C4")
    ws['A27'] = "1. Enter wall length in feet (e.g., 24)"
    ws['A28'] = "2. Enter wall height in feet (e.g., 8)"
    ws['A29'] = "3. Stud spacing: 16 or 24 (16 is most common)"
    ws['A30'] = "4. Corner Adds: +2 for exterior corners, +1 for T-intersections"
    ws['A31'] = "5. Opening Adj: Count king/jack studs minus displaced studs"
    
    # Set column widths
    for col in range(1, 14):
        ws.column_dimensions[get_column_letter(col)].width = 12
    
def create_roof_sheet(wb):
    """Create roof takeoff calculator sheet"""
    ws = wb.create_sheet("Roof Takeoff")
    
    # Header
    ws['A1'] = "ROOF TAKEOFF CALCULATOR"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:K1')
    
    # Slope factor reference table
    ws['A3'] = "SLOPE FACTORS (Reference)"
    ws['A3'].font = Font(bold=True, color="4472C4")
    
    slope_data = [
        ("Pitch", "Factor"),
        ("4:12", 1.054),
        ("5:12", 1.083),
        ("6:12", 1.118),
        ("7:12", 1.158),
        ("8:12", 1.202),
        ("9:12", 1.250),
        ("10:12", 1.302),
        ("12:12", 1.414),
    ]
    
    for row, (pitch, factor) in enumerate(slope_data, start=4):
        ws[f'A{row}'] = pitch
        ws[f'B{row}'] = factor
        if row == 4:
            ws[f'A{row}'].font = Font(bold=True)
            ws[f'B{row}'].font = Font(bold=True)
    
    # Main calculation table
    ws['D3'] = "ROOF PLANE CALCULATIONS"
    ws['D3'].font = Font(bold=True, size=12, color="4472C4")
    
    headers = ['Plane ID', 'Length (ft)', 'Width (ft)', 'Pitch', 'Slope Factor', 
               'Horiz Area (SF)', 'Surface Area (SF)', 'Sheathing Sheets', 'Waste %', 'Total Sheets', 'Bundles']
    
    header_fill = PatternFill(start_color="5B9BD5", end_color="5B9BD5", fill_type="solid")
    
    for col, header in enumerate(headers, start=4):
        cell = ws.cell(row=4, column=col)
        cell.value = header
        cell.fill = header_fill
        cell.font = Font(color="FFFFFF", bold=True)
        cell.alignment = Alignment(horizontal='center', wrap_text=True)
    
    # Add formulas for calculation rows
    for row in range(5, 15):
        # Horizontal area: Length * Width
        ws[f'I{row}'] = f'=IF(E{row}="","",E{row}*F{row})'
        
        # Surface area: Horizontal * Slope Factor
        ws[f'J{row}'] = f'=IF(I{row}="","",I{row}*H{row})'
        
        # Sheathing sheets: Surface Area / 32 (4x8 sheet = 32 SF)
        ws[f'K{row}'] = f'=IF(J{row}="","",J{row}/32)'
        
        # Total with waste
        ws[f'M{row}'] = f'=IF(K{row}="","",ROUNDUP(K{row}*(1+L{row}/100),0))'
        
        # Bundles: Sheets / 3 bundles per square (100 SF)
        ws[f'N{row}'] = f'=IF(J{row}="","",ROUNDUP(J{row}/100*3,0))'
    
    # Totals
    ws['D16'] = "TOTALS"
    ws['D16'].font = Font(bold=True)
    ws['J16'] = '=SUM(J5:J15)'
    ws['K16'] = '=SUM(K5:K15)'
    ws['M16'] = '=SUM(M5:M15)'
    ws['N16'] = '=SUM(N5:N15)'
    
    for col in ['J', 'K', 'M', 'N']:
        ws[f'{col}16'].font = Font(bold=True)
        ws[f'{col}16'].fill = PatternFill(start_color="FFD966", end_color="FFD966", fill_type="solid")
    
    # Notes
    ws['D18'] = "NOTES:"
    ws['D18'].font = Font(bold=True, color="4472C4")
    ws['D19'] = "• One 4x8 sheet = 32 square feet"
    ws['D20'] = "• Typical waste factor: 10-15% for cuts and starter"
    ws['D21'] = "• Shingles: 3 bundles = 1 square (100 SF)"
    ws['D22'] = "• Hip and ridge cap: Add 10% to total bundles"
    
    # Set column widths
    ws.column_dimensions['A'].width = 10
    ws.column_dimensions['B'].width = 10
    for col in range(4, 15):
        ws.column_dimensions[get_column_letter(col)].width = 12

def create_foundation_sheet(wb):
    """Create foundation/concrete calculator sheet"""
    ws = wb.create_sheet("Foundation")
    
    # Header
    ws['A1'] = "FOUNDATION & CONCRETE TAKEOFF"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:H1')
    
    # Slab section
    ws['A3'] = "SLAB CALCULATIONS"
    ws['A3'].font = Font(bold=True, size=12, color="4472C4")
    
    headers = ['Element', 'Length (ft)', 'Width (ft)', 'Thickness (in)', 'Cu Ft', 'Cu Yd', 'Notes']
    
    for col, header in enumerate(headers, start=1):
        cell = ws.cell(row=4, column=col)
        cell.value = header
        cell.fill = PatternFill(start_color="A5A5A5", end_color="A5A5A5", fill_type="solid")
        cell.font = Font(color="FFFFFF", bold=True)
    
    # Add slab rows with formulas
    for row in range(5, 10):
        # Cu Ft: Length * Width * (Thickness/12)
        ws[f'E{row}'] = f'=IF(B{row}="","",B{row}*C{row}*(D{row}/12))'
        # Cu Yd: Cu Ft / 27
        ws[f'F{row}'] = f'=IF(E{row}="","",E{row}/27)'
    
    # Perimeter footing section
    ws['A11'] = "PERIMETER FOOTING"
    ws['A11'].font = Font(bold=True, size=12, color="4472C4")
    
    footing_headers = ['Location', 'Length (ft)', 'Width (in)', 'Depth (in)', 'Cu Ft', 'Cu Yd', 'Rebar LF']
    
    for col, header in enumerate(footing_headers, start=1):
        cell = ws.cell(row=12, column=col)
        cell.value = header
        cell.fill = PatternFill(start_color="A5A5A5", end_color="A5A5A5", fill_type="solid")
        cell.font = Font(color="FFFFFF", bold=True)
    
    for row in range(13, 18):
        # Cu Ft: Length * (Width/12) * (Depth/12)
        ws[f'E{row}'] = f'=IF(B{row}="","",B{row}*(C{row}/12)*(D{row}/12))'
        # Cu Yd
        ws[f'F{row}'] = f'=IF(E{row}="","",E{row}/27)'
        # Rebar LF: Same as length (typically 2 runs)
        ws[f'G{row}'] = f'=IF(B{row}="","",B{row}*2)'
    
    # Totals
    ws['A19'] = "TOTAL CONCRETE"
    ws['A19'].font = Font(bold=True)
    ws['F19'] = '=SUM(F5:F9,F13:F18)'
    ws['F19'].font = Font(bold=True)
    ws['F19'].fill = PatternFill(start_color="FFD966", end_color="FFD966", fill_type="solid")
    
    ws['A20'] = "TOTAL REBAR"
    ws['A20'].font = Font(bold=True)
    ws['G20'] = '=SUM(G13:G18)'
    ws['G20'].font = Font(bold=True)
    ws['G20'].fill = PatternFill(start_color="FFD966", end_color="FFD966", fill_type="solid")
    
    # Instructions
    ws['A22'] = "CONVERSION FACTORS:"
    ws['A22'].font = Font(bold=True, color="4472C4")
    ws['A23'] = "• 1 cubic yard = 27 cubic feet"
    ws['A24'] = "• Add 5-10% waste for concrete"
    ws['A25'] = "• Standard slab thickness: 4 inches"
    ws['A26'] = "• Perimeter footing: typically 16\" wide x 12\" deep minimum"
    ws['A27'] = "• Southeast Texas: All bottom plates must be treated lumber"
    
    for col in range(1, 9):
        ws.column_dimensions[get_column_letter(col)].width = 14

def create_siding_sheet(wb):
    """Create siding/exterior materials calculator sheet"""
    ws = wb.create_sheet("Siding & Exterior")
    
    # Header
    ws['A1'] = "SIDING & EXTERIOR MATERIALS TAKEOFF"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:K1')
    
    # Main calculation table
    headers = ['Elevation', 'Width (ft)', 'Plate Ht (ft)', 'Gable Rise (ft)', 
               'Wall Area', 'Gable Area', 'Gross SF', 'Openings SF', 'Net SF', 'Waste %', 'Order SF']
    
    header_fill = PatternFill(start_color="C65911", end_color="C65911", fill_type="solid")
    
    for col, header in enumerate(headers, start=1):
        cell = ws.cell(row=3, column=col)
        cell.value = header
        cell.fill = header_fill
        cell.font = Font(color="FFFFFF", bold=True)
        cell.alignment = Alignment(horizontal='center', wrap_text=True)
    
    # Add formulas
    for row in range(4, 14):
        # Wall Area: Width * Plate Height
        ws[f'E{row}'] = f'=IF(B{row}="","",B{row}*C{row})'
        
        # Gable Area: (Width * Rise) / 2
        ws[f'F{row}'] = f'=IF(D{row}="","",B{row}*D{row}/2)'
        
        # Gross SF: Wall + Gable
        ws[f'G{row}'] = f'=IF(E{row}="","",E{row}+F{row})'
        
        # Net SF: Gross - Openings
        ws[f'I{row}'] = f'=IF(G{row}="","",G{row}-H{row})'
        
        # Order SF: Net * (1 + Waste%)
        ws[f'K{row}'] = f'=IF(I{row}="","",I{row}*(1+J{row}/100))'
    
    # Totals
    ws['A15'] = "TOTALS"
    ws['A15'].font = Font(bold=True)
    
    for col in ['G', 'H', 'I', 'K']:
        ws[f'{col}15'] = f'=SUM({col}4:{col}14)'
        ws[f'{col}15'].font = Font(bold=True)
        ws[f'{col}15'].fill = PatternFill(start_color="FFD966", end_color="FFD966", fill_type="solid")
    
    # Squares calculation
    ws['A17'] = "TOTAL SQUARES (÷100)"
    ws['A17'].font = Font(bold=True)
    ws['K17'] = '=K15/100'
    ws['K17'].font = Font(bold=True)
    ws['K17'].number_format = '0.00'
    
    # Trim section
    ws['A19'] = "TRIM & ACCESSORIES"
    ws['A19'].font = Font(bold=True, size=12, color="4472C4")
    
    trim_items = [
        ("A20", "Corner Trim:", "B20", "pieces"),
        ("A21", "J-Channel:", "B21", "LF"),
        ("A22", "Fascia:", "B22", "LF"),
        ("A23", "Soffit:", "B23", "SF"),
        ("A24", "Frieze Board:", "B24", "LF"),
    ]
    
    for label_cell, label, value_cell, unit_text in trim_items:
        ws[label_cell] = label
        ws[label_cell].font = Font(bold=True)
        ws[f'{value_cell[0]}{int(value_cell[1])+1}'] = unit_text
    
    # Notes
    ws['A26'] = "NOTES:"
    ws['A26'].font = Font(bold=True, color="4472C4")
    ws['A27'] = "• Typical waste: 10% for vinyl siding, 15% for lap siding"
    ws['A28'] = "• Deduct 50% for windows, 100% for doors (or calculate exact)"
    ws['A29'] = "• Southeast Texas: Consider hurricane-rated fasteners"
    ws['A30'] = "• Order J-channel for all openings and transitions"
    
    for col in range(1, 12):
        ws.column_dimensions[get_column_letter(col)].width = 12

def create_window_door_sheet(wb):
    """Create window and door schedule sheet"""
    ws = wb.create_sheet("Windows & Doors")
    
    # Header
    ws['A1'] = "WINDOW & DOOR SCHEDULE"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:H1')
    
    # Window section
    ws['A3'] = "WINDOWS"
    ws['A3'].font = Font(bold=True, size=12, color="4472C4")
    
    headers = ['Tag', 'Qty', 'Size (WxH)', 'Rough Opening', 'Header Size', 'Type/Material', 'Remarks', 'Unit Price']
    
    header_fill = PatternFill(start_color="4472C4", end_color="4472C4", fill_type="solid")
    
    for col, header in enumerate(headers, start=1):
        cell = ws.cell(row=4, column=col)
        cell.value = header
        cell.fill = header_fill
        cell.font = Font(color="FFFFFF", bold=True)
    
    # Add 15 window rows
    for row in range(5, 20):
        ws[f'H{row}'].number_format = '$#,##0.00'
    
    # Door section
    ws['A21'] = "DOORS"
    ws['A21'].font = Font(bold=True, size=12, color="4472C4")
    
    for col, header in enumerate(headers, start=1):
        cell = ws.cell(row=22, column=col)
        cell.value = header
        cell.fill = PatternFill(start_color="C65911", end_color="C65911", fill_type="solid")
        cell.font = Font(color="FFFFFF", bold=True)
    
    # Add 15 door rows
    for row in range(23, 38):
        ws[f'H{row}'].number_format = '$#,##0.00'
    
    # Summary
    ws['A39'] = "TOTALS"
    ws['A39'].font = Font(bold=True)
    ws['G39'] = "Window Count:"
    ws['H39'] = '=SUM(B5:B19)'
    ws['G40'] = "Door Count:"
    ws['H40'] = '=SUM(B23:B37)'
    
    for col in range(1, 9):
        ws.column_dimensions[get_column_letter(col)].width = 15

def create_material_summary_sheet(wb):
    """Create final material summary sheet"""
    ws = wb.create_sheet("Material Summary")
    
    # Header
    ws['A1'] = "MATERIAL SUMMARY - READY TO QUOTE"
    ws['A1'].font = Font(bold=True, size=16)
    ws.merge_cells('A1:F1')
    
    # Project info reference
    ws['A3'] = "Project:"
    ws['B3'] = "='Project Info'!B4"
    ws['A4'] = "Job Number:"
    ws['B4'] = "='Project Info'!B5"
    
    # Material categories
    categories = [
        ("FRAMING LUMBER", 6, [
            ("2x4x8 Studs", "EA"),
            ("2x6x8 Studs", "EA"),
            ("2x4 Plates (Treated)", "LF"),
            ("2x6 Plates (Treated)", "LF"),
            ("2x4 Top Plates", "LF"),
            ("2x6 Top Plates", "LF"),
            ("2x6 Headers", "LF"),
            ("2x8 Headers", "LF"),
            ("2x10 Headers", "LF"),
            ("2x12 Headers", "LF"),
        ]),
        ("ROOF MATERIALS", 18, [
            ("7/16\" OSB Sheathing", "Sheets"),
            ("Shingles (Architectural)", "Bundles"),
            ("Hip & Ridge Cap", "Bundles"),
            ("Starter Strip", "LF"),
            ("Drip Edge", "LF"),
            ("Felt/Underlayment", "Rolls"),
        ]),
        ("FOUNDATION", 26, [
            ("Concrete 3000 PSI", "CY"),
            ("#3 Rebar", "LF"),
            ("#4 Rebar", "LF"),
            ("6mil Vapor Barrier", "SF"),
            ("Anchor Bolts", "EA"),
        ]),
        ("EXTERIOR FINISHES", 33, [
            ("Siding", "Squares"),
            ("J-Channel", "LF"),
            ("Corner Trim", "EA"),
            ("Fascia", "LF"),
            ("Soffit", "SF"),
        ]),
    ]
    
    header_fill = PatternFill(start_color="203864", end_color="203864", fill_type="solid")
    item_fill = PatternFill(start_color="E7E6E6", end_color="E7E6E6", fill_type="solid")
    
    current_row = 6
    
    for category_name, start_row, items in categories:
        # Category header
        ws[f'A{current_row}'] = category_name
        ws[f'A{current_row}'].font = Font(bold=True, size=12, color="FFFFFF")
        ws[f'A{current_row}'].fill = header_fill
        ws.merge_cells(f'A{current_row}:F{current_row}')
        current_row += 1
        
        # Column headers
        ws[f'A{current_row}'] = "Description"
        ws[f'B{current_row}'] = "Unit"
        ws[f'C{current_row}'] = "Quantity"
        ws[f'D{current_row}'] = "Unit Price"
        ws[f'E{current_row}'] = "Extended"
        ws[f'F{current_row}'] = "Notes"
        
        for col in ['A', 'B', 'C', 'D', 'E', 'F']:
            ws[f'{col}{current_row}'].font = Font(bold=True)
            ws[f'{col}{current_row}'].fill = PatternFill(start_color="D9D9D9", end_color="D9D9D9", fill_type="solid")
        current_row += 1
        
        # Items
        for item, unit in items:
            ws[f'A{current_row}'] = item
            ws[f'B{current_row}'] = unit
            ws[f'C{current_row}'].fill = item_fill
            ws[f'D{current_row}'].number_format = '$#,##0.00'
            ws[f'E{current_row}'] = f'=C{current_row}*D{current_row}'
            ws[f'E{current_row}'].number_format = '$#,##0.00'
            current_row += 1
        
        current_row += 1
    
    # Grand total
    ws[f'D{current_row}'] = "GRAND TOTAL:"
    ws[f'D{current_row}'].font = Font(bold=True, size=12)
    ws[f'E{current_row}'].font = Font(bold=True, size=12)
    ws[f'E{current_row}'].fill = PatternFill(start_color="FFD966", end_color="FFD966", fill_type="solid")
    ws[f'E{current_row}'].number_format = '$#,##0.00'
    
    # Set column widths
    ws.column_dimensions['A'].width = 30
    ws.column_dimensions['B'].width = 10
    ws.column_dimensions['C'].width = 12
    ws.column_dimensions['D'].width = 12
    ws.column_dimensions['E'].width = 15
    ws.column_dimensions['F'].width = 25

def create_conversion_tables_sheet(wb):
    """Create reference conversion tables sheet"""
    ws = wb.create_sheet("Conversion Tables")
    
    # Header
    ws['A1'] = "QUICK REFERENCE - CONVERSION TABLES"
    ws['A1'].font = Font(bold=True, size=14)
    ws.merge_cells('A1:D1')
    
    # Stud spacing table
    ws['A3'] = "STUD SPACING MULTIPLIERS"
    ws['A3'].font = Font(bold=True, color="4472C4")
    
    stud_data = [
        ("Spacing", "Studs per LF", "Formula"),
        ("12\" O.C.", "1.00", "LF × 1 + 1"),
        ("16\" O.C.", "0.75", "LF × 0.75 + 1"),
        ("24\" O.C.", "0.50", "LF × 0.5 + 1"),
    ]
    
    for row, data in enumerate(stud_data, start=4):
        for col, value in enumerate(data, start=1):
            ws.cell(row=row, column=col, value=value)
            if row == 4:
                ws.cell(row=row, column=col).font = Font(bold=True)
    
    # Roof slope factors
    ws['A9'] = "ROOF SLOPE FACTORS"
    ws['A9'].font = Font(bold=True, color="4472C4")
    
    slope_data = [
        ("Pitch", "Degrees", "Slope Factor", "Rise per ft"),
        ("3:12", "14.0°", "1.031", "3\""),
        ("4:12", "18.4°", "1.054", "4\""),
        ("5:12", "22.6°", "1.083", "5\""),
        ("6:12", "26.6°", "1.118", "6\""),
        ("7:12", "30.3°", "1.158", "7\""),
        ("8:12", "33.7°", "1.202", "8\""),
        ("9:12", "36.9°", "1.250", "9\""),
        ("10:12", "39.8°", "1.302", "10\""),
        ("12:12", "45.0°", "1.414", "12\""),
    ]
    
    for row, data in enumerate(slope_data, start=10):
        for col, value in enumerate(data, start=1):
            ws.cell(row=row, column=col, value=value)
            if row == 10:
                ws.cell(row=row, column=col).font = Font(bold=True)
    
    # Board feet conversions
    ws['F3'] = "BOARD FEET CONVERSIONS"
    ws['F3'].font = Font(bold=True, color="4472C4")
    
    bf_data = [
        ("Size", "BF per LF"),
        ("2x4", "0.667"),
        ("2x6", "1.000"),
        ("2x8", "1.333"),
        ("2x10", "1.667"),
        ("2x12", "2.000"),
    ]
    
    for row, data in enumerate(bf_data, start=4):
        for col, value in enumerate(data, start=6):
            ws.cell(row=row, column=col, value=value)
            if row == 4:
                ws.cell(row=row, column=col).font = Font(bold=True)
    
    # Area conversions
    ws['F10'] = "AREA & VOLUME CONVERSIONS"
    ws['F10'].font = Font(bold=True, color="4472C4")
    
    area_data = [
        ("1 Square", "= 100 SF"),
        ("1 Sheet (4x8)", "= 32 SF"),
        ("1 Cubic Yard", "= 27 CF"),
        ("1 Ton", "= 2000 lbs"),
    ]
    
    for row, data in enumerate(area_data, start=11):
        ws[f'F{row}'] = data[0]
        ws[f'G{row}'] = data[1]
        ws[f'F{row}'].font = Font(bold=True)
    
    # Waste factors
    ws['A21'] = "TYPICAL WASTE FACTORS"
    ws['A21'].font = Font(bold=True, color="4472C4")
    
    waste_data = [
        ("Material", "Waste %", "Notes"),
        ("Framing Lumber", "5-10%", "More for complex cuts"),
        ("Sheathing/Subfloor", "10%", "Standard"),
        ("Roof Shingles", "10-15%", "Add for hips/valleys"),
        ("Vinyl Siding", "10%", "Standard"),
        ("Lap Siding", "15%", "More cuts required"),
        ("Concrete", "5-10%", "Spillage and leveling"),
        ("Drywall", "10-15%", "Standard"),
    ]
    
    for row, data in enumerate(waste_data, start=22):
        for col, value in enumerate(data, start=1):
            ws.cell(row=row, column=col, value=value)
            if row == 22:
                ws.cell(row=row, column=col).font = Font(bold=True)
    
    # Set column widths
    for col in range(1, 8):
        ws.column_dimensions[get_column_letter(col)].width = 18

if __name__ == "__main__":
    create_blueprint_workbook()
