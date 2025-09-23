from PIL import Image

imagen = Image.new("RGB", (1024, 1024), (255, 255, 255))

imagen.save("imagen_vacia.png")

print("Imagen vacía 1024x1024 generada y guardada como 'imagen_vacia.png'")
