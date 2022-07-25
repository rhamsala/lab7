
from curses import flash
from multiprocessing import connection
from tabnanny import check
from flask import Flask, request, render_template
import sqlite3
import os
import random
import re

app = Flask(__name__)



@app.route('/', methods=["POST" , "GET"])
def main():
     
    return render_template("index.html")


@app.route("/result",methods = ["POST","GET"])
def results():
    password = str(request.form.get("password"))
    reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"
          
    pat = re.compile(reg)
    check = re.search(pat, password)
    flag = False
       
    if check:
        flag=True
    
    return render_template("report.html",flag=flag)


if __name__=='__main__':
    app.run()