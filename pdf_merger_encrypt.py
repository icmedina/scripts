#!/usr/bin/python3

# A python script that reads subdirectories then combines several pdfs from each subdirectory in one pdf file using pdftk
# The output files are also encrypted using pdftk
# This script is used to combine several pdf files from an optical scanner into a single documen 
# Dependency: pdftk

# Author: Isidro Medina Jr.
# Date: Feb 28, 2016

import os, glob, shutil, subprocess

mypassword = "password"											# set the desired password

all_subdirs = [d for d in os.listdir('.') if os.path.isdir(d)]	# get the list of subdirectories in the current directory
path = os.path.expanduser('/home/user/Documents/DIR')		# set the working directory
j=0																# file counter
for subdir in  all_subdirs:
	print ("Merging files within ", subdir,"folder.")
	outfile = '.'.join([subdir, 'pdf'])							# name the output file based on the folder name by concatenating the subdirectory name with 'pdf'
	os.chdir (subdir)											# go to the subdirectory
	files = []													# declare an empty list of files
	for file in glob.glob("*.pdf"):								# get the list of pdf files within the subdirectory
		files.append(file)										# insert the pdf files into files array
		files.sort()											# sort the filenames alphabetically
	command = ['pdftk','cat', 'output', outfile, 'user_pw', mypassword]
	i=1
	for pdf in files:
		command.insert(i,pdf)									# insert the input files at position i in the command arguments
		i += 1													# increment the position 
	subprocess.call(command)									# call the pdftk with arguments from python
	os.chdir (os.pardir)										# go back to the parent directory
	dest = os.path.join(path, outfile)							# set the destination directory (parent directory)
	src = os.path.join(path,subdir, outfile)					# set the source directory (subdirectory)
	print ("Moving ", outfile, "to the parent directory...", end='')
	shutil.move(src, dest)										# move the file from subdirectory to parent directory
	print (" Done!")
	j += 1													# increment file counter
print ("\n",j,"files successfully created.")	
print ("Thank you for using the pdf merger script. \n\nTO GOD BE THE GLORY!\n")
