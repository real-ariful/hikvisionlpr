import datetime
#import pymysql as MySQLdb
#from pusher_push_notifications import PushNotifications

from pyfcm import FCMNotification
push_service = FCMNotification(api_key="AAAAZg1i79A:APA91bH_49dpdXeuKpc4Mr3MpGS_qwRhnSYGV6E5Gew9U26GuLuzbtIj33OgSbVD1UgW442RX5CXuf3TvZHS9DEsD0ACVnsBxV6frVSs7z0QgOJLhb_Iy3jU3qJYkrS1-tO2A_W3GIx5")


class PushNotify(object):
    def vehicle_android_notify(title,vehicleNo,timedate):    
        #test_android_notify("LPR Camera", "BELAIRE","2019-04-09 11:05:10.000123")



        #NEW NOTIFICATION

        registration_id = "f0fwNp0eKdI:APA91bEEbJ7bPCowDwL6KK9Xt75UYaoqgck-sqjU_uNDZspThHPDLxsmyKBLaAHApk0_IOWkEmJMma8kCCXo4E94Bzb2-J-4AabHteHCl4HpuwvOiSaVeQLDE8LMSYfic3VfpI4O6W-j"
        message_title = title
        message_body = 'Time: '+ str(timedate) + ', Black List Vehicle: ' + str(timedate) + 'BELAIRE on main entrance'
            
        result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)


registration_id = "dKEmXMZa2dg:APA91bGSPWTu1wgHL4IqYYpY3KN_X-HhylH1IQirN1AwIgqAx2jZZCIMuH_Yk9X0M5D6WtVMrWd-a0XqOCFY5Np8AEv6j87FeW7ObfDs5VpP3ABV2LeZnm51gzKbgZEca911Bc6XB53-"
message_title = "LPR Camera"
message_body = 'Time: '+ "BELAIRE","2019-04-09 11:05:10.000123" + ', Black List Vehicle: BELAIRE on main entrance'
print("Notification send")
result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title, message_body=message_body)




