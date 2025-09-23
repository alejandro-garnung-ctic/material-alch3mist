import os
from PIL import Image

directorio = "/mnt/c/Users/alejandro.garnung/Documents/CTIZIA/scripts/LoRA/texturas_kontext/data/transformed"

extensiones = (".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".gif")

for archivo in os.listdir(directorio):
    if archivo.lower().endswith(extensiones):
        ruta_completa = os.path.join(directorio, archivo)
        
        with Image.open(ruta_completa) as img:
            img_rgba = img.convert("RGBA")
            
            img_rgba.save(ruta_completa)

print("Todas las imágenes han sido convertidas a RGBA.")
