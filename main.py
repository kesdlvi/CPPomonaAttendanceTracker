import pandas as pd
from openpyxl import load_workbook

# Read the Excel file
df = pd.read_excel("data.xlsx")


# to get cell color
wb = load_workbook("data.xlsx")
ws = wb.active


# checking if cell is green
def did_rsvp(cell):
    return cell.fill.fgColor.rgb == "FF00FF00"
#"00FF0"

# finding a cell location by the name in the cell

def find_cell(val):
    for row in ws.iter_rows(min_row = 1, max_row = 91, min_col = 3, max_col = 3):
        for cell in row: 
            if cell.value == val: 
                return cell
    return None


# Extract the name column
person_column_name = df.columns[2]  # Assuming the third column is at index 2 (0-based index)
person_column_data = df[person_column_name]

# Filter the non-empty cells from both columns
non_empty_third_column = person_column_data.dropna().iloc[:8]


# get green cells first
for cell in non_empty_third_column:
    spec_cel = find_cell(cell)
    if did_rsvp(spec_cel):
        print (cell + " RSVP'ed and attended")
    elif spec_cel == None:
        print("DNE")
    else:
        print(cell + " did not attend")
    

# Print the green cells in the third column


