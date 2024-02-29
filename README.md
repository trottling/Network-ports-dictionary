# Port Dictionary
Simple python Dictionary for TCP ports. Usefull when code throws port number description, instead of diplaying port like `404`, show message what it means. 

Edit it for your language syntax

#### Example Python code snippet

```
import requests
#Local Imports
import HTTPStatusCodes

headers = {'content-type': 'application/json'}
url="http://www.google.com" #Example URL
data={"data":"Your Data"}
response = requests.post(url, data=data,headers=headers)
print response
if response.status_code in HTTPStatusCodes.codes:
   print HTTPStatusCodes.codes[response.status_code][0]
   print "Description",HTTPStatusCodes.codes[response.status_code][1]
```

* Collected TCP port from [http://www.iana.org](https://www.iana.org/assignments/service-names-port-numbers/service-names-port-numbers.csv)
