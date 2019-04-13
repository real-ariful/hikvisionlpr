def push_notify(title,vahicleNo,timedate):    
    from pusher_push_notifications import PushNotifications
    pn_client = PushNotifications(
    instance_id='8518a068-3e7f-4520-8b59-2799cb76b86c',
    secret_key='9A1A920184592A9F281E7635D340E2C9C6D45C27156C7F1F742E6EF69662D67E',
    )
    response = pn_client.publish(
    interests=['hello'],
    publish_body={'apns': {'aps': {'alert': 'Report Created'}},
    'fcm': {'notification': {'title': str(title), 'body': 'Black List Vehicle: '+str(vahicleNo) +'has entered'
                             }
            }}
    )
    print(response['publishId'])



push_notify("LPR Camera","BELAIRE"," has entered main gate.")

