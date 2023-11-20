import requests


response = requests.post(url='https://api.pokemonbattle.me:9104/pokemons', 
                          json={
                         "name": "generate",
                         "photo": "generate"
                         },
                         headers={'Content-Type': 'application/json', 'trainer_token': 'b4b337e60ee7b7532343f67e8792ad91'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')



response = requests.put(url='https://api.pokemonbattle.me:9104/pokemons', 
                          json={
                         "pokemon_id": "20010",
                          "name": "generate",
                          "photo": "generate"
                         },
                         headers={'Content-Type': 'application/json', 'trainer_token': 'b4b337e60ee7b7532343f67e8792ad91'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')


response = requests.post(url='https://api.pokemonbattle.me:9104/trainers/add_pokeball', 
                           json={
                         "pokemon_id": "20010"
                          },
                          headers={'Content-Type': 'application/json', 'trainer_token': 'b4b337e60ee7b7532343f67e8792ad91'}, timeout=5)

print(f'Code: {response.status_code} - {response.reason}. Message: {response.text}')