from pymongo import MongoClient
import datetime
import pystatus_settings as settings

dbconn = MongoClient(settings.database_host, settings.database_port)

database = dbconn[settings.database_name]
dbcollection = database[settings.database_collection]

issue_type = ""
issue_timestamp = int(datetime.datetime.utcnow().timestamp())
issue_title = ""
issue_body = ""
issue_solve_timestamp = ""
issue_affected_servers = ""
num_mins = 0

while issue_type == "":
	issue_type = input("Enter an issue type (maintenance|warning|downtime): ")

while issue_title == "":
	issue_title = input("Enter a title for the issue: ")

while issue_body == "":
	issue_body = input("Describe the issue: ")

while num_mins == 0:
	try:
		num_mins = int(input("Enter the number of minutes until fix: "))
	except ValueError:
		continue

while issue_affected_servers == "":
	issue_affected_servers = input("Enter a comma-separated list of affected servers: ")

issue_solve_timestamp = issue_timestamp + (num_mins * 60)
issue_solve_timestamp = datetime.datetime.fromtimestamp(issue_solve_timestamp).strftime("%d/%m/%Y %H:%M:%S")
issue_timestamp = datetime.datetime.fromtimestamp(issue_timestamp).strftime("%d/%m/%Y %H:%M:%S")

json = {
	"issue_type": issue_type,
	"issue_timestamp": issue_timestamp,
	"issue_title": issue_title,
	"issue_body": issue_body,
	"issue_solve_timestamp": issue_solve_timestamp,
	"issue_affected_servers": issue_affected_servers
}

dbcollection.insert_one(json)

print("Added successfully.")