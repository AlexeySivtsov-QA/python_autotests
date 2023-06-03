import requests

host = 'https://pokemonbattle.me:9104/'
token = '3ec18a0e5b890e32f374410f74548cc5'
contype = 'application/json'

creat_pokemons = requests.post(f'{host}pokemons',
    json = {"name": "donatelo",
        "photo": "https://dolnikov.ru/pokemons/albums/017.png"},
    headers = {'trainer_token' : token, 'Content-Type': contype})

print(creat_pokemons.text)

pokemon_id = '12747'

change_name_pokemons = requests.put(f'{host}pokemons',
    json = {"pokemon_id": pokemon_id,
        "name": "splinter",
        "photo": "https://dolnikov.ru/pokemons/albums/017.png"},
    headers = {'trainer_token' : token, 'Content-Type': contype})

print(change_name_pokemons.text)

add_pokeball = requests.post(f'{host}trainers/add_pokeball',
    json = {"pokemon_id": pokemon_id},
    headers = {'trainer_token' : token, 'Content-Type': contype})

print(add_pokeball.text)

delete_pokeball = requests.put(f'{host}trainers/delete_pokeball',
    json = {"pokemon_id": pokemon_id},
    headers = {'trainer_token' : token, 'Content-Type': contype})

print(delete_pokeball.text)

