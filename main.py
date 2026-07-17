import os
import discord
from discord.ext import commands
import tensorflow as tf
from tensorflow import keras
from PIL import Image, ImageOps
import numpy as np
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

model = keras.models.load_model(
    "keras_model.h5",
    compile=False
)

with open("labels.txt", "r") as f:
    class_names = f.readlines()

os.makedirs("images", exist_ok=True)

@bot.event
async def on_ready():
    print(f"Bot conectado como {bot.user}")

@bot.command()
async def analizar(ctx):
    if not ctx.message.attachments:
        await ctx.send("📷 Adjunta una imagen.")
        return

    try:
        attachment = ctx.message.attachments[0]

        image_path = f"images/{attachment.filename}"
        await attachment.save(image_path)

        image = Image.open(image_path).convert("RGB")
        image = ImageOps.fit(image, (224,224), Image.Resampling.LANCZOS)

        image_array = np.asarray(image)
        normalized_image_array = (image_array.astype(np.float32)/127.5)-1

        data = np.ndarray(shape=(1,224,224,3),dtype=np.float32)
        data[0]=normalized_image_array

        prediction=model.predict(data)

        index=np.argmax(prediction)

        confidence=prediction[0][index]*100

        result=class_names[index].strip()

        if confidence < 60:
            await ctx.send("Lo siento, no estoy seguro de lo que aparece en la imagen.")
        else:
            await ctx.send(
                f"🍽️ Creo que es **{result}**\nConfianza: {confidence:.2f}%"
            )

    except Exception:
        await ctx.send("❌ Ocurrió un error al analizar la imagen.")

bot.run(TOKEN)