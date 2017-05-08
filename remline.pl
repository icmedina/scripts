#!/usr/bin/perl

# A program that removes newline from a textfile copied from a pdf.
# 2009

#print "\nType the filename you want to process: ";
#$inputfile = <STDIN>;
# open(INPUT,$inputfile);

  open(INPUT,'files\in.txt');
  @data=<INPUT>;
  close(INPUT);

  &remline;

sub remline{
#print "\nType the output filename: ";
#$outputfile = <STDIN>;
#open(FILE, ">$outputfile");
$line_len = 45;

open(FILE, '>files\out.txt');
    chomp($line_data);
    foreach $line_data(@data){
     #for scientific journals
         if ((length($line_data) > $line_len) &&($line_data =~ /\n/)){
			$line_data =~ s/\n/ /;
			$line_data =~ s/\.\d+,\d+/\./;
			$line_data =~ s/\.\d+/\./;
 			}
			
         if (length($line_data) < $line_len){
            $line_data =~ s/\n/\n\n/;
			$line_data =~ s/\.\d+,\d+/\./;
			$line_data =~ s/\.\d+/\./;
			}
			
            print FILE $line_data;
			print $line_data;
    }
print FILE "\n\n";
close(FILE);
}
