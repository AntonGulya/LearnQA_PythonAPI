import requests

class TestCookie:
    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        response1 = requests.get(url)
        print(dict(response1.cookies))

        assert response1.status_code ==200, 'Wrong request'

        response_dict = dict(response1.cookies)
        assert 'HomeWork' in response_dict, 'No one HomeWork'

        expected_value_HW = 'hw_value'
        actual_value_HW = response_dict['HomeWork']
        assert expected_value_HW == actual_value_HW, 'Not expected values'

# import requests
# url = "https://playground.learnqa.ru/api/homework_cookie"
# response1 = requests.get(url)
# print(dict(response1.cookies))
# response_dict = dict(response1.cookies)
# actual_value_HW = response_dict['HomeWork']
# print(actual_value_HW)