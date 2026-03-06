import requests

# def test_get_new_user_and_assert_status_code_200():
#     response = requests.get(url="https://petstore.swagger.io/v2/user/Anna")
#     print(response.json())
#     assert response.status_code == 200

new_user = {
    "id": 10,
    "username": "1",
    "firstName": "2",
    "lastName": "3",
    "email": "third_user@test.com",
    "password": "passwordUser3",
    "phone": "+755566rr322",
    "userStatus": 0
}


def test_post_valid_schema_with_correct_user():
    response = requests.post(url="https://petstore.swagger.io/v2/user", json=new_user)
    print(response.text)
    body = response.json()
    print(body)
    # assert body['message'] == 'ok'
    assert response.status_code == 200
