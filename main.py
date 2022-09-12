from telegram.ext import *
import requests
import keys




print('Starting up bot...')

# Lets us use the /start command
def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot to create NFT. Type /nft to create your NFT')

# Lets us use the /help command
def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')

# Lets us use the /nft command
def nft_command(update, context):
    update.message.reply_text('Generating your NFT...')
    
    # nft variables
    nft_contract_name = "nft_name"
    nft_contract_short_name = "nft_short_name"

    url = 'https://thentic.tech/api/nfts/contract'
    headers = {'Content-Type': 'application/json'}
    data = {'key': keys.API_KEY_THENTIC,
            'chain_id': '97',
            'name': nft_contract_name, 
            'short_name': nft_contract_short_name}

    #creates NFT contract on BNB testnet
    r = requests.post(url, json=data, headers=headers)
    update.message.reply_text(r.text)
    return r.text


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

  
    # Log all errors
    dp.add_error_handler(error)

    # Run the bot
    updater.start_polling(1.0)
    updater.idle()