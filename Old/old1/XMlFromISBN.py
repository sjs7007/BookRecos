#take in isbn number and save xml file for corresponding book
import urllib2

ISBN="0441172717"
APIKey="X" #Enter your own key here
url="https://www.goodreads.com/book/isbn?isbn="+ISBN+"&key="+APIKey

#PageSource=urllib2.urlopen("https://www.goodreads.com/book/isbn?isbn=0441172717&key=X").read()
PageSource=urllib2.urlopen(url).read()
text_file = open("Output.xml", "w")
text_file.write("%s" %PageSource)
text_file.close()
