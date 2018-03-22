from twilio.rest import Client
import time

# Your Account SID from twilio.com/console
account_sid = "AC4384ebc19d6831a18456c6b15d127c61"
# Your Auth Token from twilio.com/console
auth_token  = "cc8449f87d23a97ba1e4ce9bbc4cb553"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+447562769232", 
    from_="+447533017891",
    body="Hello Alex, I made a program to say I love you every ten minutes for the next hour. Love you, Blair xxxxxxxx")

print ("[x] Initial message sent ID: "+message.sid)

for x in range (0, 6): 
	print("[x] Sleeping for ten minutes...")
	time.sleep(60*10)
	message = client.messages.create(
		to="+447562769232",
    from_="+447533017891",
    body="Hello Alex, I love you, Blair xxxxxxx")
	print ("[x] Message number "+str(x+1)+" sent. ID: "+message.sid)