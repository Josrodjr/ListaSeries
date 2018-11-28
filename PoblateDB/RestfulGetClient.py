import requests
import math
import http.client
from requests.auth import HTTPDigestAuth
import json
import random as rand
from urllib import request, parse

# URL for the MOVIEDB

url = "https://api.themoviedb.org/3/tv/popular?api_key=f65ec06f343bb9c8ce56e82286b16734&language=en-US&page=15"

#  you get 4000 series on the first page of the api call

myResponse = requests.get(url)

# For successful API call, response code will be 200 (OK)
if(myResponse.ok):

    # Loading the response data into a dict variable
    # Loads (Load String) takes a Json file and converts into python data structure (dict or list, depending on JSON)
    jData = json.loads(myResponse.content)
    results = jData['results']
    print(len(results))

    for serie in results:

        params = {'seasons':rand.randint(1,10) ,'total_rating': str(serie["vote_average"]/2), 'episodes': str(int(math.floor(serie["popularity"]))), 'plot': str(serie["overview"]), 'release_date': str(serie["first_air_date"]), 'name': str(serie["name"])}

        headers = {
			    'Authorization': "JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJ1c2VybmFtZSI6Ikpvc3JvZGpyIiwiZXhwIjoxNTQzNDk1NzM2LCJlbWFpbCI6Ikpvc3JvZGpyQGdtYWlsLmNvbSJ9.sYW-8RAQVeav5joT9TrLrrndMiEMLEfJO0bZWp6icmc",
			    }

        print(params)
        data = parse.urlencode(params).encode()
        req = request.Request('http://localhost:8000/api/series/', data=data, headers=headers)
        resp = request.urlopen(req)


else:
    # If response code is not ok (200), print the resulting http error code with description
    myResponse.raise_for_status()