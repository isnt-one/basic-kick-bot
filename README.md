# basic kick bot
 This is just an experiment created out of boredom to learn python more and to learn how the initial kick api worked.

### Dependencies:
 * curl_cffi
 * pysher

### Setup:
 * Install the dependencies through your package manager
 * Modify `CHANNEL_USERNAME`, `BOT_USERNAME`, and `BOT_PASSWORD` in the `app.py` file.
 * Add your own commands through `chat_socket.add_command` in `app.py`.

### Notes:
 To bypass the Cloudflare protections that Kick uses to protect specific API endpoints, this bot relies on curl_cffi requests to impersonate Chrome browser.

 To login to Kick as the bot, it uses the mobile login endpoint using tokens provided by Kicks token provider endpoint.

 For receiving chat messages, the bot relies on the pysher library to listen to Kicks pusher server.