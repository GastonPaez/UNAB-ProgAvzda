import requests

class Provincia:
    def __init__(self, nombre, latitud, longitud):
        self.nombre = nombre
        self.latitud = latitud
        self.longitud = longitud

    def __str__(self):
      return f"Provincia: {self.nombre}, Latitud: {self.latitud}, Longitud: {self.longitud}"

    def __repr__(self):
        return f"{self.nombre} (Lat: {self.latitud}, Long: {self.longitud})"

class ProvinciaManager:
    def __init__(self, url):
        self.url = url
        self.provincias = []              

    def convertir_datos(self):
        response = requests.get(self.url)
        data = response.json()
        for item in data['provincias']:
            provincia = Provincia(
                nombre=item['nombre'],
                latitud=item['centroide']['lat'],
                longitud=item['centroide']['lon']
            )
            self.provincias.append(provincia)

    def clasificar_pcia_latitud(self, latitud_limite):
        self.lat_alta = []
        self.lat_baja = []  
        for provincia in self.provincias:
            if provincia.latitud > latitud_limite:
                self.lat_alta.append(provincia)
            else:
                self.lat_baja.append(provincia)
        print(f"\nProvincias con latitudes altas: {self.lat_alta}")
        print(f"\nProvincias con latitudes bajas: {self.lat_baja}")
                
    def clasificar_pcia_longitud(self, longitud_limite):
        self.long_alta = []
        self.long_baja = []
        for provincia in self.provincias:
            if provincia.longitud > longitud_limite:
                self.long_alta.append(provincia)
            else:
                self.long_baja.append(provincia)
        print(f"\nProvincias con longitudes altas: {self.long_alta}")
        print(f"\nProvincias con longitudes bajas: {self.long_baja}")

    def mostrar_provincias(self):
        print(f"\nTotal de provincias: {len(self.provincias)}")
        print(f"\nNombres de provincias: {[provincia.nombre for provincia in self.provincias]}")


    def pcia_lat_cercana(self, latitud_objetivo):
        provincia_cercana = None
        menor_diferencia = float('inf')
        for provincia in self.provincias:
            diferencia = abs(provincia.latitud - latitud_objetivo)
            if diferencia < menor_diferencia:
                menor_diferencia = diferencia
                provincia_cercana = provincia
        return provincia_cercana
    
    def pcia_lon_cercana(self, longitud_objetivo):
        provincia_cercana = None
        menor_diferencia = float('inf')
        for provincia in self.provincias:
            diferencia = abs(provincia.longitud - longitud_objetivo)
            if diferencia < menor_diferencia:
                menor_diferencia = diferencia
                provincia_cercana = provincia
        return provincia_cercana

# URL específica
url = 'https://apis.datos.gob.ar/georef/api/provincias'

# Crear instancia de ProvinciaManager
manager = ProvinciaManager(url)

# Obtener datos de la api para completar la informacion de las provincias
manager.convertir_datos()

# Mostrar resultados obtenidos
manager.mostrar_provincias()

# Clasificar provincias por latitud dada
manager.clasificar_pcia_latitud(latitud_limite=-41.1649750616583)

# Clasificar provincias por longitud dada
manager.clasificar_pcia_longitud(longitud_limite=-69.9557619144913)

# Encontrar la provincia más cercana a una latitud dada
latitud_objetivo = -34.6037
provincia_cercana = manager.pcia_lat_cercana(latitud_objetivo)
print(f"\nLa provincia más cercana a la latitud {latitud_objetivo} es: {provincia_cercana}")

# Encontrar la provincia más cercana a una longitud dada
longitud_objetivo = -46.6037
provincia_cercana = manager.pcia_lon_cercana(longitud_objetivo)
print(f"\nLa provincia más cercana a la longitud {longitud_objetivo} es: {provincia_cercana}")