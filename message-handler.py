from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from spellchecker import SpellChecker

# Создаем объект SpellChecker для русского языка
spell_checker = SpellChecker(language='ru')

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот для проверки правописания на русском языке. Просто отправь мне текст для проверки.')

# Функция для проверки правописания в текстовом сообщении
def check_spelling(update, context):
    text = update.message.text

    # Получаем слова из сообщения
    words = text.split()

    # Список слов с ошибками
    misspelled = spell_checker.unknown(words)

    if misspelled:
        update.message.reply_text(f'Ошибки в тексте: {", ".join(misspelled)}')
    else:
        update.message.reply_text('Ошибок в тексте не найдено.')

def main():
    # Создаем объект Updater и передаем в него токен вашего бота
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик для текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, check_spelling))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
