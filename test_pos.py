import requests

BASE_URL = "https://preprod.softmg.ru/"
url = f"{BASE_URL}api/v2/feedback/add"

# data = {
#     "feedback_name": "Обсудить проект"
# }
#
# headers = {
#     "Accept": "application/json",
#     "Content-Type": "application/json"
# }
#
# response = requests.post(url, json=data, headers=headers)
#
# print(response.status_code)
# print(response.text)

#data = {
#    "feedback_name": "Обсудить проект",
#    "email": "test@test.ru"
#}

#headers = {
#    "Accept": "application/json",
#    "Content-Type": "application/json"
#}

#response = requests.post(url, json=data, headers=headers)

#print(response.status_code)
#print(response.text)

# data = {
#     "feedback_name": "Обсудить проект",
#     "email": "test@test.ru"
# }
#
# files = {
#     'files[0]': ('', '', 'application/octet-stream')
# }
#
# response = requests.post(url, data=data, files=files)
#
# print(response.status_code)
# print(response.text)

# data = {
#     "feedback_name": "Обсудить проект",
#     "email": "test@test.ru",
#     "name": "Иван Иванов",
#     "phone": "79996666666"
# }
#
# files = {
#     'files[0]': ('', '', 'application/octet-stream')
# }
#
# response = requests.post(url, data=data, files=files)
#
# print(response.status_code)
# print(response.text)

# data = {
#     "feedback_name": "Обсудить проект",
#     "email": "test@test.ru",
#     "name": "Иван Ивановааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааааа яаааааааааа",
#     "phone": "79996666666",
#     "description": "Хочу хочу хочу хочу]",
#     "tags[0]": "Разработка",
#     "privacy_consent": "1",
#     "newsletter_consent": "0"
# }
#
# files = {
#     'files[0]': ('', '', 'application/octet-stream')
# }
#
# response = requests.post(url, data=data, files=files)
#
# print(response.status_code)
# print(response.text)

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