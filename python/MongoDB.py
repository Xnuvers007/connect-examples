# importing module
from pymongo import MongoClient

hostname = "<$hostname>"
database = "<$database>"
port = "<$port>"
username = "<$user>"
password = "<$password>"

uri = "mongodb://" + username + ":" + password + "@" + hostname + ":" + port + "/" + database

# Connect with the portnumber and host
client = MongoClient(uri)

# Access database
mydatabase = client[database]
