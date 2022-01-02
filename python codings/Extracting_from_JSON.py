import json
import urllib.request as ur
count = 0

url = "http://py4e-data.dr-chuck.net/comments_1043530.json"
print ("retrieving URL. Stand by.")
uh = ur.urlopen(url)
data= uh.read()

info = json.loads(data)
for item in info["comments"]:
	
	number = int(item["count"])
	count = count + number
print (count)
