#take in isbn number and save xml file for corresponding book
import urllib2
from xml.dom import minidom
import sys

def bookData(ISBN):
	#ISBN="0441172717"
	APIKey="G0YLe4KJic94J0Bi0zeBQ" #Enter your own key here
	url="https://www.goodreads.com/book/isbn?isbn="+ISBN+"&key="+APIKey

	#PageSource=urllib2.urlopen("https://www.goodreads.com/book/isbn?isbn=0441172717&key=X").read()
	PageSource=urllib2.urlopen(url).read()
	text_file = open("Output.xml", "w")
	text_file.write("%s" %PageSource)
	text_file.close()

	#now read from xml file and display output

	output=""
	xmldoc = minidom.parse('Output.xml')
	itemlist = xmldoc.getElementsByTagName('original_title') 
	print "Title :-"
	print itemlist[0].childNodes[0].nodeValue
	print "-------------"
	output=output+itemlist[0].childNodes[0].nodeValue+"\n"

	xmldoc = minidom.parse('Output.xml')
	itemlist = xmldoc.getElementsByTagName('name') 
	print "Author :-"
	print itemlist[0].childNodes[0].nodeValue
	print "-------------"
	output=output+itemlist[0].childNodes[0].nodeValue+"\n"

	xmldoc = minidom.parse('Output.xml')
	itemlist = xmldoc.getElementsByTagName('description') 
	print "Description :-"
	print itemlist[0].childNodes[0].nodeValue
	print "-------------"
	output=output+itemlist[0].childNodes[0].nodeValue+"\n"

	itemlist = xmldoc.getElementsByTagName('average_rating') 
	print "Average Rating on GoodReads :-"
	print itemlist[0].childNodes[0].nodeValue
	print "-------------"
	output=output+itemlist[0].childNodes[0].nodeValue+"\n"

	text_file = open("output.txt", "w")
	text_file.write("%s" %output)
	text_file.close()


bookData("0441172717")