import requests
#headers = {'User-Agent': 'Mozilla/5.0'}
payload = {'user_name':'Shanta','secret_key':'hfjKricAdD'}

session = requests.Session()
session.post('http://182.163.112.219:9193/fcmtokenget',data=payload)
# the session instance holds the cookie. So use it to get/post later.
# e.g. session.get('https://example.com/profile')



r = requests.post('http://182.163.112.219:9193/fcmtokenget', data = payload)

print(r.text)
print(r.json())
r_json = r.json()
print(type(r_json))

description = r_json['description']
error = r_json['error']
fcm_token = r_json['fcm_token']

print(description)

print(error)
print(r_json['fcm_token'])
#print(len(r_json['fcm_token']))
#print(len(r_json['fcm_token'][0]))
print(fcm_token[0])

