
#Importing libraries
import requests
from xml.dom import minidom
from pytz import timezone 

import datetime
from datetime import datetime, date
import pymysql as MySQLdb
import time
import json
from pprint import pprint
import csv
import xmltodict, json

import DBconnection
from PushNotificationold import PushNotify


def convertdatetime(captureTime):
    date = captureTime.split("T")[0]
    timee = captureTime.split("T")[1].split("-")[0]
    year =date[0:4]
    day = date[4:6]
    mm = date[6:8]
    #2019-04-08 11:19:42.829561
    return year+"-"+mm+"-"+day+" "+ timee

def lprtimetodbtime(captureTime):

    #datetimee = "20190411T161739-500"
    date = captureTime.split("T")[0]
    timee = captureTime.split("T")[1].split("-")[0]
    year =date[0:4]
    day = date[4:6]
    mm = date[6:8]
    hr = timee[0:2]
    mins = timee[2:4]
    ss = timee[4:6]

    #2019-04-08 11:19:42.829561
    return year+"-"+mm+"-"+day+" "+ hr +":" + mins +":" +ss+".000000"

while True:

    florida = timezone('US/Eastern')
    #florida = timezone('Asia/Dhaka')
    florida_time = datetime.now(florida)
    print(florida_time)


    data = "2019-04-12 09:19:19.838092-04:00"
    year = data.split("-")[0]
    month= data.split("-")[1]
    day = data.split("-")[2].split(" ")[0]

    hm = data.split(" ")[1].split(":")[0]
    mins = data.split(" ")[1].split(":")[1]
    ss = data.split(" ")[1].split(":")[1]
    msec = data.split(".")[1].split("-")[0]
    print(hm)
    print(mins)
    print(ss)
    print(msec)
    datetimee = year+month+day
    print(datetimee)

    xmldata = year+month+day+hm+mins+ss+msec
    print(xmldata)

    #201904120601000000

    print(year)
    print(month)
    print(day)


    try:
        xml = """<?xml version="1.0" encoding="UTF-8"?>
        <AfterTime> <picTime> """ + xmldata+ """</picTime></AfterTime> """
        headers = {'Content-Type': 'text/xml'} # set what your server accepts

        res_lpr = requests.post('http://scthik.dvrlists.com:70/ISAPI/Traffic/channels/1/vehicleDetect/plates', auth=('admin', '$ct12345'), data= xml)
        #print(res_lpr.text)
        print(type(res_lpr.text))
        print(type(res_lpr.json))


        

        parsed = xmltodict.parse(res_lpr.text)
        response_json = json.dumps(parsed)
        print(type(response_json))


        Plates = json.loads(response_json)["Plates"]["Plate"]

        print(len(Plates))

        for plate in Plates:


            captureTime = plate['captureTime']
            #print(lprtimetodbtime(captureTime))

            #captureTime = convertdatetime(captureTime)

            capTimeNew = lprtimetodbtime(captureTime)
            #date = captureTime.split("T")[0]
            #timee = captureTime.split("T")[1].split("-")[0]
            plateNo = plate['plateNumber']
            picName = plate['picName']
            country = plate['country']
            laneNo = plate['laneNo']
            direction = plate['direction']
            matchingResult = plate['matchingResult']
            #20190412080100148_1J6AG_VEHICLE_DETECTION.jpg
            imageLoc = "http://3.18.42.77/vehicledetection/lprcamera1/"
            imageLoc = imageLoc + picName + "_" + plateNo + "_" + "VEHICLE_DETECTION.jpg"


            print("Capture Date: " + str(capTimeNew))
            print("plateNumber: " + str(plateNo))
            print("picName: " + str(picName))
            #print("country: " + str(country))
            #print("laneNo: " + str(laneNo))
            print("direction: " + str(direction))
            print("matchingResult: " + str(matchingResult))
            print("imageLoc: " +str(imageLoc))

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
                    DBconnection.Dbquery.insertvehicledetection(capTimeNew, plateNo,0,imageLoc,"","")#(entryTime, vehiclePlate, blorwh, imageLoc, vehicleModel,vehicleColor)
                    print("Notification send")
                    PushNotify.vehicle_android_notify("LPR Camera",plateNo,capTimeNew)
                    #print("Not require insertion")

            elif resquery == 1:
                print("Not require insertion")

            time.sleep(5)





            
            
        #--------------------------------------------------------------------

        with open('test.json','w') as file:
            file.write(response_json)


    except requests.exceptions.HTTPError as err:
        print(err)
