import requests
import pytest

host = 'https://pokemonbattle.me:9104/'
token = '3ec18a0e5b890e32f374410f74548cc5'
contype = 'application/json'

def test_status_code():
    answer = requests.get(f'{host}trainers',
    headers = {'trainer_token' : token, 'Content-Type': contype})
    assert answer.status_code == 200

def test_part_of_answer():
    answer_body = requests.get(f'{host}trainers', params = {'trainer_id' : 4636})
    assert answer_body.json()['trainer_name'] == 'leonardo'

@pytest.mark.parametrize('key, value', [('trainer_name', 'leonardo'),
                                        ('city', 'chicago'),
                                        ('get_history_battle', '0'),
                                        ('level', '1')])

def test_parts_of_answer(key, value):
    answer = requests.get(f'{host}trainers', params = {'trainer_id' : 4636})
    assert answer.json()[key] == value
