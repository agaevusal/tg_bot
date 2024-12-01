import telebot

bot = telebot.TeleBot("7902463603:AAHkPj6gsadfPuLxNX53BFGg2qc8BaBL2R0")
@bot.message_handler(commands=['qibla'])
def main(message):
       link = "https://rawcdn.githack.com/agaevusal/base-of-python/41bf6e593322e9a5b6786d6ccc4afe9203f994df/map.html"
       link_2 = 'https://drive.google.com/file/d/1PfUCZoDm5k0Vd0Oe-iDrtPhXYYFET7gE/view?usp=drive_link'
       bot.send_message(message.chat.id, link, parse_mode='html')
bot.infinity_polling()

