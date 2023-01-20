import json
import requests


lst = []

response = requests.get(f"http://localhost:3000/pokemon/1")
resp = response.json()
pkID = resp["id"]
pkName = resp["name"]
pkType1 = resp["type1"]
pkType2 = resp["type2"]
pkSprite = resp["sprite"]


print(f"#{pkID} {pkName}\n{pkType1}{pkType2}\n{pkSprite}")
