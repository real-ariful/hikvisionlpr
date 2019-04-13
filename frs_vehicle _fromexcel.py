#----------------------------------------------Code to Simulate FRS Vehicle Recognition--------------------------------#
#----------------------------------------------------------------------------------------------------------------------#


#Importing libraries
import logging
import socket
import datetime
import pymysql as MySQLdb
import time
import json
from pprint import pprint
import csv

import DBconnection
from PushNotification import PushNotify



while True:
    #Dictionary Reader
    with open('test1.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for line in csv_reader:
            no = line['No.']
            capTime = line['Capture Time']
            plateNo = line['Plate No.']
            print(no)
            #print(capTime)
            capTimeNew = DBconnection.timefunctions.converttime(capTime)
            print(capTimeNew)

            resquery = DBconnection.Dbquery.checkvehicledetection(capTimeNew,plateNo)
            if resquery == 0:
                print("Needs to be inserted and checked for blacklist and whitelist")
                DBconnection.Dbquery.insertvehicledetection("Notgiven", capTimeNew, plateNo, "Notgiven", "Notgiven", "Notgiven")

                print("check for blacklist and whitelist")

                blorwhcheck = DBconnection.Dbquery.checkBlacklistorWhiteList(plateNo)
                print(blorwhcheck)
                if blorwhcheck == 1:
                    print("Vehicle is whitelist")
                else:
                    print("Vehicle is blacklisted")
                    PushNotify.vehicle_android_notify("LPR Camera",plateNo,capTime)
     
            elif resquery == 1:
                print("Already inserted")
                
                                                              
                                                                                                                    




