#http://stackoverflow.com/questions/1912434/how-do-i-parse-xml-in-python
#extract data from xml file

from xml.dom import minidom
xmldoc = minidom.parse('isbn.xml')
itemlist = xmldoc.getElementsByTagName('description') 
print "Description :-"
print itemlist[0].childNodes[0].nodeValue
print "-------------"

itemlist = xmldoc.getElementsByTagName('average_rating') 
print "Average Rating :-"
print itemlist[0].childNodes[0].nodeValue
print "-------------"





