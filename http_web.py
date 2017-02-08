# A command line application that REquests data from JSONplaceholder
# JsonPlaceHolder is an online REST API service that that generates 100 fake posts for testing
# the app uses the https://jsonplaceholder.typicode.com/posts url to call the api
# we use the requests HTTP library to make request
# we use simplejson to display the collection of data in the response

import requests
import simplejson as json


#http request to get information from a public api 
r = requests.get('https://jsonplaceholder.typicode.com/posts')
r.text

data = json.loads(r.text)

# loop through result and print
for index in range(len(data)):
	for key in data[index]:
		print(data[index][key])
