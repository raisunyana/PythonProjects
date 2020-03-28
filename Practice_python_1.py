# -*- coding: utf-8 -*-
"""
Created on Tue Dec  5 08:16:12 2017

@author: Arun.r
"""

#program pratice character input#
#take user input of name and age, tell the person when he/she will be 100#

#take nameinput

name =input("Please let me know your name")
print ("Your name is "+name)

# take age input #
age= int(input("Please let me know your age"))

#time to become hundred years
years_to_hun=100-age
hun_year = 2017 + years_to_hun

#print when the person will become hundred years
print (name +"You will become 100 years in " + str(hun_year))

# how many copies you want to print #
copies_num = int(input("How many copies you want for the above message"))
while copies_num>1:
    print (name +"You will become 100 years in " + str(hun_year))
    copies_num=copies_num-1


