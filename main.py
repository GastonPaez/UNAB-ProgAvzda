import requests

url = 'https://campus.unab.edu.ar' 
res= requests.get(url) # => Objeto donde vamos a almacenar la respuesta
""" 
print(dir(res)) # => metodos disponibles
['__attrs__', '__bool__', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__enter__', '__eq__',
'__exit__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__', '__init__',
'__init_subclass__', '__iter__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__nonzero__',
'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', '__str__',
'__subclasshook__', '__weakref__', '_content', '_content_consumed', '_next', 'apparent_encoding', 'close',
'connection', 'content', 'cookies', 'elapsed', 'encoding', 'headers', 'history', 'is_permanent_redirect',
'is_redirect', 'iter_content', 'iter_lines', 'json', 'links', 'next', 'ok', 'raise_for_status', 'raw',
'reason', 'request', 'status_code', 'text', 'url']
"""

# auth_data = {'username': '35000000', 'password': '12345'}
# resp = requests.post('https://campus.unab.edu.ar/login', data=auth_data)

print(res) # => status code
print(res.encoding) # => utf-8
# print(r.text) # => HTML