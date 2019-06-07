import os
#import requests
import json
from bruteforce import SecondsToYears, TimeEstimateSec, Bruteforce
from dictionary import LoadFile, DictSearchAlgo
from UserInfo import UserInfoAnalysis

#from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from time import strftime, gmtime

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":

        userInfo = dict()
        common = dict()
        dictionary = dict()
        time = ""

        if request.form.get("password"):

            password = request.form.get("password")

            # calculate time to bruteforce  
            time = SecondsToYears(TimeEstimateSec(password))

            if request.form.get("dictionary"):
                    
                # get the dictionary search result
                dictionary = DictSearchAlgo(
                    LoadFile("data/dictionary/*.marisa"), password)

            if request.form.get("common"):

                # get common passwords words in password
                common = DictSearchAlgo(LoadFile("data/common/*.marisa"), password)

            if request.form.get("info"):
                    
                if request.form.get("fullname"):

                    userInfo["fullname"] = UserInfoAnalysis(request.form.get("fullname"), password)

                else:

                    userInfo["fullname"] = ""

                if request.form.get("petname"):

                    userInfo["petname"] = UserInfoAnalysis(request.form.get("petname"), password)

                else:

                    userInfo["petname"] = ""

                if request.form.get("birthday"):

                    userInfo["birthday"] = UserInfoAnalysis(request.form.get("birthday"), password)

                else:

                    userInfo["birthday"] = ""

                if request.form.get("lovename"):

                    userInfo["lovename"] = UserInfoAnalysis(request.form.get("lovename"), password)

                else:

                    userInfo["lovename"] = ""
    
                if request.form.get("sport"):

                    userInfo["sport"] = UserInfoAnalysis(request.form.get("sport"), password)

                else:

                    userInfo["sport"] = ""

                if request.form.get("team"):

                    userInfo["team"] = UserInfoAnalysis(request.form.get("team"), password)
 
                else:

                    userInfo["team"] = ""

            return jsonify(time, dictionary, common, userInfo)

        else:
            render_template("error.html")

    else:
        return render_template("index.html")

    
