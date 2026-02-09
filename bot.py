import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = "PASTE_YOUR_BOT_TOKEN_HERE"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(
        message.chat.id,
        "🎮 Welcome to BGMI UC Store\n\n🆔 Apna BGMI Game ID bhejo"
    )

@bot.message_handler(func=lambda m: m.text.isdigit())
def verify_id(message):
    game_id = message.text

    text = f"""
✅ ID Verified Successfully
👤 Player: DemoPlayer
🆔 Game ID: {game_id}

🎁 Select UC Package:
"""

    kb = InlineKeyboardMarkup()
    kb.add(
        InlineKeyboardButton("350 UC ₹99", callback_data="350"),
        InlineKeyboardButton("800 UC ₹249", callback_data="800")
    )
    kb.add(
        InlineKeyboardButton("1800 UC ₹399", callback_data="1800"),
        InlineKeyboardButton("❌ Cancel", callback_data="cancel")
    )

    bot.send_message(message.chat.id, text, reply_markup=kb)

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data == "cancel":
        bot.send_message(call.message.chat.id, "❌ Cancelled")
    else:
        bot.send_message(
            call.message.chat.id,
            f"💳 UPI Payment karo\n📸 Screenshot bhejo\n\nUC: {call.data}"
        )

bot.infinity_polling()
