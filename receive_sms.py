import os
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

# Twilio SMS route was at: https://demo.twilio.com/welcome/sms/reply/
# Use NGROK for routing.
@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    print "We are in sms_reply"
    print "The message is: {} ".format(request.form.get('Body'))
    print "The message is form: {}".format(request.form.get('From'))
    print "The message is from country: {} ".format(request.form.get('FromCountry'))



    resp = MessagingResponse()

    resp.message("The Robots are coming! Head for the hills! By Nicholas Herriot")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)





