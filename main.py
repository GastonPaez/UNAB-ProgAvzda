import requests

r= requests.get('https://campus.unab.edu.ar')


# auth_data = {'username': '35000000', 'password': '12345'}
# resp = requests.post('https://campus.unab.edu.ar/login', data=auth_data)

print(r) # => status code
print(r.encoding) # => utf-8
print(r.text) # => HTML