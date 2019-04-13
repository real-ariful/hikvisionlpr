import datetime
import pymysql as MySQLdb

#import mysql.connector
#mydb = MySQLdb.connect(host = 'localhost', port = 3306, user = 'root', passwd = 'root', db = 'frs')

class Dbquery(object):
	def checkplate(vehiclePlate):

		try: 
			mydb = MySQLdb.connect(host = '', port = 3306, user = '', passwd = '', db = '')
			mycursor = mydb.cursor()
			mycursor.execute("SELECT COUNT(*) FROM frs_vehicle where vehiclePlate=%s",vehiclePlate)
			myresult = mycursor.fetchone()
			print("Matched with: " + str(myresult))
			return myresult[0]
		except Exception as e:
			print(e)

	def checkvehicledetection(captureTime, vehiclePlate):
		try:
			mydb = MySQLdb.connect(host = '', port = 3306, user = '', passwd = '', db = '')
			mycursor = mydb.cursor()
			sql_insert_query = """SELECT COUNT(*) FROM tbl_lprcamera1 where entryTime =%s AND vehiclePlate=%s"""
			sql_values =(captureTime,vehiclePlate)
			mycursor.execute(sql_insert_query,sql_values)
			myresult = mycursor.fetchone()
			print("Matched with: " + str(myresult))
			return myresult[0]
		except Exception as e:
			print(e)


	def insertvehicledetection(entryTime, vehiclePlate, blorwh, imageLoc, vehicleModel,vehicleColor):
		try:
			mydb = MySQLdb.connect(host = '', port = 3306, user = '', passwd = '', db = '')
			mycursor = mydb.cursor()
			sql_insert_query = """ INSERT INTO `tbl_lprcamera1`(`entryTime`, `vehiclePlate`, `blorwh`, `imageLoc`,`vehicleModel`,`vehicleColor`) 
			                          VALUES (%s,%s,%s,%s,%s,%s)"""

			sql_values = (entryTime, vehiclePlate, blorwh, imageLoc, vehicleModel,vehicleColor )		
			mycursor.execute(sql_insert_query, sql_values)
			row_affected = mycursor.rowcount
			mydb.commit()
			print(row_affected, "record(s) affected")
		except Exception as e:
			print(e)

	def checkBlacklistorWhiteList(vehiclePlate):
		try:
			mydb = MySQLdb.connect(host = '', port = 3306, user = '', passwd = '', db = '')
			mycursor = mydb.cursor()
			sql_query = """SELECT blorwh FROM tbl_whitelistvehicle where vehiclePlate=%s"""
			sql_values = (vehiclePlate)		
			mycursor.execute(sql_query, sql_values)
			#row_affected = mycursor.rowcount
			myresult = mycursor.fetchone()
			print(myresult)
			print("Matched with: " + str(myresult))
			return myresult
		except Exception as e:
	  		print(e)


class timefunctions(object):
        def converttime(capturetime):
            print(capturetime)
            mm = capturetime.split(" ")[0].split("-")[0]
            dd = capturetime.split(" ")[0].split("-")[1]
            yyyy = capturetime.split(" ")[0].split("-")[2]
            hh = capturetime.split(" ")[1].split(":")[0]
            mt = capturetime.split(" ")[1].split(":")[1]
            ss = capturetime.split(" ")[1].split(":")[2]
            #2019-03-10 00:00:00.000000
            return yyyy+"-"+mm+"-"+dd+" "+hh+":"+mt+":"+ss+".000000"


