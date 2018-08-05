import requests
import random

url = "http://palletone.club/member.php?mod=register"

params = {"SAq38w": (None, "123")}

res = requests.post(url, files=params)

print res.request.body

print res.request.headers