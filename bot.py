import logging
import telebot
from telebot import types

API_TOKEN = 'NODZ5srU'

logging.basicConfig(level=logging.INFO)

bot = telebot.TeleBot(API_TOKEN)

rules_dict = {
    "П1": "🌟 Любые оскорбления и провокации запрещены [мут 60-180+варн]",
    "П2": "🚫 Спам/флуд [мут 60-120+варн]. Общение только на русском/украинском/английском языках.",
    "П3": "⛔ Оскорбление родителей [бан😐]",
    "П4": "⚙️ Копание, открывание кейсов и создание зелий в личных сообщениях бота [мут 30]",
    "П5": "🔞 Любой контент 18+ в любом виде [мут 120-180+варн]. Зоофилия и т.д. также запрещены, как в обычных сообщениях, так и в гифках и стикерах.",
    "П6": "📣 Политические дискуссии, ссоры и разногласия решаются в личных сообщениях [мут 60-120+варн]",
    "П7": "🕗 Скримаки запрещено отправлять после 20:00 по мск [мут 60]",
    "П8": "📛 Реклама запрещена. Чтобы поделиться ссылкой на видео и т.д., спросите разрешение у админов [мут 60-180+варн]",
    "П9": "🚫 Раскрытие ссылок на чат и информации о клане [бан☠️]",
    "П10": "🛑 Запрещено отправлять что-то, из-за чего вылетает тг или взлом [мут 60+варн-бан👩‍💻]",
    "П12": "🚷 Не размещайте в группе фотографии, видео или другие данные другого человека без его разрешения [мут 60-бан🫤]",
    "П17": "(Присутствует [1-60 минут (модераторам - 30)])"
}

@bot.message_handler(regexp=r'^Правило \d+$')
def send_rule_by_number(message):
    rule_number = message.text.split()[1]
    rule_key = f"П{rule_number}"
    if rule_key in rules_dict:
        rule_text = rules_dict[rule_key]
        bot.reply_to(message, rule_text, parse_mode='Markdown')
    else:
        bot.reply_to(message, "Такого правила не существует.")

@bot.message_handler(regexp=r'^П\d+$')
def send_rule_by_number(message):
    rule_number = message.text[1:]
    rule_key = f"П{rule_number}"
    if rule_key in rules_dict:
        rule_text = rules_dict[rule_key]
        bot.reply_to(message, rule_text, parse_mode='Markdown')
    else:
        bot.reply_to(message, "Такого правила не существует.")

@bot.message_handler(regexp=r'^Правила$')
def send_all_rules(message):
    rules_text = "Список всех правил:\n\n" + "\n\n".join([f"{key}: {value}" for key, value in rules_dict.items()])
    bot.reply_to(message, rules_text, parse_mode='Markdown')

if __name__ == '__main__':
    bot.polling(none_stop=True)
