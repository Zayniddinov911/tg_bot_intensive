from telegram import Update
from telegram.ext import CommandHandler, Application, MessageHandler, filters, ContextTypes
from typing import Final
from datetime import datetime


TOKEN: Final = '7210389151:AAHQyUqg7EXWY5_zCJKqQr60j5lzqF03SfA'
BOT_USERNAME: Final = '@first_1_teacher_bot'

# Command handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Salom, kids!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Yordam kerak bo\'lsa kel!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Har xil custom!')

    # async def ask_time(message: types.Message):
    # now = datetime.now()
    # date_time = now.strftime("%d/%m/%y, %H:%M:%S")
    # await message.answer(date_time.title())


async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.now()
    date_time = now.strftime("%m/%y, %H:%M:%S")
    await update.message.reply_text(date_time)



# Handle the user input and respond accordingly
def handle_response(text: str) -> str:
    if 'salom' in text.lower():
        return 'Vasalam'
    if 'how are you' in text.lower():
        return 'I am good!'
    if 'i love python' in text.lower():
        return 'Don’t forget to subscribe!'
    return 'Cumadim'

# Handle messages
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text: str = update.message.text
    message_type: str = update.message.chat.type

    print(f"User ({update.message.chat.id}) in {message_type}: '{text}'")

    # Check if in group and bot is mentioned
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return
    else:
        response: str = handle_response(text)

    print('BOT:', response)
    await update.message.reply_text(response)

# Handle errors
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    print('Starting the bot...')
    
    # Create the Application
    app = Application.builder().token(TOKEN).build()
    
    # Command Handlers
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))
    app.add_handler(CommandHandler('time', time_command))

    # Message Handler
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Error Handler
    app.add_error_handler(error)

    # Start polling the bot
    print('Polling...')
    app.run_polling(poll_interval=2)
