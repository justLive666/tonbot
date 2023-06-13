from pyrogram import Client, filters

api_id = 13123638
api_hash = "36bf1242c1911d63585d01543424efe7"

app = Client("my_account", api_id=api_id, api_hash=api_hash)


@app.on_message(filters.channel)
def log(client, message):
    if(message.reply_markup):
        wallet_bot_link = message.reply_markup.inline_keyboard[0][0].url
        bot_link , refereal = wallet_bot_link.split('?')
        message = f"/start {refereal.split('=')[1]}"
        app.send_message("wallet", message)


app.run()
