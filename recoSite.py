# program portion to calculate probability that active user is of same personality types as some other user
#from part6.py
import math #for exponent 
import csv #for reading csb database
import sys #for command line args
import xml.etree.cElementTree as ET #for writing XML

def readDB(allUsers,fileName): 
	for i in range (2,32):
		temp=[]
		with open(fileName, 'rb') as f:
	    		reader = csv.reader(f)
	    		for col in reader:
	        		temp.append(col[i])
	    	allUsers.append(temp)
		#print allUsers[i-2]

allUsers=[]
readDB(allUsers,'BookDB.csv')
#print allUsers

Booklists=['BookName','Asylum','Fire and blood','Twisted sisters','Moth and Spark','Dangerous Illusions','The Black-Eyed Blonde','The ghost runner','Dead silent','Before we met','I forgot to remember','Sixth extinction','Wild Things','Alienated','Annhilation','Flight of the silvers','Influx','Tuesdays with Morrie','The alchemist','The fountainhead','Jonathan Livingston Seagull','Mahashweta','Illusions','One','The sound of letting go','Sherlock Holmes and the Vampires of London']
ISBN=['ISBN','1599907844','0825460131','0451239652','0670015709','1940521645','0805098143','1620403404','1408327562','1620402750','1451685815','0805092994','0451415191','1423170288','0374104093','0399164987','0525953183','0751529818','0061122416','0451191153','0743278909','8126417463','0099427869','0330311735','0670015539','1616552662']
def equation1(x,y): #x=actual rating,y=true rating
	x_y = x - y
	partPersonality = math.exp(-(x_y)*(x_y)/12.5) # 12.5 = 2 sigma^2 where sigma = free parameter
	return partPersonality
answer='Y' #for while loop to rate multiple books
nUsers = 30 #number of users
nReviews = 25 #number of reviews
Final=['FinalRatings','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null']#list of final predicted ratings for active user
currentUser=['ActiveUser','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null','null']
probabilityList = [] #probability that current user is similar to ith user
"""while(answer=='Y'):
print("To proceed further kindly rate the books you've read on a scale of 1-5\n1.Asylum\n2.Fire and blood\n3.Twisted sisters\n4.Moth and Spark\n5.Dangerous Illusions\n6.The Black-Eyed Blonde\n7.the ghost runner\n8.Dead silent\n9.Before we met\n10.I forgot to remember\n11.Sixth extinction\n12.Wild Things\n13.Alienated\n14.Annhilation\n15.Flight of the silvers\n16.Influx\n17.Tuesdays with Morrie\n18.The alchemist\n19.The fountainhead\n20.Jonathan Livingston Seagull\n21.Mahashweta\n22.Illusions\n23.One\n24.The sound of letting go\n25.Sherlock Holmes and the Vampires of London")
num=int(raw_input("Enter a book number"))
print "Enter your rating for book" , num
rating=int(raw_input(""))
	currentUser[num]=rating
	Final[num]=rating
	answer=raw_input("want to rate another book? press Y/N")
print("To proceed further kindly rate the books you've read on a scale of 1-5\n1.Asylum\n2.Fire and blood\n3.Twisted sisters\n4.Moth and Spark\n5.Dangerous Illusions\n6.The Black-Eyed Blonde\n7.the ghost runner\n8.Dead silent\n9.Before we met\n10.I forgot to remember\n11.Sixth extinction\n12.Wild Things\n13.Alienated\n14.Annhilation\n15.Flight of the silvers\n16.Influx\n17.Tuesdays with Morrie\n18.The alchemist\n19.The fountainhead\n20.Jonathan Livingston Seagull\n21.Mahashweta\n22.Illusions\n23.One\n24.The sound of letting go\n25.Sherlock Holmes and the Vampires of London")
"""

countRatings = len(sys.argv)-1 
current = 1
while(current<=countRatings):
	currentUser[int(sys.argv[current])]=sys.argv[current+1]
	Final[int(sys.argv[current])]=sys.argv[current+1]
	current=current+2


for i in range (0,nUsers):
	probabilityList.append(1)
	for j in range (1,nReviews+1): #NOTE : Start from 1 because 1st coloumn has userNumber
		temp = currentUser[j]# current user's rating for jth movie
		# if temp=null,probability list[i]=0 for that
		if (temp!="null"):
			x=float(temp)
			y = float(allUsers[i][j]) #rating of ith user for jth movie
			probabilityList[i] = probabilityList[i] * equation1(x,y)
		
	if(temp!='null'):
		probabilityList[i] = probabilityList[i] * 1.0 /nUsers
	else:
		probabilityList[i] = 0

#print "Just printed PL"
#print probabilityList

#booknumber=int(raw_input("Enter book number for which you want predicted rating"))
for x in range(1,24):
	if currentUser[x]=="null":
	 	booknumber=x
	 	probabilityDistResult=[]
		for i in range (0,5):
			probabilityDistResult.append(0)
			for j in range (0,nUsers):
				x = i+1 # i+1 for rating 1,2,3,4,5 
				y = float(allUsers[j][booknumber]) #assume 3rd movie's rating we are finding out for now
				probabilityDistResult[i] = probabilityDistResult[i] + equation1(x,y) * probabilityList[j]

		temp = probabilityDistResult[0]
		finalRating = 1
		for i in range (1,5):
			if (probabilityDistResult[i]>=temp):
				temp = probabilityDistResult[i]
				finalRating = i+1

		#print "Final rating for book", booknumber, Booklists[booknumber],"with ISBN", ISBN[booknumber]
		Final[booknumber]=finalRating
		#print finalRating
#print("Final Rating : $d" %finalRating)

root = ET.Element("root")
doc = ET.SubElement(root, "books")


print "We recommend the following books :"
for x in range(1,24):
	if int(Final[x])>=4:
		print Booklists[x],", ISBN : ",ISBN[x]
		
		#write to xml

		field = ET.SubElement(doc, "Name")
		field.text = Booklists[x]


		field = ET.SubElement(doc, "ISBN")
		field.text = ISBN[x]


tree = ET.ElementTree(root)
tree.write("pyCreatedXML.xml")

"""
Sample output:-

python recoSite.py 5 2 4 3 2 2 1 1 6 3 7 1 9 1 10 1 11 1 12 1 13 1 14 1 15 1 16 1 17 1 18 1 20 1 21 1
We recommend the following books :
Twisted sisters , ISBN :  0451239652
Dead silent , ISBN :  1408327562
The fountainhead , ISBN :  0451191153
Illusions , ISBN :  0099427869
One , ISBN :  0330311735

"""