#!/usr/bin/perl

use WWW::Mechanize;						# Include the WWW::Mechanize module

$url = "http://";	# What URL shall we retrieve?

#&mechanize_page;
#&mechanize_links;

sub mechanize_page{
# Create a new instance of WWW::Mechanize enabling autocheck 
# checks each request to ensure it was successful, producing an error if not.
$mechanize = WWW::Mechanize->new(autocheck => 1);

$mechanize->get($url);						# Retrieve the page
$title = $mechanize->title;					# Retrieve the page title
$page = $mechanize->content;#(format => 'text' );		# Assign the page content to $page
}

sub mechanize_links{
@links = $mechanize->links;					# Place all of the links in an array

  foreach $link (@links) {					# Loop through and output each link
    #print $name = $link->name();
    #print $tag = $link->tag();
    #print $base = $link->base();				# Retrieve and print the Base URL to which the links are relative
    $text = $link->text(), ":";					# Retrieve and print the link text
    $href = $link->url(), "\n";					# Retrieve and print the link URL
    print "$text: $href\n";
  }
}
