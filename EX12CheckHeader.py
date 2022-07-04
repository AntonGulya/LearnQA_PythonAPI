import requests

class TestCookie:
    def test_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        response1 = requests.get(url)
        header = response1.headers
        header_value = header.get("x-secret-homework-header")
        print(header)
        assert response1.status_code ==200, 'Bad request'
        assert 'x-secret-homework-header' in header, 'No have x-secret-header in header'
        assert header_value == 'Some secret value', 'Wrong x-secret-header value'


