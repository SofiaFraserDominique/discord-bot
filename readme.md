# 🤖 Bot de Discord - Juego de Preguntas

Este proyecto es un **bot de Discord** que recibe un código encriptado desde Fortnite, lo desencripta y muestra un reporte formateado sobre las respuestas del candidato.

---

## 🚀 Funcionalidades
- Desencripta un código enviado desde Fortnite.
- Muestra el camino elegido (JAVA, IOS, ANDROID).
- Indica si la respuesta de la pregunta fue correcta o incorrecta.
- Da una breve descripción del conocimiento validado.
- Permite crecer fácilmente: las preguntas están en `questions.json`.

---

## 📂 Estructura del proyecto

discord-bot/
│── bot.py # Código principal del bot
│── questions.json # Preguntas y descripciones en español
│── requirements.txt # Dependencias de Python
│── .env.example # Variables de entorno (ejemplo)
│── README.md # Este archivo

yaml
Copiar código

---

## ⚙️ Instalación local

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/tu-usuario/discord-bot.git
   cd discord-bot
Crear un archivo .env con tu token de bot:

env
Copiar código
DISCORD_BOT_TOKEN=tu_token_aqui
Instalar dependencias:

bash
Copiar código
pip install -r requirements.txt
Ejecutar el bot:

bash
Copiar código
python bot.py