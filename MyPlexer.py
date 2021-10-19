import requests
import os, sys

from main import app
from flask import request

def flaskapp():
    app.run(host="127.0.0.1", port=5000)

def getinp():
    while(True):
        inp = input().strip()
        if "hi" == inp.lower():
            res = requests.get("http://127.0.0.1:5000/hi")
            print(res.text)
        elif "sayhito" in inp.lower():
            name = inp.split(" ")
            if len(name) < 2:
                print("Error: Unable to Process. Wrong no of Parameters provided")
                continue
            name = inp.split(" ")[1]
            res = requests.get("http://127.0.0.1:5000/sayhito/{}".format(name))
            print(res.text)
        elif "count" in inp.lower():
            vals = inp.split(" ")
            if len(vals) < 2:
                print("Error: Unable to Process. Wrong no of Parameters provided")
                continue
            vals = " ".join(vals[1:])
            res = requests.get("http://127.0.0.1:5000/count?{}".format(vals))
            print(res.text)
        elif "exit" == inp.lower():
            try:
                res = requests.get("http://127.0.0.1:5000/exit")
            except Exception as e:
                break
