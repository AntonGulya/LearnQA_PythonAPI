import requests

a= requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(a.text)

b= requests.head("https://playground.learnqa.ru/ajax/api/compare_query_type")
print(b)

c = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data={"method":"POST"})
#response = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params={"method":"GET"})
#response = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type")
#response = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type")

print(c.text)

import requests

print("****************************")
print("****************************")
print("****************************")

methods = [{"method": "POST"}, {"method": "GET"}, {"method": "PUT"}, {"method": "DELETE"}]


for method_type in methods:
     print("Значение параметра: ", method_type) # выводим тип метода
     response1 = requests.get("https://playground.learnqa.ru/ajax/api/compare_query_type", params=method_type)
     # делаем запрос с вышевыведенным на экран методом
     print("Результат методом GET: ", response1.text) #  результат отправки запроса с параметром method_type

print("****************************")

for method_type in methods:
    print("Значение параметра: ", method_type)
    response2 = requests.post("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method_type)
    print("Результат методом POST: ",response2.text)

print("****************************")

for method_type in methods:
    print("Значение параметра: ", method_type)
    response3 = requests.put("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method_type)
    print("Результат методом PUT: ",response3.text)

print("****************************")

for method_type in methods:
    print("Значение параметра: ", method_type)
    response4 = requests.delete("https://playground.learnqa.ru/ajax/api/compare_query_type", data=method_type)
    print("Результат методом DELETE: ",response4.text)