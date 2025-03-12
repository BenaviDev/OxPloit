import random
import string
import hashlib
import socket
import os
from PIL import Image
from PIL.ExifTags import TAGS

# 1. Generador de contraseñas seguras
def generar_contrasena(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

print("Contraseña generada:", generar_contrasena())

# 2. Fuerza bruta simple contra un hash MD5
def fuerza_bruta_md5(hash_objetivo, diccionario):
    for palabra in diccionario:
        palabra_hash = hashlib.md5(palabra.encode()).hexdigest()
        if palabra_hash == hash_objetivo:
            print("Contraseña encontrada:", palabra)
            return
    print("No se encontró la contraseña en el diccionario.")

diccionario = ["1234", "password", "admin", "qwerty", "hack"]
hash_prueba = hashlib.md5("qwerty".encode()).hexdigest()
fuerza_bruta_md5(hash_prueba, diccionario)

# 3. Escáner de puertos básico
def escanear_puertos(ip, puertos=[21, 22, 80, 443, 3306]):
    print(f"Escaneando {ip}...")
    for puerto in puertos:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        resultado = sock.connect_ex((ip, puerto))
        if resultado == 0:
            print(f"Puerto {puerto} está ABIERTO")
        sock.close()

# Descomentar para probar con una IP conocida
# escanear_puertos("192.168.1.1")

# 4. Descubrimiento de subdominios
def encontrar_subdominios(dominio, subdominios=['www', 'mail', 'ftp', 'blog']):
    for sub in subdominios:
        subdominio = f"{sub}.{dominio}"
        try:
            ip = socket.gethostbyname(subdominio)
            print(f"{subdominio} -> {ip}")
        except socket.gaierror:
            pass

# Descomentar para probar con un dominio
# encontrar_subdominios("example.com")

# 5. Analizador de metadatos en imágenes
def extraer_metadatos(imagen_path):
    imagen = Image.open(imagen_path)
    exif_data = imagen._getexif()
    if exif_data:
        for tag_id, valor in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"{tag}: {valor}")
    else:
        print("No se encontraron metadatos en la imagen.")

# Descomentar para probar con una imagen
# extraer_metadatos("imagen.jpg")

