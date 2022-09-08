import mysql.connector
import requests
import json
import time



url = "https://e621.net/tags.json"

querystring = {"page": "0", "search[hide_empty]": "yes", "search[order]": "count"}

headers = {
    "User-Agent": "nekuake/e621Stats"}  # It is mandatory to set a valid UserAgent. Spoofing one (like Chrome's) could block your IP address to make
# new requests.

response = requests.request("GET", url, data="", headers=headers, params=querystring)
finalDiccionary = []
for x in (range(1, 750)):  #E621 doesn't serve pages after the 750th.
    querystring["page"] = x
    response = requests.request("GET", url, data="", headers=headers, params=querystring)
    tempDictionary = json.loads(response.text)
    for y in (range(0, len(tempDictionary))):
        finalDiccionary.append(tempDictionary[int(y)])
    time.sleep(0.5)  # Delay mandatory by the E621 API. 2 requests per second.

# JSON Export
with open("results.json", "w") as f:
    json.dump(finalDiccionary, f)
    f.close()

# Dump to SQL
mydb = mysql.connector.connect(
  host="",
  user="",
  password=""
)
mycursor = mydb.cursor()
print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)