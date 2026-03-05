import requests

BASE_URL = "https://preprod.softmg.ru/"
url = f"{BASE_URL}api/v2/feedback/add"

def test_form_empty ():
    data = {
        "feedback_name": "Обсудить проект"
    }

    response = requests.post(url, data=data)

    assert response.status_code == 422
    assert response.text is not None

    print(f"Статус: {response.status_code}")
    print(f"Текст: {response.text}")

def test_with_email():

    data = {
        "feedback_name": "Обсудить проект",
        "email": "test@test.ru"
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json"
    }

    response = requests.post(url, json=data, headers=headers)

    print(f"Ответ: {response.text}")
    print(f"Заголовки: {response.headers}")

    assert response.status_code == 500
    assert response.text is not None
    assert response.text != ""

    print(f"Code: {response.status_code}")
    print(f"Text: {response.text}")

def test_with_emeil_file ():
    data = {
        "feedback_name": "Обсудить проект",
        "email": "test@test.ru"
    }

    files = {
        'files[0]': ('', '', 'application/octet-stream')
    }

    response = requests.post(url, data=data, files=files)

    assert response.status_code == 201
    assert response.text is not None

    print(f"Code: {response.status_code}")
    print(f"Text: {response.text}")

def test_with_all ():
    data = {
        "feedback_name": "Обсудить проект",
        "email": "test@test.ru",
        "name": "Иван Иванов",
        "phone": "79996666666"
    }

    files = {
        'files[0]': ('', '', 'application/octet-stream')
    }

    response = requests.post(url, data=data, files=files)

    print(response.status_code)
    print(response.text)

def test_with_long_name ():
    data = {
        "feedback_name": "Обсудить проект",
        "email": "test@test.ru",
        "name": "Иван Ивановааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа яаааааааааа",
        "phone": "79996666666",
        "description": "Хочу хочу хочу хочу]",
        "tags[0]": "Разработка",
        "privacy_consent": "1",
        "newsletter_consent": "0"
    }

    files = {
        'files[0]': ('', '', 'application/octet-stream')
    }

    response = requests.post(url, data=data, files=files)

    print(response.status_code)
    print(response.text)

def test_with_invalid_phone ():
    data = {
        "feedback_name": "Обсудить проект",
        "email": "test@test.ru",
        "name": "Иван Иванов",
        "phone": "привет"
    }

    files = {
        'files[0]': ('', '', 'application/octet-stream')
    }

    response = requests.post(url, data=data, files=files)

    print(response.status_code)
    print(response.text)