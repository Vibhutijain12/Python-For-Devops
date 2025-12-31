# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://vibhutijain9812.atlassian.net/rest/api/3/issue/bulk"


API_TOKEN = " "
auth = HTTPBasicAuth("vibhutijain9812@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps({
    "issueUpdates": [
    {
      "fields": {
        "issuetype": {
          "id": "10023"
        },
        "project": {
          "key": "DT"
        },
        "summary": "First Ticket",
        "description": {
          "type": "doc",
          "version": 1,
          "content": [
            {
              "type": "paragraph",
              "content": [
                {
                  "type": "text",
                  "text": "The order placed on 5th June is still in pending status. Please resolve this issue urgently."
                }
              ]
            }
          ]
        }
      },
      "update": {}
    }
  ]
})
  

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
