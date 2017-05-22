from flask import Flask, render_template, redirect, make_response, request
from pymongo import MongoClient
import pystatus_settings as settings
import datetime
import uuid

webapp = Flask(__name__)
dbconn = MongoClient(settings.database_host, settings.database_port)

database = dbconn[settings.database_name]
dbcollection = database[settings.database_collection]

@webapp.route("/")
def display_homepage(issue_list=None, app_name=None, app_slogan=None):
	return render_template("home.html", issue_list=dbcollection, app_name=settings.app_name, app_slogan=settings.app_slogan)

@webapp.route("/issues")
def display_issues(issue_list=None, app_name=None):
	return render_template("issues.html", issue_list=dbcollection, app_name=settings.app_name)

webapp.run(host=settings.app_host, port=settings.app_port)