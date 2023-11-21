import requests

response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
                          json= {                                        
    "name": "generate",
    "photo": "generate",
},
headers={'Content-Type': 'application/json',
         "trainer_token": "6a47209661bebe16d767690e6c60c945"
         }, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text} ')


response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
                          json={
    "pokemon_id": "12720",
    "name": "Rabbit",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png",
},
headers={'Content-Type': 'application/json',
         "trainer_token": "6a47209661bebe16d767690e6c60c945"}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text} ')


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                          json={
    "pokemon_id": "12720"
},
headers={'Content-Type': 'application/json',
         "trainer_token": "6a47209661bebe16d767690e6c60c945"}, timeout=5)
print(f'Code: {response.status_code} - {response.reason}. Message: {response.text} ')



