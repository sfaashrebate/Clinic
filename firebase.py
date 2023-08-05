import firebase_admin
from firebase_admin import credentials, messaging, auth

import firebase_admin
from firebase_admin import credentials

cred = credentials.Certificate('libancall-2e332-firebase-adminsdk-61psz-de7332859f.json')
firebase_admin.initialize_app(cred)

# This registration token comes from the client FCM SDKs.
registration_token = 'dD9qHk6GS0-vdEff-oy94A:APA91bHzIkcTiTLiQvnP8c3Ub85_3Jhr41nf8ODdExSc2HLazMHwhetTPopMhdjrh5plbbvsehv_4CFyble2t6Lkz5D2fRsr2QSEek7fzP3lPBg5h-7avpntQpbdRiD2RErKdh4Yztsi'

# See documentation on defining a message payload.
message = messaging.Message(
    data={
        'score': 'test'
    },
    token=registration_token,
)

# Send a message to the device corresponding to the provided
# registration token.
response = messaging.send(message)
# Response is a message ID string.
print('Successfully sent message:', response)

print(response)
print(type(response))
