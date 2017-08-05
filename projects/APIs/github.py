# coding: utf-8
# Uso via terminal: 
# Para informações sobre o perfil:
# python github.py -u <username>
# Para ver os repositórios:
# python github.py -r <username>

from sys import argv
import requests # pip install requests
import iso8601 # pip install iso8601
import json
from datetime import datetime

script, first, second = argv

api_root = 'https://api.github.com/'

def get_profile(input_str):
    url = (api_root + 'users/%s' % second)
    response = requests.get(url)
    result = response.json()
    date = iso8601.parse_date(result['created_at'])
    as_str = "The user requested is @%s\nYou can visit their blog here: %s\nTheir full name is %s\nMember since %s" % (result['login'], result['blog'], result['name'], date.year)
    return as_str

def get_repos(input_str):
    url = (api_root + 'users/%s/repos' % second)
    response = requests.get(url)
    result = response.json()
    as_str = "@%s has %s repos! The most recent one is %s" % (second, len(result), result[0]['name'])
    return as_str

if first in ['-u', '-U']:
    print(get_profile(second))
elif first in ['-r', '-R']:
    print(get_repos(second))
else:
    print('Invalid options provided!')