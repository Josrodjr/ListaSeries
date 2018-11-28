#Python 2.7.6
#RestfulClient.py

import requests
import math
import http.client
from requests.auth import HTTPDigestAuth
import json
import urllib

# URL for the MOVIEDB

url = "https://api.themoviedb.org/3/tv/popular?api_key=f65ec06f343bb9c8ce56e82286b16734&language=en-US&page=1"

#  you get 4000 series on the first page of the api call

myResponse = requests.get(url)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):

	# Loading the response data into a dict variable
	# Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
	jData = json.loads(myResponse.content)

	conn = http.client.HTTPConnection("localhost")
	params = {'total_rating': str(jData['results'][0]["vote_average"]), 'episodes': str(int(math.floor(jData['results'][0]["popularity"]))), 'plot': str(jData['results'][0]["overview"]), 'release_date': str(jData['results'][0]["first_air_date"]), 'nombre': str(jData['results'][0]["name"])}
	# payload = "total_rating="+str(jData['results'][0]["vote_average"])+"&episodes="+str(int(math.floor(jData['results'][0]["popularity"])))+"&plot="+str(jData['results'][0]["overview"])+"&release_date="+str(jData['results'][0]["first_air_date"])+"&nombre="+str(jData['results'][0]["name"])

	headers = {
			'Authorization': "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6Ikpvc3JvZGpyIiwiZXhwIjoxNTQzNDk1NzM2LCJlbWFpbCI6Ikpvc3JvZGpyQGdtYWlsLmNvbSJ9.sYW-8RAQVeav5joT9TrLrrndMiEMLEfJO0bZWp6icmc",
			'Content-Type': "application/x-www-form-urlencoded",
			'cache-control': "no-cache",
			'Postman-Token': "8762fa02-5c9f-44cb-93da-5213bba12550"
			}

	payload = urllib.parse.urlencode(params, quote_via=urllib.parse.quote)

	conn.request("POST", "api,series,", payload, headers)

	res = conn.getresponse()
	data = res.read()

	print(data.decode("utf-8"))

else:
  # If response code is not ok (200), print the resulting http error code with description
	myResponse.raise_for_status()