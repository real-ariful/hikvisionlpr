import datetime
#import pymysql as MySQLdb
from pusher_push_notifications import PushNotifications


class PushNotify(object):
    def vehicle_android_notify(title,vehicleNo,timedate):    
        
        pn_client = PushNotifications(
        instance_id='8518a068-3e7f-4520-8b59-2799cb76b86c',
        secret_key='9A1A920184592A9F281E7635D340E2C9C6D45C27156C7F1F742E6EF69662D67E',
        )
        response = pn_client.publish(
        interests=['hello'],
        publish_body={'apns': {'aps': {'alert': 'Report Created'}},
        'fcm': {'notification':
                {'title': str(title), 'body': 'Time: '+ str(timedate)+ ', Black List Vehicle: '+str(vehicleNo) +' on main entrance'}}})


    def student_android_notify(title,studentName,alert,timedate):    
        
        pn_client = PushNotifications(
        instance_id='8518a068-3e7f-4520-8b59-2799cb76b86c',
        secret_key='9A1A920184592A9F281E7635D340E2C9C6D45C27156C7F1F742E6EF69662D67E',
        )
        response = pn_client.publish(
        interests=['hello'],
        publish_body={'apns': {'aps': {'alert': 'Report Created'}},
        'fcm': {'notification':
                {'title': 'FRS Camera', 'body': alert}}})




    def test_android_notify(title,vehicleNo,timedate):


        pn_client = PushNotifications(
        instance_id='dKEmXMZa2dg:APA91bGSPWTu1wgHL4IqYYpY3KN_X-HhylH1IQirN1AwIgqAx2jZZCIMuH_Yk9X0M5D6WtVMrWd-a0XqOCFY5Np8AEv6j87FeW7ObfDs5VpP3ABV2LeZnm51gzKbgZEca911Bc6XB53-',
        secret_key='dKEmXMZa2dg:APA91bGSPWTu1wgHL4IqYYpY3KN_X-HhylH1IQirN1AwIgqAx2jZZCIMuH_Yk9X0M5D6WtVMrWd-a0XqOCFY5Np8AEv6j87FeW7ObfDs5VpP3ABV2LeZnm51gzKbgZEca911Bc6XB53-',
        )
      

        response = pn_client.publish(
        interests=['hello'],
        publish_body={'apns': {'aps': {'alert': 'Report Created'}},
        'fcm': {'notification':
                {'title': str(title), 'body': 'Time: '+ str(timedate)+ ', Black List Vehicle: '+str(vehicleNo) +' on main entrance'}}})
        #print(response['publishId'])







