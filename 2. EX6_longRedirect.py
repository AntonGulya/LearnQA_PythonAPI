import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

#first_response = response.history[0]
#second_response = response

print(response.history)
print(response.url)
#print(first_response.url)
#print(second_response.url)
