## HTTP

<table>
    <thead>
        <tr>
            <th></th>
            <th text="bold">HTTP</th>
            <th></th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td align="center">Peticion</td>
            <td align="center">URL PATH</td>
            <td align="center">VERSION</td>
        </tr>
        <tr>
            <td align="center"></td>
            <td align="center">HEADERS</td>
            <td align="center"> </td>
        </tr>
         <tr>
            <td align="center"></td>
            <td align="center">BODY</td>
            <td align="center"> </td>
        </tr>
    </tbody>
</table>

> POST | /login | 1.1
>
> "host" https://api.github.com | User-Agent: "Chrome/97.0" | "accept":"text/html" | "accept-language":"es-ES"
>
>{ "username":"GastonDev", "password":"UNAB1234" }

| PETICION | | 
| --- | --- | 
| GET | Solicita un recurso |
| POST | Envia informacion |
| PUT | Reemplaza informacion | 
| DELETE | Elimina un recurso | 
| HEAD | Solicita solo los HEADERS | 
| CONNECT | Abre conexion con un recurso | 
| OPTIONS | Obtiene las peticiones disponibles | 
| TRACE | Prueba un bucle de retorno | 
| PATH | Edita un recurso | 
|| 


| | CODIGO DE RESPUESTA | |
|:-:|:-:|:-:| 
| | VERSION | CODIGO DE RESPUESTA|
| | 1-- | respuesta informativa |
| | 2-- | respuesta correcta |
| | 3-- | redireccion | 
| | 4-- | error del Cliente | 
| | 5-- | error del Servidor | 
|| 

