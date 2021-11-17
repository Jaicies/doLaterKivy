from __future__ import absolute_import

import schedule, time, random

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

#import arrow
#import dramatiq

from django.conf import settings


from twilio.rest import Client

preset_Message = ["Happy Birthday!",
                  "Merry Christmas!",
                  "Happy Anniversary"
                  ]


# scheduler = sched.scheduler(time.time,
#  time.sleep)

def send_sms_message(messages,cellphoneNum):
    account = twilio_account
    token = twilio_token
    client = Client(account, token)
    message = messages  # picks random message from list for now

    client.messages.create(to=cellphoneNum,
                           from_=twilio_number,
                           body=message
                           )

    return True

   # schedule().every().day.at('15:15').do(send_sms_message)

    #while True:
     #   schedule.run_pending()
      #  time.sleep(1)

#  return schedule.Cancel(send_message())  # should make task execute only once

#def schedule_message(self):


   # result = send_sms_message.send_with_options(

   # )