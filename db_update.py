import requests

word_list = open("words.txt")

"""
r = requests.post('http://127.0.0.1:5000/insert', data={'Key': 'value'})
print(r.text)

r = requests.post('http://127.0.0.1:5000/insert', data={'Key': 'val'})
print(r.text)

r = requests.post('http://127.0.0.1:5000/insert', data={'Key': 'hello'})
print(r.text)

r = requests.post('http://127.0.0.1:5000/find', data={'Key': 'value'})
print(r.text)

r = requests.post('http://127.0.0.1:5000/find', data={'Key': 'val'})
print(r.text)

r = requests.post('http://127.0.0.1:5000/delete', data={'Key': 'val'})
print(r.text)

r = requests.post('http://127.0.0.1:5000/find', data={'Key': 'val'})
print(r.text)

"""

#for i in word_list:
#    r = requests.post('http://127.0.0.1:5000/insert', data={'Key': i.strip()})

r = requests.post('http://127.0.0.1:5000/autocomplete', data={'Key': 'became'})
print(r.text)

