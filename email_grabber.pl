#!/usr/bin/perl
print "\nThis program parses addresses from forwarded emails.\nBeware!!!\n";
print "\nType the filename you want to process: ";
$inputfile = <STDIN>;
  open(INPUT,$inputfile);
    $new=<INPUT>; @data=<INPUT>;
  close(INPUT);
&sort_email;
&outfile;

sub sort_email{
  open(FILE, '>email_temp');
    foreach $line_data(@data) {
    if ($line_data =~ /\@/g) {
      $line_data =~ s/\,/\n/g;
      $line_data =~ s/\:\s/\n/g;
      $line_data =~ s/\;\s//g;
      $line_data =~ s/\s\</\,/g;
        $line_data =~ s/\"//g;
      $line_data =~ s/\>/\n/g;}
    print FILE $line_data;}
  close(FILE);
}
sub outfile{
  open(OUTPUT, 'email_temp');
    @out=<OUTPUT>;
  close(INPUT);
  
  open(OUT, '>mail.csv');
  print OUT "NAME\,E-MAIL\n";
    foreach $line_out(@out) {
    if ($line_out =~ /\@/g) {}
        else{
      $line_out =~ s/$line_out//g;}
    print OUT $line_out;}
  close(OUT);
}