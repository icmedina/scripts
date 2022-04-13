# -*- coding: utf-8 -*-
"""
get and change working directory

Created on Fri Jan 29 11:56:49 2021
@author: Sid
"""
# =============================================================================
# Open Directory using file chooser
# =============================================================================
def open_folder_tk():
    from tkinter import Tk, filedialog
    
    root = Tk() # pointing root to Tk() to use it as Tk() in program.
    root.withdraw() # Hides small tkinter window.
    root.attributes('-topmost', True) # Opened windows will be active. above all windows despite of selection.
    
    open_dir = filedialog.askdirectory() # Returns opened path as str
    return open_dir 


def open_file_tk():
    from tkinter import Tk     # from tkinter import Tk for Python 3.x
    from tkinter.filedialog import askopenfilename
    
    Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
    filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
    print(filename)
    return filename 

in_file = open_file_tk()



import os
# =============================================================================
#  Get path to root directory and current directory
# =============================================================================
path = "C:\\Users\\iceb0\OneDrive\\Pictures\\Be a Blessing with your Words"

folder_name = os.path.basename(path)
parent = os.path.dirname(path)
print("Parent directory: %s \nCurrent directory: %s" %(parent,folder_name))

# =============================================================================
#  Get cwd and update working directory
# =============================================================================
def change_dir():
    import os, platform
    
    # Determine system platform
    pf = platform.system()
    print("\n" + pf + " system\n")
    
    cwd = os.getcwd()
    print("Current working directory: \n  {0}".format(cwd))
    
    set_path = input("Enter working directory:")
        
    if (pf == "Windows"):  # Windows platform
        path = set_path.replace("\\", "/")
    elif (pf == "Linux"):  # Linux platform
        path = set_path
    
    os.chdir(path)
    print("\nWorking directory changed to: ", set_path)

change_dir()

# =============================================================================
# create new directory
# =============================================================================
# New Directory 
directory = "new_dir"
# Path 
path = os.path.join(set_path, directory) 

# Create the directory 
os.mkdir(path) 
print("Directory '% s' created" % directory) 
  
# =============================================================================
#  count the number of files and directories
# =============================================================================
def count_dir (path):
    totalDir, totalFiles = 0, 0
    
    for base, dirs, files in os.walk(path):
        print('Directory: ',base)
        for Dir in dirs:
            totalDir += 1
        for File in files:
            totalFiles += 1
            print('  ', File)
    print('\n')
            
    # output the number of directories and files
    if (totalDir <= 1):
        print(totalDir, 'directory')
    else:
        print(totalDir, 'directories')
    if (totalFiles <= 1):
        print(totalFiles, 'file')
    else:
        print(totalFiles, 'files')
            
    print('\nTotal:',(totalDir + totalFiles))
    

# =============================================================================
# var = words
# print("Type: " + str(type(var)), "Length: " + str(len(var)))
# =============================================================================
# Read each file within the subdirectory
# option 2
import os, glob

# read folder containing txt files of data
def read_folder(folder):
    cwd = os.getcwd()
    os.chdir(cwd +'/'+folder)               # go to subdirectory containing data
    files = [f for f in glob.glob("*.csv")] # read csv files
    # print("\n",files)

    ctr = 1
    for file in files:
        text_data = open(file,"rt")
        raw_text = text_data.read()
        ctr=+1
        print ("File: ", ctr, "\n")
        print(raw_text)
        text_data.close()

    os.chdir(cwd)                           # go back to higher directory
    return dfs, files                       # return dataframes from list of files from the subdir

    
# read folder containing csv files of data
def read_folder(folder):
    cwd = os.getcwd()
    os.chdir(cwd +'/'+folder)               # go to subdirectory containing data
    files = [f for f in glob.glob("*.csv")] # read csv files
    print("\n",files)
    dfs = []
    for file in files:
        df = pd.read_csv(file)
        dfs.append(df)
    os.chdir(cwd)                           # go back to higher directory
    return dfs, files                       # return dataframes from list of files from the subdir