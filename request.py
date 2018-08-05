import requests
import random

url = "http://palletone.club/member.php?mod=register"

params = {}

res = requests.post(url, files=params)

print res.request.body

print res.request.headers