
### Requests
```
r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
r.status_code
200
r.headers['content-type']
'application/json; charset=utf8'
r.encoding
'utf-8'
r.text
'{"type":"User"...'
r.json()
{'private_gists': 419, 'total_private_repos': 77, ...}
```
### Requests (Solcitudes)
> Permite enviar solicitudes HTTP. Facilita el envio sin codificacion ya que usa
> urllib3 

### Solicitud GET
```
import requests
resp = requests.get('https://www.google.com/')
```
> La función devuelve un objeto Response, que en este caso se ha asignado a la variable resp, con toda la información de la respuesta.

### Solicitud POST

```
import requests

auth_data = {'email': 'prueba@mail.com', 'pass': '1234'}
resp = requests.post('https://mipagina.xyz/login/', data=auth_data)
```