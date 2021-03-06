###########################################
## TITLE: progressplot.py
#
## AUTHOR: Marissa Adams (madams@pas.rochester.edu)
#
## EXECUTION: python progressplot.py [file name from Blackboard GradeCenter][.csv] [Module #] [Values Col] [Grade Col]
#
## PURPOSE: Takes the grade center .csv file from Blackboard and spits out a histogram. This histogram charts the students progress in a Mastery-Self-Paced Physics course. Students are binned based on the current module they have passed. Special cases are Module 0 (Haven't started) and the last module. Also yields the exact number on the histogram, and total number of students. Also provides information of who is on what module given the module preference of the user.
#
# NOTES:
# 1. To edit the number of modules for a given class (say changing from 12 to 13: you need to amend the pertainent info for the histogram at the bottom and add or take away a 0 from grade_lst
###########################################

import csv
import sys
import re
import matplotlib.pyplot as plt
import numpy as np

#File I/O for the grade center download
grade_center = open(sys.argv[1], 'rt')

#Cheap way to extract the date
date = sys.argv[1][46:-13]

selected_mod = int(sys.argv[2])
selected_cols_min = int(sys.argv[3])
selected_cols_max = int(sys.argv[4])

#Empty list holds the header
header_lst = [] #Empty list

#Read the csv from grade center
reader = csv.reader(grade_center) #A bunch of rows with data in them
header = reader.next()

#Finds the module grade columns
module_finder = re.compile("Module 1?[0-9] Grade") #Creating a pattern
for i in xrange(len(header)): 
    searcher = module_finder.search(header[i])
    if searcher:
        header_lst.append(i)

#A list that holds the grades... then spits the values if_pass into the histogram
grade_lst = [0,0,0,0,0,0,0,0,0,0,0,0,0]
hist_lst = []

#But first we need to determine what module is the highest for the students
for row in reader:
    current_mod=(0, 0, row)
    for i in xrange(len(header_lst)):
        #Grades are entered like 100.00, need to convert
        try:
            variable = int(float(row[header_lst[i]]))
        except ValueError:
            variable = 0

        if 90 <= variable <= 100:
            current_mod=(i+1 ,variable, row)

    grade_lst[current_mod[0]] += 1
    hist_lst.append(current_mod[0])
    if current_mod[0] == selected_mod:
        current_mod[2][3] += "@u.rochester.edu" 
        print current_mod[2][0:4], current_mod[2][selected_cols_min:selected_cols_max]

#Total Number of Students
TSSum = sum(grade_lst)

print "TOTAL # OF STUDENTS: ", TSSum

print "VALUES ON HISTOGRAM"
print "( Module #, # of Students Passed )"
for i in xrange(len(grade_lst)):
    print "(",i,",",grade_lst[i],")"

#Calculating the CoM of the class (Average) & STD
CoM = np.mean(hist_lst)
StD = np.std(hist_lst)
Median = np.median(hist_lst)

print "Average Module: ", CoM
print "Median: ", Median
print "Standard Deviation: ", StD

#Making plot
binner = (-.5,.5,1.5,2.5,3.5,4.5,5.5,6.5,7.5,8.5,9.5,10.5,11.5,12.5)
plt.hist(hist_lst,bins=binner)
plt.title("Highest Module Students Are On as of  " + date)
plt.xlabel("Module Number")
plt.ylabel("Number of Students")
plt.axis([-.5,12.5,0,max(grade_lst)+5])
plt.xticks([0,1,2,3,4,5,6,7,8,9,10,11,12])
file_name = "PHY122P-ProgressPlot-" + date + ".pdf"
plt.savefig(file_name, format='pdf')

grade_center.close()    
