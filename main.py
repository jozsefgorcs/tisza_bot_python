import os

from telegram import Update
from telegram.ext import Application, Updater, CommandHandler, CallbackContext

from tisza_downloader import download_shoes_by_size


# Define the command handler function
async def kifuto_command(update: Update, context: CallbackContext) -> None:
    # Get the parameter from the command
    if len(context.args) > 0 and is_number(context.args[0]):
        size = int(context.args[0])

        await update.message.reply_text(f'Python tisza bot. Kifutó cipők {size} méretben:')
        shoes = download_shoes_by_size(size)
        if(len(shoes) == 0):
            await update.message.reply_text(f'Nincsenek cipők {size} méretben')

        for shoe in shoes:
            await update.message.reply_text(shoe.print_to_message())
    else:
        await update.message.reply_text('Így használd: /kifuto 45 ')


def is_number(value):
    try:
        int(value)
        return True
    except ValueError:
        return False


def main() -> None:
    bot_token = os.environ.get('TELEGRAM_BOT_TOKEN', None)
    if(bot_token is None):
        raise Exception('TELEGRAM_BOT_TOKEN env var is missing')
    application = Application.builder().token(bot_token).build()
    application.add_handler(CommandHandler("kifuto", kifuto_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()