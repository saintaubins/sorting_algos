import requests

my_req = requests.get('http://www.example.com')

print(my_req.content)