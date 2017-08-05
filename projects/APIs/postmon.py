# Uso via terminal:
# Para consultar um CEP:
# python postmon.py -c 64000000
# Para verificar situacao de rastreio:
# python postmon.py -r LX404165200CN

from sys import argv
import requests
import json

script, first, second = argv
api_root = 'http://api.postmon.com.br/v1/'

def cep(input_str):
    url = api_root + 'cep/%s' % input_str
    response = requests.get(url)
    result = response.json()
    as_str = "O endereço correspondente ao CEP é %s no bairro %s da cidade de %s, no %s" % (result['logradouro'], result['bairro'], result['cidade'], result['estado_info']['nome'])
    return as_str

def rastreio(input_str):
    url = api_root + 'rastreio/ect/%s' % input_str
    response = requests.get(url)
    result = response.json()
    historico = result['historico']
    historico = historico[len(historico)-1]
    as_str = "A última informação sobre o código %s foi:\n%s em %s no local %s" % (result['codigo'], historico['situacao'], historico['data'], historico['local'])
    return as_str

if first in ['-cep', '-CEP', '-c', '-C']:
    print(cep(second))
elif first in ['-r', '-R']:
    print(rastreio(second))
else:
    print('Invalid params!')