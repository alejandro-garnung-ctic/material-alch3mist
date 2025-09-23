import os
from PIL import Image

directorio = "/mnt/c/Users/alejandro.garnung/Downloads/foo"

extensiones = (".jpg", ".jpeg", ".bmp", ".tiff", ".gif", ".png")

tamano_objetivo = (1024, 1024)

for archivo in os.listdir(directorio):
    if archivo.lower().endswith(extensiones):
        ruta_completa = os.path.join(directorio, archivo)
        
        with Image.open(ruta_completa) as img:
            img_rgba = img.convert("RGBA")
            
            if img_rgba.size != tamano_objetivo:
                img_rgba = img_rgba.resize(tamano_objetivo, Image.LANCZOS)
            
            nombre_sin_ext = os.path.splitext(archivo)[0]
            nueva_ruta = os.path.join(directorio, f"{nombre_sin_ext}.png")
            img_rgba.save(nueva_ruta, "PNG")
        
        if not archivo.lower().endswith(".png"):
            os.remove(ruta_completa)

print("Todas las imágenes han sido convertidas a RGBA, redimensionadas a 1024x1024 y guardadas como PNG en la misma carpeta.")
