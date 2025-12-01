import requests
import pytest

base_url = 'https://reqres.in/api/users'
HEADER = {'x-api-key': 'reqres-free-v1'}
query_parm  = {'page':1}

def test_get():
    response = requests.get(base_url,params=query_parm)
    data = response.json()
    # print(data)
    url = response.url
    print(url)
    assert response.status_code == 200

def test_get_resource():

    response = requests.get(base_url + "api/unknown",headers=HEADER)
    data = response.json()
    # print(data)
    print(response.headers['content-type'])






