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

# Table of Contents 

1. [Introduction](#introduction)
2. [Models](#models)
   1. [Flux1 dev](#flux1-dev)
   2. [Flux1 kontext dev](#flux1-kontext-dev)
   3. [Trellis](#trellis)
3. [Dataset](#dataset)
4. [Tools](#tools)
   1. [GPUs](#gpus)
   2. [ComfyUI](#comfyui)
   3. [AI Toolkit - OSTRIS](#ai-toolkit---ostris)
   4. [OWUI](#owui)
   5. [Python + PIL](#python--pil)
5. [Results](#results)

# Introduction

## Introduction

The **Material-Alch3mist** project arises from the need to create 3D assets rich in textures from textual descriptions, combining innovation in generative models with modular flexibility. It is an **end-to-end text-to-mesh pipeline** based on **FLUX.1 Kontext \[dev]**, specialized in generating and enhancing textures, ensuring that the final 3D meshes retain fine details and stylistically coherent materials.

The core idea of the project is based on a **modular three-stage approach**. First, base images are generated from textual prompts using **FLUX.1-dev**, producing 2D assets that are coherent with the desired scene or object. The second stage introduces a **specialized FLUX.1-Kontext dev for texture enhancement**, trained with a **lightweight LoRA** that transforms these base images into enriched versions, applying specific materials, styles, and colors. Finally, the third stage converts these textured images into **multiview 3D meshes**, ensuring that texture fidelity is preserved when transitioning from 2D to 3D.

One of the main advantages of this approach is its **flexibility and modularity**. Each stage of the pipeline can be adjusted independently: different LoRAs or FLUX variants can be incorporated, the generative flow can be finely parameterized, and new textures can be experimented with without compromising the base model. Additionally, delegating texture enhancement to a LoRA enables **fast training**, requiring only a few hours of computation and a relatively small number of image pairs, avoiding the need to retrain full models with large datasets.

The project also integrates a **testing and visualization environment**, including a repository with ComfyUI JSON configurations, ChatGPT prompts for generating texture and material variations, and a workflow that allows producing images, transforming them, and generating the final 3D mesh with ease. Optionally, a **web interface based on OWUI** is planned, where users can submit prompts, visualize results, and explore multiviews of their generated assets.

Overall, **Material-Alch3mist** represents an innovative approach to text-to-mesh generation, combining diffusion techniques, LoRA, and modular pipelines to provide an accessible, efficient, and highly customizable 3D creation experience, ideal for artistic exploration and practical applications in design and simulation environments.

# Models

Essentially, in this project we use three different models. Each serves a specific purpose and was motivated by the need to address challenges that arose during the development of the main idea driving this project: the generation of realistic and visually striking 3D objects from text.

## Flux1 dev

This model consists of BLABLABLABLA.

We have used it for BLABLABLA.

We have employed a basic workflow, available [aquí](./flows/flux-dev-basic/flux-dev-basic.json), which encapsulates its main functionalities.

## Flux1 kontext dev

This model consists of BLABLABLABLA.

We have used it for BLABLABLA.

We have employed a basic workflow, available [aquí](./flows/flux-kontext-dev-basic/flux-kontext-dev-basic.json), which encapsulates its main functionalities.

## Trellis

This model consists of BLABLABLABLA.

We have used it for BLABLABLA.

We have employed a basic workflow, available [aquí](./flows/image-to-mesh/test_image_to_mesh_trellis.json), which encapsulates its main functionalities.

# Dataset

We have created a dataset consisting of BLABLABLA

# Tools

We have employed open-source tools, both in cloud and local versions, for the implementation of the different parts of the project. Among the most relevant, we highlight the following:

## GPUs

...

## ComfyUI

....

## AI Toolkit - OSTRIS

....

## OWUI

...

## Python + PIL

Python with PIL was used to convert all images to RGBA and save them as PNG, ensuring a uniform format for the dataset, which is necessary for LoRA training and 3D texture generation.

# Results

The file [baseline_vs_enhanced](https://github.com/alejandro-garnung-ctic/material-alch3mist/blob/main/results/baseline_vs_enhanced.md) contains a compilation of the results obtained. It is referenced for consulting the experiments and their conclusions.
