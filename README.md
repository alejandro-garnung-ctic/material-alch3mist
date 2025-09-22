# material-alch3mist
An end-to-end text-to-mesh FLUX.1 Kontext [dev]-based diffusion model specialized on texture generation

# (PARA DESARROLLO) Pipeline:

- [ ] Repo con JSON de comfy + README + algo de owui
- [ ] Brief explanation
- [ ] Text description
- [ ] Demo video: comfyui explicar el flujo + Lora... y al final prueba de concepto con asistente conversacional en OWUI
- [ ] URL a los pesos del modelo (en HF o como Release de Git)

Flujo

1. pedir chatgpt prompts para imagenes con texturas y materiales variados y singulares (5-10)
2. reservar 10 imagenes para test
3. inyectarlos en FLUX-dev de comfy para generar img_0 (50 aprox)
4. meter imagenes_0 a 3D model para tener base
5. meter img_0 a flux kontext + prompt de enhacing texture -> imagenes con mejor textura img_1
6. meter al LoRa las imagenes + prompts del paso 1
7. entrenar el LoRa con los pares de imagenes img_0 - img_1
8. volver a pasar los prompts una vez entrenado el lora por todo el flujo hasta el mesh y comparar
   
wizard -> todos los pasos

flux-dev-basic -> prompts de chatGPT -> cambiar nombre a img0_001.jpg

> [!NOTE]
> En la carpeta `/data`:
> 
> /img0 == /original
> 
> /img1 == /transformed

# (PARA DESARROLLO) Idea general

- Idea general: Se trata de la generación text-to-mesh; se generan activos 3D a partir de prompts especialmente enfocados en la generación de texturas particulares. Se sigue un enfoque en tres grandes pasos.

  - En primera instancia, podríamos pensar en entrenar un modelo de difusión/generativo end-to-end text-to-3D. Pero esto tiene sus inconvenientes, como costo y complejidad computacional y no hay tantas soluciones open source practicables aún. Menos en ComfyUI. Así que como primer workaround hemos pensado en sustituir el end-to-end por dos etapas, primero una generación text-to-image con Flux.1-dev y luego la generación multivista, triplano y 3d mesh con modelos como Trellis o InstantMesh. 

  - Pero hemos notado que la anterior configuración simple flojea al generar la textura de las mallas, y en vez de modificar la arquitectura o los parámetros del paso 3D, hemos decidido agregar un nuevo elemento a la etapa 2D que nos mejore esto. En esta nueva etapa añadimos un Flux1-kontext dev especializado en el perfeccionamiento de las texturas 2D a través de un LoRA entrenado en la potenciación de materiales, colores, etc. De esta forma, el primer FLUX genera la imagen fuente coherente y sin sesgo de estilo y el FLUX+LoRA consiguiente transforma esa imagen en una versión especializada (e.g. texturizada, con material aplicado, un estilo creativo…). Luego, el pipeline image=>mesh convierte esta imagen texturizada en una malla 3D final.

- Una ventaja de este enfoque es que es modular y flexible. Se pueden desenchufar y enchufar adaptadores LoRA o modelos FLUX a gusto, así como parametrizar a granularidad fina cualquiera de las etapas, sin modificar su compartamiento particular pero alterando conscientemente el funcionamiento general de todo el pipeline generativo. La arquitectura queda auto-orquesta. Otra ventaja de dedicar una etapa particular a la potenciación de la textura 2D es que así el salto 2D a 3D no la menoscaba, sino que se enfocará más aún en la generación fiel y de detalles finos de la misma. Otra ventaja es que hacer recaer la responsabilidad de la generación de textura en el LoRA nos permite disponer de tiempos de entrenamiento muy cortos, de pocas horas, en comprarción con lo que sería reentrenar o finetunear un FLUX1-kontext dev entero con un dataset personalizado.

- Entrenamiento del Lora con OSTRIS sobre FLUX.1 (Imagen → Imagen con transformación). No necesitamos millares de datos, basta con 50–200 pares consistentes. Ajustar rank=8–16, lr=1e-4, entrenar 2–4h (dependiendo dataset). Para validación, generar outputs con prompts nuevos para ver si realmente aplica el “efecto”. Para generar los pares de entrenamiento, se puede:

  - Generar objetos base con FLUX.1 DEV (ej: “simple chair, plain white plastic”) (e.g. con el flujo flux_dev_basic.json).

  - Editar (poco a poco) con prompts en el flujo flux_kontext_dev_basic.json o Stable Diffusion XL para aplicar material e ir guardando las imágenes originales, edits y prompts.

  - Para que el LoRA entre en acción hay que especificar la trigger Word que irá en los prompts del usuario. Esta trigger words activarán, en tiempo de inferencia (generación), el estilo que está aprendiendo el LoRA para que el modelo aplique el estilo. Por ejemplo, podemos poner “Alch3mist” como trigger Word y los prompts serán del tipo “Material Alch3mist, genérame una vaca con piel de cocodrilo y con una melena en llamas”.

  - Opcionalmente recortar y normalizar imágenes a 512–768-1024px y guardar los prompts con los que se han generado las imágenes transformadas para conformar los datasets de entrenamiento y control. E.g. unas 25 imágenes por material, con unos 5 materiales (total 125 imágenes).

  - Preparar la API => quizá una pequeña aplicación web (o bien usar OWUI directamente, y así aprovechamos la visualización de la malla) en la que subir el prompt y recibir el 3D y la imagen generada, así como las multivista. Así llamamos a nuestros servicios de CTIZ con simples consultas remotas y evitamos replicar el setup en otros equipos (¿hacer que se requiera clave pública/privada proporcionada por nosotros para usarlos?).

# Models

...

## Flux1 dev

...

## Flux1 kontext dev

...

## Trellis

...

# Tools

...

## ComfyUI

....

### flux-dev-basic.json

...

### flux-kontext-dev-basic.json

...

### image-to-mesh.json

...

### flux-kontext-texture-wizar3d-basic.json

...

## AI Toolkit - OSTRIS

....


## OWUI

...
