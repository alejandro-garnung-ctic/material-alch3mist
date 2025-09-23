import os
from PIL import Image

directorio = "/mnt/c/Users/alejandro.garnung/Downloads/img0-20250922T113605Z-1-001/img0"

extensiones = (".jpg", ".jpeg", ".bmp", ".tiff", ".gif", ".png")

for archivo in os.listdir(directorio):
    if archivo.lower().endswith(extensiones):
        ruta_completa = os.path.join(directorio, archivo)
        
        with Image.open(ruta_completa) as img:
            img_rgba = img.convert("RGBA")
            
            nombre_sin_ext = os.path.splitext(archivo)[0]
            nueva_ruta = os.path.join(directorio, f"{nombre_sin_ext}.png")
            img_rgba.save(nueva_ruta, "PNG")
        
        if not archivo.lower().endswith(".png"):
            os.remove(ruta_completa)

print("Todas las imágenes han sido convertidas a RGBA y guardadas como PNG en la misma carpeta.")
