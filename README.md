# 🤖 Discord Imagen Clasificación Bot

🚀 Bot de Discord capaz de analizar y clasificar imágenes utilizando un modelo de inteligencia artificial previamente entrenado.

Este proyecto combina **Discord.py** con un modelo de clasificación de imágenes para permitir que los usuarios envíen imágenes al bot y reciban una predicción sobre la categoría a la que pertenece la imagen.

---

## 📌 Descripción

El bot funciona como un asistente inteligente dentro de Discord. Su principal objetivo es recibir imágenes enviadas por los usuarios, procesarlas y utilizar un modelo de Machine Learning entrenado para identificar y clasificar el contenido visual.

Cuando un usuario envía una imagen:

1. 📷 El bot recibe la imagen dentro de un canal de Discord.
2. 🔎 Procesa la imagen para adaptarla al formato requerido por el modelo.
3. 🧠 El modelo entrenado analiza las características de la imagen.
4. ✅ El bot devuelve la categoría predicha junto con la confianza de la clasificación.

El modelo utilizado fue entrenado con un conjunto de imágenes etiquetadas, permitiendo que la inteligencia artificial aprenda patrones visuales y pueda realizar nuevas predicciones sobre imágenes que nunca había visto.

---

## ✨ Características

- 🤖 Integración con Discord mediante Discord.py.
- 🖼️ Clasificación automática de imágenes.
- 🧠 Uso de un modelo de inteligencia artificial entrenado.
- 📊 Predicciones basadas en categorías aprendidas.
- ⚡ Respuesta automática dentro del servidor.
- 🔒 Uso seguro del token mediante variables de entorno.

---

## 🛠️ Tecnologías utilizadas

- Python 🐍
- Discord.py
- TensorFlow / Machine Learning
- Python-dotenv
- Pipenv

---

## 📂 Estructura del proyecto
