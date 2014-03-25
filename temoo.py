#take in isbn number and save xml file for corresponding book
import urllib2


PageSource=urllib2.urlopen("https://www.goodreads.com/book/isbn?isbn=0441172717&key=G0YLe4KJic94J0Bi0zeBQ").read()
text_file = open("Output.xml", "w")
text_file.write("%s" %PageSource)
text_file.close()
