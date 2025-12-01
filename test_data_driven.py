import pytest
import requests
from pytest_dependency import depends

# -----------------------------------------------------------
# 1. Define your Test Data
# Format: List of Tuples -> [(input, expected), (input, expected)]
# -----------------------------------------------------------
test_data = [
    (1, "Leanne Graham"),
    (2, "Ervin Howell"),
    (3, "Clementine Bauch")
]

# -----------------------------------------------------------
# 2. The Test Function
# We use the @pytest.mark.parametrize decorator.
# It takes two arguments:
#   1. A string with variable names "user_id, expected_name"
#   2. The list of data to inject
# -----------------------------------------------------------
@pytest.mark.parametrize("user_id, expected_name", test_data)
def test_verify_multiple_users(user_id, expected_name):
    url = f"https://jsonplaceholder.typicode.com/users/{user_id}"

    # Make Request
    response = requests.get(url)
    data =response.json()
    print(data)

    # Assert Status
    assert response.status_code == 200, f"User {user_id} not found!"

    # Assert Logic
    actual_name = response.json()['name']
    assert actual_name == expected_name, \
        f"Name Mismatch! Expected '{expected_name}', but got '{actual_name}'"


#
# test_data = [(7,"michael.lawson@reqres.in"),
#              (8,"lindsay.ferguson@reqres.in"),
#              (9,"tobias.funke@reqres.in"), ]
#
#
# @pytest.mark.parametrize("user_id, email", test_data)
# def test_verify_email(user_id, email):
#     url = "https://reqres.in/api/users?page=2"
#
#     response = requests.get(url)
#     print(response.json()['data'][0])
#     assert response.status_code == 200, f"User {user_id} not found!"
#
#
#     actual_email = response.json()['data'][1]['email']
#     assert actual_email == email , f"Email Mismatch! Expected '{email}', but got '{actual_email}'"

# user_id = None
# headers = {'x-api-key': 'reqres-free-v1'}
#
# @pytest.mark.dependency(1)
# def test_create_resource():
#     global user_id
#     url = "https://reqres.in/api/users"
#     payload = {
#     "name": "morpheus",
#     "job": "leader"}
#
#     # headers = {'x-api-key': 'reqres-free-v1'}
#     response = requests.post(url, json=payload,headers=headers)
#     print(response.json())
#     assert response.status_code == 201, f"User {payload['name']} not found!"
#
#
# @pytest.mark.dependency(depends=["test_create_resource"])
# def test_get_resource():
#     url = f"https://reqres.in/api/users/{user_id}"
#     response = requests.get(url,headers=headers)
#     data = response.json()
#     print(data)
#
#     # assert response.status_code == 200, f"User {user_id} not found!"
#     # assert response.json()['name'] == 'morpheus' , f"User {id} not found!"
#
# @pytest.mark.dependency(depends=["test_create_resource"])
# def test_register_resource():
#     url = "https://reqres.in/api/register"
#     payload = {
#     "email": "eve.holt@reqres.in",
#     "password": "pistol"}
#
#     response = requests.post(url,json=payload,headers=headers)
#     print(response.json())
#
# # =============================================================================================
#
# import pytest
# import requests
#
# @pytest.fixture
# def create():
#     url = 'https://reqres.in/api/users'
#     payload = {'name': "Rishwan", 'job': "Junior QA"}
#
#     # 1. Create the user
#
#     res = requests.post(url, json=payload, timeout=5)
#
#     # 2. Extract the ID
#
#     user_id = res.json()['id']
#
#     print(f"Created User ID: {user_id}")
#
#     return user_id
#
#
# def test_update_user(create):
#     user_id = create
#     payload = {'job': "Senior QA"}
#
#     res = requests.put(f'https://reqres.in/api/users/{user_id}', json=payload)
#
#     print(f"Update Status Code: {res.status_code}")
#
#     assert res.status_code == 200
# ==============================================================================================

class UserAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session =  requests.Session()
        self.session.headers = {'x-api-key': 'reqres-free-v1'}

    def create_user(self,name, job):
        url = f"{self.base_url}/api/users"
        res = self.session.post(url,json = {"name":name, "job":job})
        return res

    def update_user(self, user_id, job):
        url = f"{self.base_url}/api/users/{user_id}"
        res = self.session.put(url, json={ "job": job})
        return res

    def delete_user(self, user_id):
        url = f"{self.base_url}/api/users/{user_id}"
        res = self.session.delete(url)
        return res

@pytest.mark.parametrize("name,job",[
    ("Morpheus", "Leader"),
    ("Neo", "The One"),
    ("Trinity", "Hacker"),
])
def test_crud_workflow(name,job):
    api_client = UserAPI('https://reqres.in',)
    response = api_client.create_user(name, job)
    print(f"Server Response: {response.text}")
    assert response.status_code == 201
    new_id = response.json()['id']

    dele = api_client.delete_user(new_id)
    assert dele.status_code == 204








