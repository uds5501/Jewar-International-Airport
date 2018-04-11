from twilio.rest import TwilioRestClient
import pickle
# Find these values at https://twilio.com/user/account
x=pickle.load(open('twilio_info.dat','rb'))

account_sid = x[0]
auth_token = x[1]
client = TwilioRestClient(account_sid, auth_token)

def send_OTP(no,OTP):
    message = client.messages.create(to="+91"+str(no), from_="+13614330844",body="Hello there!"+" Your OTP for transaction is: "+str(OTP)+ "!"+"\nFROM JEWAR")
