import os
import json
import disnake as discord
from dotenv import load_dotenv

# ======================
# ENCRIPTAR / DESENCRIPTAR
# ======================
Alfabeto  = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
             "N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
             "a","b","c","d","e","f","g","h","i","j","k","l","m",
             "n","o","p","q","r","s","t","u","v","w","x","y","z",
             "0","1","2","3","4","5","6","7","8","9",
             " ", ".", ",", "!", "?", "@", "#", "%", "&", "(", ")", "-", "_", "=", "+"]

Cripto = ['O', 'D', 'j', 'f', 'c', 'R', 'N', '%', 'L', '2', 'E', '=', '#', 'b', 
          '+', 'g', 'm', 'B', '_', 'M', 't', 'p', 's', 'i', 'a', ' ', ')', 
          'l', '(', 'A', 'K', '@', '.', 'V', 'w', 'J', '&', 'r', 'G', 'F', 'Y', 
          '8', 'W', '1', 'Q', 'C', 'X', 'z', 'q', '!', '5', '-', 'y', '3', 'U', 
          'T', ',', 'S', '6', 'Z', '7', 'H', '0', '?', '9', '4', 'd', 'n', 'o', 
          'P', 'x', 'k', 'u', 'e', 'I', 'v', 'h']

def decrypt(text: str) -> str:
    result = ""
    for ch in text:
        if ch in Cripto:
            idx = Cripto.index(ch)
            result += Alfabeto[idx]
        else:
            result += ch
    return result


# ======================
# CARGAR PREGUNTAS
# ======================
with open("question.json", "r", encoding="utf-8") as f:
    PREGUNTAS = json.load(f)


# ======================
# DISCORD BOT
# ======================
load_dotenv()
TOKEN = os.getenv("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"✅ Bot en línea como {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # Ejemplo: !Run <codigo_encriptado>
    if message.content.startswith("!Run "):
        encrypted = message.content[len("!Run "):].strip()
        decrypted = decrypt(encrypted)

        try:
            camino, pregunta_id, resultado = decrypted.split("_")

            camino = camino.upper()
            descripcion = PREGUNTAS.get(camino, {}).get(pregunta_id, "Pregunta desconocida")

            acierto = "✅ Correcto" if resultado in ["1", "true", "True"] else "❌ Incorrecto"
            feedback = (
                f"-> Candidato: {message.author.mention}\n"
                f"-> Camino elegido: {camino}\n"
                f"-> Pregunta {pregunta_id}: {acierto}\n"
                f"-> Descripción: {descripcion if 'Correcto' in acierto else 'El candidato no domina este conocimiento'}"
            )

            await message.reply(feedback)

        except Exception as e:
            await message.reply(f"⚠️ Error al procesar: {e}")


client.run(TOKEN)
