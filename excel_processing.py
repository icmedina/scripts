# -*- coding: utf-8 -*-
"""
open excel by extension
load and open sheets
Save csv file to output directory
Save xls file to output directory

Created on Thu Jan 28 1:30:09 2021
@author: Sid
"""
# requires: pip install xlrd
# requires: pip install openpyxl

import os 
import pandas as pd

# =============================================================================
#  function to check filetype and open the file
# =============================================================================
def file2df(in_file):
    # a script that runs read file based on file extension
    if in_file.endswith('.csv'):
        df = pd.read_csv(in_file)
        """
        read_csv(filepath_or_buffer, sep=', ', delimiter=None, header='infer', names=None, index_col=None, ....)
        Read a csv file to a dataframe with multiple delimiters in regular expression
        usersDf =  pd.read_csv('file.csv',  sep='[:,|_]', engine='python')
        """
    elif in_file.endswith('.xls') | in_file.endswith('.xlsx'):
        df = pd.ExcelFile(in_file)
    #elif in_file.endswith('.xlsx'):
    #    file = pd.read_excel(in_file, engine='openpyxl')
    
    return df
# =============================================================================
# function to get the available sheets within the worksheet
# =============================================================================
def get_sheets(file):
    # determine sheets within the file
    print("\n\nAvailable sheet(s): '%s'" % file.sheet_names)
    sheetname = input("\nSpecify the sheet name to open: ")
    
    # Load selected sheet
    df = pd.read_excel(file, sheet_name=sheetname)
    print("Selected sheet: ", sheetname)        
    return df
    
    # =============================================================================
    # Load Multiple Sheets
    # df_sheet_multi = pd.read_excel('sample.xlsx', sheet_name=[0, 'sheet2'])
    # 
    # print(df_sheet_multi)
    # =============================================================================
    
    # =============================================================================
    # Load all sheets
    # If sheet_name argument is none, all sheets are read.
    # 
    # df_sheet_all = pd.read_excel('sample.xlsx', sheet_name=None)
    # print(df_sheet_all)
    # =============================================================================
    
    # determine columns within the excel sheet
    col_name = input("\nAvailable column(s): '%s'"% df.columns+ "\nSelect column name: ")
    
    # extract column and save to list
    col_sel = df[col_name]
        
    return col_sel

# =============================================================================
# Create output directory
# ============================================================================= 
# in_file = input("\nInput file (with extension): ")
in_file = open_file_tk()

file_exist = os.path.isfile(in_file)  # check if file exist

# process input file if exists
if file_exist:
    df = file2df(in_file)
    col_sel = get_sheets(df)
    print (col_sel)
    
    # Create output directory
    print("\nSpecify/ Create output directory: ")
    dir_out = input()
    dir_exist = os.path.isdir(dir_out)  # check if dir exist
    
    if dir_exist:
        print("Directory '% s' already exist!" % dir_out) 
    else:
        os.mkdir(dir_out) 
        print("Directory '% s' is created!" % dir_out) 
else:
    print("File '% s' does not exist!" % in_file)

# =============================================================================
# Save csv file to output directory
# =============================================================================
# output parameters
output = 'output'
file_ext = '.csv'
dir_out = 'out' 

# save output file
output_file = output + file_ext
output_file = dir_out + '/' +  out_file
print("\nOutput path and text file: " + output_file)

with open(output_file, "w") as f:      # options: a - append; w - write 
    print(out_file, file=f)

# save DataFrame as a CSV file without the index
csv_data = df2.to_csv(output_file, index = False)
print('\nCSV String:\n', csv_data)
# =============================================================================
# Save xls to output directory
# =============================================================================
# output parameters
output = 'output'
file_ext = '.xls'
dir_out = 'out' 

# save output file
out_file = output + file_ext
output_file = dir_out + '/' +  out_file

# save DataFrame as a xls file without the index
import xlwt
from xlwt import Workbook
  
# Workbook is created
wb = Workbook()
  
# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
  
sheet1.write(:, :, 'ISBT DEHRADUN')
sheet1.write(2, 0, 'SHASTRADHARA')
sheet1.write(3, 0, 'CLEMEN TOWN')
sheet1.write(4, 0, 'RAJPUR ROAD')
sheet1.write(5, 0, 'CLOCK TOWER')
  
wb.save(output_file)