#!/usr/bin/python
#Passwordlist.txt
#456b7016a916a4b178dd72b947c152b7

import hashlib

print ("""
Persian Hack Team
Code By Mojtaba MobhaM
Email : Kazemimojtaba@live.com
""")

hash = raw_input("Enter Your Hash : ")
filename = raw_input("Enter Passwordlist Name: ")
try :
    file = open(filename,'r')
    for password in file:
        if hash == hashlib.md5(password).hexdigest():
            print ("")
            print "Sucessfully Done : "
            print password
except:
    print ("File Error")





