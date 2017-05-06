import os
from flask import Flask, request, redirect
from twilio import twiml

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    number = request.form['Form']
    message_body = request.form['Body']

    resp = twiml.Response()
    resp.message('Hello {}, you said: {}'.format(number, message_body))

    return str(resp)





if __name__ == "__main__":
    app.run(debug=True)
