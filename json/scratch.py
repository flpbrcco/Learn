import json
import requests

cidade = requests.get("https://servicodados.ibge.gov.br/api/v1/localidades/municipios/timoteo")

a = cidade.json()

print("Retorno API: " + str(a))

# data = {'test1': '1', 'test2': '2', 'test3': '3'}
#
# json_str = json.dumps(data)
#
# resp = json.loads(json_str)
#
# print(resp)
#
# print(resp['test1'])

b = json.dumps(a)

c = json.loads(b)

print('Retorno id:' + (str(c['id'])))
