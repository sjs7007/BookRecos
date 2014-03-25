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





