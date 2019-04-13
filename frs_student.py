###----------------------------------------------Code to Simulate FRS student Recognition--------------------------------#
###----------------------------------------------------------------------------------------------------------------------#
##
##
###Importing libraries
##import logging
##import socket
##import datetime
##import pymysql as MySQLdb
##import time
##import json
##from pprint import pprint
##import datetime
##
##import DBconnection
##from PushNotification import PushNotify
##
##with open('student_rec.json') as f:
##    data = json.load(f)
##    student_rec =  data["student_rec"]
##
###PushNotify.student_android_notify("LPR Camera","BELAIRE"," has entered main gate.")
###print("PUSH Notification Working")
##
##pprint("---------------------Student Simulation has started---------------------")
##pprint("------------------------------------------------------------------------")
### pprint(data["student_rec"])
### print(len(student_rec))
##
##time.sleep(30)
##
###--------------Simulation student entry and exit----------------------------------
##
###student-1-entry
##i=0
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has arrived")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student1.jpg", currentDT, i+1, studentName)
###PushNotify.student_android_notify("Student"+str(i+1), studentName, studentName +" has arrived",currentDT)
##print()
##time.sleep(5)
##
###student-2-entry
##i=1
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has arrived")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student2.jpg", currentDT, i+1, studentName)
###PushNotify.student_android_notify("Student"+str(i+1), studentName,studentName +" has arrived",currentDT)
##print()
##time.sleep(5)
##
##
###student-3-entry
##i=2
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has arrived")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student3.jpg", currentDT, i+1, studentName)
###PushNotify.student_android_notify("Student"+str(i+1), studentName,studentName +" has arrived",currentDT)
##print()
##time.sleep(5)
##
### #student-2-exit
### i=1
### print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has exited school")
### studentName = student_rec[i]["studentName"]
### time.sleep(5)
##
##
###student-4-entry
##i=3
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has arrived")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student4.jpg", currentDT, i+1, studentName)
###PushNotify.student_android_notify("Student"+str(i+1), studentName,studentName +" has arrived",currentDT)
##print()
##time.sleep(5)
##
###student-5-entry-unregistered
##i=4
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has entered school")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student5.jpg", currentDT, i+1, studentName)
##PushNotify.student_android_notify("Suspected: UnKnown Student"," ","Suspected: UnKnown Student" +" has arrived",currentDT)
##print()
##time.sleep(5)
##
##
### #student-4-exit
### i=3
### print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has exited school")
### studentName = student_rec[i]["studentName"]
### time.sleep(5)
##
###student-6-entry
##i=5
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has entered school")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student6.jpg", currentDT, i+1, studentName)
##PushNotify.student_android_notify("Student"+str(i+1), studentName,studentName +" has arrived",currentDT)
##print()
##time.sleep(5)
##
### #student-5-exit
### i=4
### print("student "+ student_rec[i-1]["number"]+ "--" + student_rec[i-1]["studentName"] +" has exited school")
### studentName = student_rec[i]["studentName"]
### time.sleep(5)
##
###student-7-entry
##i=6
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" arrived with big bag")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student7.jpg", currentDT, i+1, studentName)
##PushNotify.student_android_notify("Suspected"+str(i+1), studentName,"Suspected: " +studentName +" arrived with big bag",currentDT)
##print()
##time.sleep(20)
##
###student-8-entry
##i=7
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" arrived with knife")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student8.jpg", currentDT, i+1, studentName)
##PushNotify.student_android_notify("Student"+str(i+1), studentName,"Suspected: " +studentName +" arrived with knife",currentDT)
##print()
##time.sleep(20)
##
### #student-6-exit
### i=5
### print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has exited school")
### studentName = student_rec[i]["studentName"]
### time.sleep(5)
##
### #student-8-exit
### i=7
### print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has exited school")
### studentName = student_rec[i]["studentName"]
### time.sleep(5)
##
###student-9-entry
##i=8
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has arrived")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student9.jpg", currentDT, i+1, studentName)
###PushNotify.student_android_notify("Student"+str(i+1), studentName,studentName +" has arrived",currentDT)
##print()
##time.sleep(20)
##
###student-10-entry
##i=9
##print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has arrived")
##studentName = student_rec[i]["studentName"]
##currentDT = datetime.datetime.now()
##DBconnection.Dbquery.frsstudententry("Students/student10.jpg", currentDT, i+1, studentName)
##PushNotify.student_android_notify("Student"+str(i+1),studentName,"Suspected: " +studentName +" is with gun.",currentDT)
##print()
##time.sleep(5)
##
### #student-9-exit
### i=8
### print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has exited school")
### studentName = student_rec[i]["studentName"]
### time.sleep(5)
##
### #student-10-exit
### print("student "+ student_rec[i]["number"]+ "--" + student_rec[i]["studentName"] +" has exited school")
### studentName = student_rec[i]["studentName"]
### time.sleep(5)
##
