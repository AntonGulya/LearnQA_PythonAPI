import json
import requests
import time

url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

response1=requests.get(url)
token=json.loads(response1.text)["token"]
sec=json.loads(response1.text)["seconds"]

print(response1.text)
#print(token)
#print(time)

ready="Job is ready"
not_ready = "Job is NOT ready"
payload = {"token":{token}}

response2=requests.get(url, params=payload)
status = json.loads(response2.text)["status"]
if status != not_ready:
    print(f"Wrong status:{status}")
time.sleep(sec)
#print(response2.text)

response3=requests.get(url, params=payload)
print(response3.text)
status2 = json.loads(response3.text)["status"]
if status2 != ready:
    print(f"Wrong status:{status2}")
try:
    result=json.loads(response3.text)["result"]
except KeyError:
    print("Нет поля result")