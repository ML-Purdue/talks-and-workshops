import requests
import json

# URL for the web service
scoring_uri = 'http://ed9e1665-47bd-4423-8dde-07df13bae38e.eastus2.azurecontainer.io/score'
# If the service is authenticated, set the key or token
# key = ''

# Two sets of data to score, so we get two results back
data = {"data":
        [
            [ "57" , "technician" , "married" , "high.school" , "no" , "no" , "yes" , "cellular" , "may" , "mon" , "371" , "1" , "999" , "1" , "failure" , "-1.8" , "92.89300000000000" , "-46.2" , "1.2990000000000000" , "5099.1" ]
        ]
        }
# Convert to JSON string
input_data = json.dumps(data)

# Set the content type
headers = {'Content-Type': 'application/json'}
# If authentication is enabled, set the authorization header
# headers['Authorization'] = f'Bearer {key}'

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.text)
