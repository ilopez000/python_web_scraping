import requests

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
url = "https://ejemplo.com"
nombre_archivo_salida = "pagina_descargada.html"
descargar_html(url, nombre_archivo_salida)
