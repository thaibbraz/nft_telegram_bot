from telegram.ext import *

import keys




print('Starting up bot...')


# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot to create NFT. Type /nft to create your NFT')

# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')

def nft_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')

def handle_message(update, context):
    # Get basic info of the incoming message
    message_type = update.message.chat.type
    text = str(update.message.text).lower()
    response = ''

    # Print a log for debugging
    print(f'User ({update.message.chat.id}) says: "{text}" in: {message_type}')

    # React to group messages only if users mention the bot directly
    if message_type == 'group':
        # Replace with your bot username
        if '@bot19292bot' in text:
            new_text = text.replace('@bot19292bot', '').strip()
            response = handle_response(update, new_text)
            print(response)
    else:
        response = handle_response(update, text)

    # Reply normal if the message is in private
    update.message.reply_text(response)

def handle_response(update, text) -> str:
    # Create your own response logic
    if ('hey','hi','hello') in text:
        return 'Hello there! I\'m a bot to create NFT. Type /nft to create your NFT'

    return 'I don\'t understand. Please write /start to get started again'

# Log errors
def error(update, context):
    print(f'Update {update} caused error {context.error}')


# Run the program
if __name__ == '__main__':
    updater = Updater(keys.API_KEY_TELEGRAM, use_context=True)
    dp = updater.dispatcher

    # Commands
    dp.add_handler(CommandHandler('start', start_command))
    dp.add_handler(CommandHandler('help', help_command))
    dp.add_handler(CommandHandler('nft', nft_command))

    # Messages
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()