#take in isbn number and save xml file for corresponding book
import urllib2
from xml.dom import minidom
import sys

#ISBN="0441172717"
ISBN=sys.argv[1]
APIKey="X" #Enter your own key here
url="https://www.goodreads.com/book/isbn?isbn="+ISBN+"&key="+APIKey

#PageSource=urllib2.urlopen("https://www.goodreads.com/book/isbn?isbn=0441172717&key=X").read()
PageSource=urllib2.urlopen(url).read()
text_file = open("temp.xml", "w")
text_file.write("%s" %PageSource)
text_file.close()

#now read from xml file and display output

xmldoc = minidom.parse('temp.xml')
itemlist = xmldoc.getElementsByTagName('original_title') 
print "Title :-"
print itemlist[0].childNodes[0].nodeValue
print "-------------"

xmldoc = minidom.parse('temp.xml')
itemlist = xmldoc.getElementsByTagName('description') 
print "Description :-"
print itemlist[0].childNodes[0].nodeValue
print "-------------"

itemlist = xmldoc.getElementsByTagName('average_rating') 
print "Average Rating :-"
print itemlist[0].childNodes[0].nodeValue
print "-------------"





