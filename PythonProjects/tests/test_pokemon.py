import requests
import pytest

HOST = 'https://api.pokemonbattle.me:9104'

def test_status_code():
    response = requests.get(url=f'{HOST}/trainers')
    assert response.status_code == 200
    
def test_name_trainer():
    response = requests.get(f'{HOST}/trainers', params= { 'trainer_id' : 2716}, timeout=5)
    assert response.json()['trainer_name'] == 'Lil'
