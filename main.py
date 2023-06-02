import telebot  # telegram API библиотека
import os
from dotenv import load_dotenv  # для чтения .env
load_dotenv()

# поднимаем наш бот. `os.environ.get('TELEBOT')` это токен нашего бота, который мы берем из файла .env
# почему .env? -- для безопасности. токен должен быть известен только разработчику бота,
# в случае его утечки злоумышленники смогут перепрограммировать бот как им хочется
bot = telebot.TeleBot(os.environ.get('TELEBOT'))


# message_handler ловит любые сообщения которые может увидеть бот в чате.
# данный хендлер реагирует только на сообщения в которых есть `hello` или `bye` как можно видеть в regexp
@bot.message_handler(regexp=r'(?i)\b(hello|bye)\b')
def respond(message):
    text = message.text.lower()     # обрабатываем полученное сообщение

    if "hello" in text:
        response = "Hi there!"

    elif "bye" in text:
        response = "Goodbye!"

    # отправляем ответ бота на сообщение обратно в чат
    bot.send_message(chat_id=message.chat.id, text=response)


# запускаем бот. теперь он работает пока сам скрипт руками не выключить (или пока нет ошибок)
bot.polling(none_stop=True, interval=0)
