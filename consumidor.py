import requests

r = requests.get('http://localhost:5000')

cadastros = r.json()['cadastros']
print("Total de " + str(len(cadastros)) + " cadastros...")
print(cadastros)