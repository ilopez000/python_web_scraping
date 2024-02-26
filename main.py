import requests
from bs4 import BeautifulSoup

def descargar_html(url, nombre_archivo_salida):
    try:
        # Realiza una solicitud GET a la URL
        respuesta = requests.get(url)
        # Verifica que la solicitud fue exitosa (código de estado 200)
        if respuesta.status_code == 200:
            # Abre un nuevo archivo en modo de escritura
            with open(nombre_archivo_salida, 'w', encoding='utf-8') as archivo:
                # Escribe el contenido HTML en el archivo
                archivo.write(respuesta.text)
            print(f"El archivo '{nombre_archivo_salida}' ha sido guardado exitosamente.")
        else:
            print(f"Error al descargar la página: Código de estado {respuesta.status_code}")
    except Exception as e:
        print(f"Ocurrió un error al descargar la página: {e}")

# Ejemplo de uso
#url = "https://es.wikipedia.org/wiki/Wikipedia"
#nombre_archivo_salida = "pagina_descargada.html"
#descargar_html(url, nombre_archivo_salida)


def extraer_informacion(url):
    # Realiza la petición HTTP a la URL indicada
    respuesta = requests.get(url)

    # Verifica que la petición fue exitosa
    if respuesta.status_code == 200:
        # Parsea el contenido HTML de la respuesta utilizando BeautifulSoup
        soup = BeautifulSoup(respuesta.text, 'html.parser')

        # Busca el span con la clase 'sln-member-name' que contenga el texto 'Magdalena ADAMOWICZ'
        span = soup.find('span', class_='sln-member-name')
        partido= soup.find('h3', class_='sln-political-group-name')
        pais=soup.find('div', class_='erpl_title-h3')

        if span:
            print(span.text)
            print(partido.text)
            print(pais.text)
        else:
            print("No se encontró el elemento buscado.")
    else:
        print(f"Error al acceder a la página: {respuesta.status_code}")


# Ejemplo de uso
url = "https://www.europarl.europa.eu/meps/es/197490/MAGDALENA_ADAMOWICZ/home"
extraer_informacion(url)
