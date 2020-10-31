# -*- coding: utf-8 -*-
"""
Created on Sun Oct 11 23:18:44 2020

@author: User
"""


import flask
from flask import Flask,request
from summariser import Summariser

app=Flask(__name__)


@app.route('/get_summary',methods=['GET'])
def findSummary():
    summariserObj=Summariser()   
    summary=summariserObj.findSummary()
    return summary
    
app.run('localhost',port=8023)    