from pyrogram import Client, filters

api_id = 123
api_hash = "123"

app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.channel)
def log(client, message):
    if(message.reply_markup):
        wallet_bot_link = message.reply_markup.inline_keyboard[0][0].url
        bot_link , refereal = wallet_bot_link.split('?')
        message = f"/start {refereal.split('=')[1]}"
        app.send_message("wallet", message)


app.run()
