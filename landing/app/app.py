from flask import Flask, render_template, request, flash, redirect, url_for

import requests
import os
import json

app = Flask(__name__)
app.secret_key = 'thisisjustarandomstring'


def usd(n1):

    response = requests.get('http://usd-service:5050/'+n1)

    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def eur(n1):
    response = requests.get('http://eur-service:5050/'+n1)

    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def gbp(n1):
    response = requests.get('http://gbp-service:5050/'+n1)

    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def jpy(n1):
    response = requests.get('http://jpy-service:5050/'+n1)

    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def cad(n1):
    response = requests.get('http://cad-service:5050/'+n1)

    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def aud(n1):
    response = requests.get('http://aud-service:5050/'+n1)

    result = json.loads(response.content.decode('utf-8'))
    return result['result']


def chf(n1):
    response = requests.get('http://chf-service:5050/'+n1)

    result = json.loads(response.content.decode('utf-8'))
    return result['result']


@app.route('/', methods=['POST', 'GET'])
def index():
    req1 = request.form.get("first")
    number_1 = None
    try:
        number_1 = float(req1)
    except Exception:
        print('cant convert', req1, 'to float')
        number_1 = req1
    operation = request.form.get('operation')
    result = 0
    if operation == 'USD':
        result = usd(str(number_1))
    elif operation == 'EUR':
        result = eur(str(number_1))
    elif operation == 'GBP':
        result = gbp(str(number_1))
    elif operation == 'JPY':
        result = jpy(str(number_1))
    elif operation == 'CAD':
        result = cad(str(number_1))
    elif operation == 'AUD':
        result = aud(str(number_1))
    elif operation == 'CHF':
        result = chf(str(number_1))
    else:
        result = '0'

    flash(
        f'The result of Conversion to {operation} for {number_1} INR is {result}')

    return render_template('index.html')


if __name__ == '__main__':
    app.run(
        debug=True,
        port=5050,
        host="0.0.0.0"
    )
