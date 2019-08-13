# install pip if not installed
# pip install requests
import csv
import requests

errors_for  = dict()
with open('Urls.csv', 'r') as csvfile:
	#reader = csv.reader(csvfile)
	for r in csvfile.read().splitlines():
		url = r.split(",")[0]
		res = requests.get(url)
		#if res.status_code != 200:
		if not res:
			errors_for[url] = res
			print(url, " => ", res)

#print(errors_for)
	