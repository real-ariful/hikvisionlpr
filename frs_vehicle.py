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

import DBconnection
from PushNotification import PushNotify

with open('vehicle_rec.json') as f:
    data = json.load(f)
    vehicle_rec =  data["vehicle_rec"]

#PushNotify.android_notify("LPR Camera","BELAIRE"," has entered main gate.")
#print("PUSH Notification Working")

#pprint(data)
pprint("---------------------Vehicle Simulation has started---------------------")
pprint("------------------------------------------------------------------------")
# pprint(data["vehicle_rec"])
# print(len(vehicle_rec))

time.sleep(5)
#Vehicle-1-entry
i=0
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
#DBconnection.Dbquery.frsvehicleentry("C://Image//image1.png", "2019-03-10 00:00:00.000000", vehicle_plate, vehicle_model, vehicle_color, 0)
print()
time.sleep(5)

#Vehicle-2-entry
i=1
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
vehicle_model = vehicle_rec[i]["vehicle_model"]
vehicle_color= vehicle_rec[i]["vehicle_color"]

DBconnection.Dbquery.checkplate(vehicle_plate)
DBconnection.Dbquery.frsvehicleentry("C://Image", "2019-03-10 00:00:00.000000", vehicle_plate, vehicle_model, vehicle_color, 0)
print()
time.sleep(5)


#Vehicle-1-exit
i=0
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has exited school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)


#Vehicle-3-entry-not registered
i=2
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)

PushNotify.vehicle_android_notify("LPR Camera ",vehicle_plate," is on main entrance.")
print()
time.sleep(5)

#Vehicle-2-exit
i=1
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has exited school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)


#Vehicle-4-entry
i=3
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-5-entry
i=4
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)


#Vehicle-4-exit
i=3
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has exited school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-6-entry
i=5
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-5-exit
i=4
print("Vehicle "+ vehicle_rec[i-1]["number"]+ "--" + vehicle_rec[i-1]["vehicle_plate"] +" has exited school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-7-entry-unregistered
i=6
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
PushNotify.vehicle_android_notify("LPR Camera ", vehicle_plate ,"abc")
print()
time.sleep(5)

#Vehicle-8-entry
i=7
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-6-exit
i=5
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has exited school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-8-exit
i=7
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has exited school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-9-entry
i=8
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-10-entry
i=9
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has entered school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-9-exit
i=8
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has exited school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

#Vehicle-10-exit
print("Vehicle "+ vehicle_rec[i]["number"]+ "--" + vehicle_rec[i]["vehicle_plate"] +" has exited school")
vehicle_plate = vehicle_rec[i]["vehicle_plate"]
DBconnection.Dbquery.checkplate(vehicle_plate)
print()
time.sleep(5)

