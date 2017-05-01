import os



from twilio.rest import Client
#account_sid = os.environ["TWILIO_ACCOUNT_SID"]
#auth_token = os.environ["TWILIO_AUTH_TOKEN"]
door_number = "+447746232368"
my_number = "+447717275049"
account_sid = "AC4046025f20801e32a9524f61cbad34a8"
auth_token = "9e65869078ac5caa40aebf47b7f28f4e"

client = Client(account_sid, auth_token)

print "Sending message to: {} ".format(door_number)
message = client.api.account.messages.create(to=door_number,from_="+441845202065", body="9ZUnAUYm95")
