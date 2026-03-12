import requests
import pytest
from generators import generate_name, generate_email, generate_phone_1, generate_phone_2, generate_phone_3, \
    generate_description, generate_long_phone

BASE_URL = "https://preprod.softmg.ru/"
url = f"{BASE_URL}api/v2/feedback/add"


feedback_names = [
    "Оставить заявку",
    "Обсудить проект",
    "Мы готовы помочь с выбором",
    "Остались вопросы",
    "Задать вопрос"
]

@pytest.mark.parametrize ('feedback_name', feedback_names)
def test_form_empty(feedback_name):
    data = {
        "feedback_name": feedback_name
    }

    response = requests.post(url, data=data)

    assert response.status_code == 422
    assert response.text is not None

    print(f"Статус: {response.status_code}")
    print(f"Текст: {response.text}")

@pytest.mark.parametrize ('feedback_name', feedback_names)
def test_with_email(feedback_name):

    data = {
        "feedback_name": feedback_name,
        "email": generate_email()
    }

    print(f"Мыло: {generate_email()}")

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

@pytest.mark.parametrize ('feedback_name', feedback_names)
def test_with_emeil_file(feedback_name):
    data = {
        "feedback_name": feedback_name,
        "email": generate_email()
    }

    files = {
        'files[0]': ('', '', 'application/octet-stream')
    }

    response = requests.post(url, data=data, files=files)

    assert response.status_code == 201
    assert response.text is not None

    print(f"Code: {response.status_code}")
    print(f"Text: {response.text}")


@pytest.mark.parametrize ('feedback_name', feedback_names)
def test_with_all(feedback_name):

    data = {
        "feedback_name": feedback_name,
        "email": generate_email(),
        "name": generate_name(),
        "phone": generate_phone_2(),
        "privacy_consent": "1",
        "newsletter_consent": "0"
    }

    files = {
        'files[0]': ('', '', 'application/octet-stream')
    }

    response = requests.post(url, data=data, files=files)

    print(f"Код ответа: {response.status_code}")
    print(f"Тело ответа: {response.text}")

    assert response.status_code == 201
    assert response.text is not None

@pytest.mark.parametrize ('feedback_name', feedback_names)
def test_with_long_name(feedback_name):

    data = {
        "feedback_name": feedback_name,
        "email": generate_email(),
        "name": generate_name(),
        "phone": generate_phone_3(),
        "description": generate_description(),
        "tags[0]": "Разработка",
        "privacy_consent": "1",
        "newsletter_consent": "0"
    }

    files = {
        'files[0]': ('', '', 'application/octet-stream')
    }

    response = requests.post(url, data=data, files=files)

    print(f"Код ответа: {response.status_code}")
    print(f"Ответ: {response.text}")
    print(f"Телефон: {generate_phone_3}")
    print(f"Описание: {generate_description}")

    assert response.status_code == 201
    assert response.text is not None

@pytest.mark.parametrize ('feedback_name', feedback_names)
def test_with_invalid_phone(feedback_name):

    data = {
        "feedback_name": feedback_name,
        "email": generate_email(),
        "name": generate_name(),
        "phone": generate_long_phone()
    }

    files = {
        'files[0]': ('', '', 'application/octet-stream')
    }

    response = requests.post(url, data=data, files=files)

    assert response.status_code == 422
    assert response.text is not None

    print(f'Код: {response.status_code}')
    print(f'Ответ: {response.text}')

@pytest.mark.parametrize ('feedback_name', feedback_names)
def test_privacy_consent(feedback_name):

    data = {
    'feedback_name': feedback_name,
    'email': generate_email(),
    'name': generate_name(),
    'phone': generate_phone_3()
    }

    files = {
        'files[0]': ('', '', 'application/octet-stream')
    }

    response = requests.post(url, data=data, files=files)

    print(f"Форма: {feedback_name}")
    print(f"Код ответа: {response.status_code}")
    print(f"Тело ответа: {response.text}")

    assert response.status_code == 422
    assert response.text is not None
    assert response.text != ""
