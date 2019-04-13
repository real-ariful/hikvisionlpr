#----------------------------------------------Code to Simulate FRS Vehicle Recognition--------------------------------#
#----------------------------------------------------------------------------------------------------------------------#


#Importing libraries

import datetime
import pymysql as MySQLdb
import time
import json
from pprint import pprint
import csv

import DBconnection
from PushNotification import PushNotify



#while True:
    #Dictionary Reader
with open('vehicle_detection.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for line in csv_reader:
        no = line['No.']
        capTime = line['Capture Time']
        plateNo = line['Plate No.']
        print(no)
        #print(capTime)
        capTimeNew = DBconnection.timefunctions.converttime(capTime)
        print(capTimeNew)
        print(plateNo)

        resquery = DBconnection.Dbquery.checkvehicledetection(capTimeNew,plateNo)
        if resquery == 0:
            print("Needs to be inserted and checked for blacklist and whitelist")
            #DBconnection.Dbquery.insertvehicledetection(capTimeNew, plateNo,0,"","","")

            print("check for blacklist and whitelist")

            blorwhcheck = DBconnection.Dbquery.checkBlacklistorWhiteList(plateNo)
            print(blorwhcheck)
            if blorwhcheck == 1:
                print("Vehicle is whitelist")
                DBconnection.Dbquery.insertvehicledetection(capTimeNew, plateNo,1,"","","")
            else:
                print("Vehicle is blacklisted")
                DBconnection.Dbquery.insertvehicledetection(capTimeNew, plateNo,0,"","","")#(entryTime, vehiclePlate, blorwh, imageLoc, vehicleModel,vehicleColor)
                print("Notification send")
                PushNotify.vehicle_android_notify("LPR Camera",plateNo,capTime)
                #print("Not require insertion")
 
        elif resquery == 1:
            print("Not require insertion")

        time.sleep(20)

        
                
                                                                                          

    time.sleep(5)
    ###Vehicle-1-entry
    ##i=0
    ##print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
    ##vehicle_plate = vehicle_rec[i]["vehicle_plate"]
    ##DBconnection.Dbquery.checkplate(vehicle_plate)
    ###DBconnection.Dbquery.frsvehicleentry("C://Image//image1.png", "2019-03-10 00:00:00.000000", vehicle_plate, vehicle_model, vehicle_color, 0)
    ##print()
    ##time.sleep(5)





