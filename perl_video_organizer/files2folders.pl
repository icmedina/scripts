#!/usr/bin/perl -w

use strict;
use File::Find;					# required module to delete empty directories
use POSIX qw(strftime);				# required module toe get the localtime

#  ICMedina Jr.  : Transfer video files (mp4, mkv or avi) into folders according to release year 
#    Script Name : files2folders.pl
#    Version     : 1
#    Release     : August 2015
#    OS Support  : Linux, Mac OSX, FreeBSD or any system with perl
#  IO
#    $input	: directory path 
#    $output	: organized folder and a log file 

my @files = &list_files;
&create_folder (@files);
my @folders = &list_folders;

open (LOGFILE,">>log.txt");
foreach my $folder (@folders) {chop ($folder);	# chop removes the "/" after the folder name
  foreach my $file (@files){
	if ($file =~ m/$folder/){		# check if the year in the filename matches the directory
	print "\nMoving \"$file\" to $folder... "; print LOGFILE "\nMoving \"$file\" to $folder... ";
  	system "mv $file $folder";		# move the files in the directory
	
	# get the local time
	my $datestring = strftime "%b %e, %Y %H:%M:%S", localtime;
	printf "done. \t$datestring";
	printf LOGFILE "done. \t$datestring";
	}
  }
} close LOGFILE;

# CREATE FOLDER ACCORDING THE LIST OF AVAILABLE FILES
sub create_folder { my @files = @_;
  foreach my $file (@files){
     if ($file =~ m/(\d{4})/){
	my ($year) = $file =~ m/(\d{4})/;	# check the release year in the filename then assigns it to a variable
     	mkdir("$year");# || die ("Cannot create directory");
     }else {
     	mkdir("Unclassified");
     }
  }  
}

# CREATE LIST OF FILES IN THE CURRENT DIRECTORY
sub list_files { 
  my @mp4_list = glob "*.mp4"; 			# list all the mp4 files
  my @mkv_list = glob "*.mkv"; 			# list all the mkv files
  my @avi_list = glob "*.avi"; 			# list all the avi files
  my @files_list =(@mp4_list,@mkv_list,@avi_list);
  return @files_list;
}

# CREATE LIST OF FOLDERS IN THE CURRENT DIRECTORY
sub list_folders {
  my @folders_list = glob "*/"; 		# list all the folder names
  return @folders_list ;
}

finddepth(sub{rmdir},'.')			# delete empty directories
