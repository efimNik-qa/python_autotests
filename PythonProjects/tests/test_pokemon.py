import requests
import pytest

def test_status_code():
    response = requests.get(url='https://api.pokemonbattle.me:9104/trainers', params={'trainer_id':2545}, timeout=5)
    assert response.status_code == 200
    assert response.json()['trainer_name'] == 'Fifa'