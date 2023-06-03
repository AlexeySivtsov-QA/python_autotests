import requests

token = '3ec18a0e5b890e32f374410f74548cc5'

answer = requests.post('https://pokemonbattle.me:9104/trainers/reg', 
json = {"trainer_token": token,
    "email": "leonardo@dolnikov.ru",
    "password": "Iloveqa1"}, 
headers = {'Content-Type': 'application/json'})

host = 'https://pokemonbattle.me:9104/'

answer_confirm = requests.post(f'{host}trainers/confirm_email', 
json = {"trainer_token": token}, 
headers = {'Content-Type': 'application/json'})

print(answer_confirm.text)