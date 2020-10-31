# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 20:13:57 2020

@author: User
"""

import flask
from flask import Flask,request

app=Flask(__name__)

@app.route('/home',methods=['GET'])
def checkStatus():
    return "YAY!!! its working"

@app.route('/add',methods=['GET'])
def adddNum():
    a=2
    b=3
    return 'The sum of {} and {} is {}.'.format(a,b,a+b)
    
app.run(host='localhost',port=8023)
