# This script read excel data (no vba, no formula)
# You must change the path, which should be your path for the Str_Wrapper
import xlrd

PATH = r'G:\Vincent\BSCM\ATM\Utilities\Strat_Wrapper.xltm'

class ExcelReader():

    def __init__(self):
        self.active_book = xlrd.open_workbook(PATH)

    def read_cells(self, active_book):
        self.products_dowloader_sheet = self.active_book.sheet_by_index(1)

    def create_liste_parameters(self):
        dict_inputs = {}
        for s in products_dowloader_sheet.nrows:
            dict_inputs.keys()= product_dowloader_sheet.row()
            dict_inputs.values() = product_dowloader_sheet.cell(row,1).value


        self.products_dowloader_sheet.row()

book = xlrd.open_workbook(PATH)
sheet = book.sheet_by_index(1)
cell = sheet.cell(4,2)

import xlrd
import pandas as pd

PATH = r'G:\Vincent\BSCM\ATM\Utilities\Strat_Wrapper.xltm'

active_book = xlrd.open_workbook(PATH)
products_downloader_sheet = self.active_book.sheet_by_index(1)

df_parameter = { 'DL_Param' : pd.Series([1,2,3,4],index=['a','b','c',d]), 'Adv_Param': pd.Series([5,6,7,8], index = ['x','y','z','zz'])}