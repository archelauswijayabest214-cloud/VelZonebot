import telebot
import os

# Token yang kamu berikan tadi
TOKEN = "8457488582:AAH1AX91Vylnk5xq0d-baxs8TZCA8ynQAjg"
bot = telebot.TeleBot(TOKEN)

# Respon saat user ketik /start
@bot.message_handler(commands=['start'])
def welcome(message):
    nama_user = message.from_user.first_name
    bot.reply_to(message, f"Halo {nama_user}! Selamat datang di **VelZonebot** 🚀\n\nBot ini sedang aktif via Cloud.")

# Respon saat user ketik /help
@bot.message_handler(commands=['help'])
def help_command(message):
    bot.reply_to(message, "Ada yang bisa dibantu? Bot ini masih dalam tahap pengembangan.")

# Respon untuk pesan teks biasa (Echo)
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"VelZonebot menerima pesan: {message.text}")

print("VelZonebot sedang berjalan...")
bot.infinity_polling()
