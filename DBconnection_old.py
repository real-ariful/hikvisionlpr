import datetime
import pymysql as MySQLdb

#import mysql.connector
mydb = MySQLdb.connect(host = host, port = 3306, user = 'root', passwd = 'root', db = 'frs_ble')

class Dbquery(object):
	def checkplate(vehiclePlate):
	  	mycursor = mydb.cursor()
	  	mycursor.execute("SELECT COUNT(*) FROM frs_vehicle where vehiclePlate=%s",vehiclePlate)
	  	myresult = mycursor.fetchone()
	  	print("Matched with: " + str(myresult))
	  	return myresult[0]

	def checkvehicledetection(captureTime, vehiclePlate):
		mycursor = mydb.cursor()
		sql_insert_query = """SELECT COUNT(*) FROM frs_vehicledetection where captureTime =%s AND vehiclePlate=%s"""
		sql_values =(captureTime,vehiclePlate)
		mycursor.execute(sql_insert_query,sql_values)
		myresult = mycursor.fetchone()
		print("Matched with: " + str(myresult))
		return myresult[0]


	def insertvehicledetection(imageLoc,captureTime, vehiclePlate, vehicleModel, vehicleColor):
		mycursor = mydb.cursor()
		sql_insert_query = """ INSERT INTO `frs_vehicledetection`(`imageLoc`, `captureTime`, `vehiclePlate`, `vehicleModel`, `vehicleColor`) 
		                          VALUES (%s,%s,%s,%s,%s)"""

		sql_values = (imageLoc, captureTime, vehiclePlate, vehicleModel, vehicleColor)		
		mycursor.execute(sql_insert_query, sql_values)
		row_affected = mycursor.rowcount
		mydb.commit()
		print(row_affected, "record(s) affected")

	def checkBlacklistorWhiteList(vehiclePlate):
		mycursor = mydb.cursor()
		sql_query = """SELECT blorwh FROM frs_vehicle where vehiclePlate=%s"""
		sql_values = (vehiclePlate)		
		mycursor.execute(sql_query, sql_values)
		#row_affected = mycursor.rowcount
		myresult = mycursor.fetchone()
		print(myresult)
		print("Matched with: " + str(myresult))
		return myresult


	def frsvehicleentry(imageLoc, entryTime, vehiclePlate, vehicleModel, vehicleColor, matchid):
		mycursor = mydb.cursor()
		sql_insert_query = """ INSERT INTO `frs_vehicleentry`(`imageLoc`, `entryTime`, `vehiclePlate`, `vehicleModel`, `vehicleColor`, `matchId`) 
		                          VALUES (%s,%s,%s,%s,%s,%s)"""

		sql_values = (imageLoc, entryTime, vehiclePlate, vehicleModel, vehicleColor, matchid)		
		#print(sql_insert_query, sql_values)
		#mycursor.execute("INSERT INTO frs_vehicleentry(imageLoc, entryTime, vehiclePlate, vehicleModel, vehicleColor, matchid) VALUES (%s,%s,%s,%s,%s,%s)", (imageLoc, entryTime, vehiclePlate, vehicleModel, vehicleColor, matchid))
		mycursor.execute(sql_insert_query, sql_values)
		#myresult = mycursor.fetchone()
		row_affected = mycursor.rowcount
		mydb.commit()
		print(row_affected, "record(s) affected")

##	def frsvehicleexit(imageLoc, entryTime, vehiclePlate, vehicleModel, vehicleColor, matchid):
##		mycursor = mydb.cursor()
##		sql_insert_query = """INSERT INTO `frs_vehicleexit`(`imageLoc`, `entryTime`, `vehiclePlate`, `vehicleModel`, `vehicleColor`, `matchId`) 
##		                VALUES (%s,%s,%s,%s,%s,%s)"""
##
##		sql_values = (imageLoc, entryTime, vehiclePlate, vehicleModel, vehicleColor, matchid)		
##		#print(sql_insert_query, sql_values)
##		#mycursor.execute("INSERT INTO frs_vehicleentry(imageLoc, entryTime, vehiclePlate, vehicleModel, vehicleColor, matchid) VALUES (%s,%s,%s,%s,%s,%s)", (imageLoc, entryTime, vehiclePlate, vehicleModel, vehicleColor, matchid))
##		mycursor.execute(sql_insert_query, sql_values)
##		#myresult = mycursor.fetchone()
##		row_affected = mycursor.rowcount
##		mydb.commit()
##		print(row_affected, "record(s) affected")
##
##
##	def frsstudententry(imageLoc, entryTime, studentId, studentName):
##		mycursor = mydb.cursor()
##		sql_insert_query = """ INSERT INTO `frs_studentmatch`(`imageLoc`, `dateTime`, `matchstudentid`, `matchstudentName`) 
##		                          VALUES (%s,%s,%s,%s)"""
##
##		sql_values = (imageLoc, entryTime, studentId, studentName)		
##		mycursor.execute(sql_insert_query, sql_values)
##		row_affected = mycursor.rowcount
##		mydb.commit()
##		print(row_affected, "record(s) affected")

class timefunctions(object):
        def converttime(capturetime):
            mm = capturetime.split(" ")[0].split("-")[0]
            dd = capturetime.split(" ")[0].split("-")[1]
            yyyy = capturetime.split(" ")[0].split("-")[2]
            hh = capturetime.split(" ")[1].split(":")[0]
            mt = capturetime.split(" ")[1].split(":")[1]
            ss = capturetime.split(" ")[1].split(":")[2]
            #2019-03-10 00:00:00.000000
            return yyyy+"-"+mm+"-"+dd+" "+hh+":"+mt+":"+ss+".000000"
