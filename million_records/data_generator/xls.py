import csv
import openpyxl
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet


def read_xls(xls_filepath: str) -> Workbook:
    return openpyxl.load_workbook(xls_filepath)


def read_sheet(wb: Workbook, sheet_name: str) -> Worksheet:
    return wb.get_sheet_by_name(sheet_name)


def create_xls_from_csv(sheet_name: str, csv_filepath: str, xls_filepath: str):
    wb = Workbook()
    ws = wb.active
    ws.title = sheet_name

    with open(csv_filepath) as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            ws.append(row)

    wb.save(xls_filepath)
