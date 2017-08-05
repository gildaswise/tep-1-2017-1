# Uso via terminal:
# Para retornar uma trivia:
# python numbers-api.py -t 42
# Para retornar um fato matematico:
# python numbers-api.py -m 42
# Para informacao sobre alguma data: (use datas no formato brasileiro dia/mes)
# python numbers-api.py -d 5/8

from sys import argv
import requests
import json

script, first, second = argv
api_root = 'http://numbersapi.com/'

def number_trivia(num):
    response = requests.get(api_root + '%s/trivia' % num)
    return response.text

def number_math(num):
    response = requests.get(api_root + 'http://numbersapi.com/%s/math' % num)
    return response.text

def number_date(num):
    if '/' in num:
        day, month = num.split('/')
        response = requests.get(api_root + 'http://numbersapi.com/%s/%s/date' % (month, day))
        return response.text
    else:
        return 'Invalid date provided!'

if first in ['-t', '-T']:
    print(number_trivia(second))
elif first in ['-m', '-M']:
    print(number_math(second))
elif first in ['-d', '-D']:
    print(number_date(second))
elif first.isnumeric:
    print(number_trivia(first))
else:
    print('Invalid params!')
