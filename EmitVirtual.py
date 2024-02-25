import os
import requests
import datetime
import json

with open('config.json','r') as f:
    config = json.load(f)
    
instanceName = config['instanceName']
login = config['login']
password = config['password']

print(f'Авторизуемся под учетной записью {login}'+'\n')

url = f'{instanceName}/authorizationservice/token'
body = f'grant_type=password&username={login}&password={password}&area=Default'

response = requests.post(url,data=body).json()

print('Получили токен'+'\n')

token = response['access_token']

print('я здесь')



for i in range(1):
    url = f'{instanceName}/publicapi/api/v1.2/Cards/EmitVirtual'
    headers = {'Authorization': 'Bearer '+token, 'Content-Type': 'application/json'}
    response = requests.post(url,headers=headers,data=body).json()
    print(datetime.datetime.now(),' ',response,'\n')
