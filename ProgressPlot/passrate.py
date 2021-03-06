###########################################
# TITLE: passrate.py
#
# AUTHOR: Marissa Adams (madams@pas.rochester.edu)
#
# EXECUTION: python progressplot.py [file name from Blackboard GradeCenter][.csv]
#
# PURPOSE: This allows you to query about information regarding how many quizzes are being given out, which quizzes per module, and also the prescreen rate per module. One would hope that you have a prescreen rate that is around 1 (for each quiz there is a prescreen). If the rate is much higher than 1, then you may want to instruct the staff to heavily prescreen for students on that particular module based on their history.
#
# NOTES:
# 1. If you would like to add a quiz name, feel free to add another if statement under the counting for quizzes
###########################################

import csv
import sys
import re
import matplotlib.pyplot as plt
import numpy as np

#File I/O for the grade center download                                                                             
grade_center = open(sys.argv[1], 'rt')

#Empty list holds the header                                                                                         
header_lst = [] #Empty list                                                                                          
#Read the csv from grade center                                                                                      
reader = csv.reader(grade_center) #A bunch of rows with data in them                                                 
header = reader.next()

#Finds the module grade columns                                                                                      
version_finder = re.compile("Module 1?[0-9] Version") #Creating a pattern                                            
for i in xrange(len(header)):
    searcher = version_finder.search(header[i])
    if searcher:
        header_lst.append(i)

row_lst = []
num_q = [0] * 12
num_r = [0] * 12

for row in reader:
    row_lst.append(row)
grade_center.close()

c_q = 0

# Looping through all quiz types and counts how many of each name
for i in header_lst:
    for row in row_lst:
        if "a" in row[i].lower():
           num_q[c_q] += 1
        if "b" in row[i].lower():
            num_q[c_q] += 1
        if "c" in row[i].lower():
            num_q[c_q] += 1
        if "d" in row[i].lower():
            num_q[c_q] += 1
        if "e" in row[i].lower():
            num_q[c_q] += 1
        if "f" in row[i].lower():
            num_q[c_q] += 1
#        if "n" in row[i].lower():
#            num_q[c_q] += 1
    c_q += 1
    
c_r = 0

#Counts the number of prescreens
for i in header_lst:
    for row in row_lst:
        if "r" in row[i].lower():
            num_r[c_r]+= 1
    c_r += 1

print "Number of Quizzes Given Each Module: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] = ",num_q
print "Total Number of Quizzes Given According to Blackboard: ",sum(num_q)
print "% of Module 1 Quizzes: ", float(num_q[0])/sum(num_q)*100
print "% of Module 2 Quizzes: ", float(num_q[1])/sum(num_q)*100
print "% of Module 3 Quizzes: ", float(num_q[2])/sum(num_q)*100
print "% of Module 4 Quizzes: ", float(num_q[3])/sum(num_q)*100
print "% of Module 5 Quizzes: ", float(num_q[4])/sum(num_q)*100
print "% of Module 6 Quizzes: ", float(num_q[5])/sum(num_q)*100
print "% of Module 7 Quizzes: ", float(num_q[6])/sum(num_q)*100
print "% of Module 8 Quizzes: ", float(num_q[7])/sum(num_q)*100
print "% of Module 9 Quizzes: ", float(num_q[8])/sum(num_q)*100
print "% of Module 10 Quizzes: ", float(num_q[9])/sum(num_q)*100
print "% of Module 11 Quizzes: ", float(num_q[10])/sum(num_q)*100
print "% of Module 12 Quizzes: ", float(num_q[11])/sum(num_q)*100
print "Total number of Prescreens per Module:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12] = ", num_r
print "Total Number of Prescreens: ", sum(num_r)
print "Module 1: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[0])/float(num_r[0])
print "Module 2: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[1])/float(num_r[1])
print "Module 3: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[2])/float(num_r[2])
print "Module 4: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[3])/float(num_r[3])
print "Module 5: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[4])/float(num_r[4])
print "Module 6: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[5])/float(num_r[5])
print "Module 7: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[6])/float(num_r[6])
print "Module 8: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[7])/float(num_r[7])
print "Module 9: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[8])/float(num_r[8])
print "Module 10: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[9])/float(num_r[9])
print "Module 11: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[10])/float(num_r[10])
print "Module 12: Number of Quizzes Given/Number of Prescreens Given: ",float(num_q[11])/float(num_r[11])
