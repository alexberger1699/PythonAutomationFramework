import os

import openpyxl


def createExcelFile():
    # Load the Excel workbook
    wb = openpyxl.load_workbook('names1.xlsx')

    # Get the active sheet
    sheet = wb.active

    # Create a list of names
    names = ['Alice', 'Bob', 'Charlie']

    # Add the names to the sheet
    for row_num, name in enumerate(names):
        sheet.cell(row=row_num + 1, column=1).value = name

    # Save the workbook
    wb.save('names1.xlsx')



createExcelFile()