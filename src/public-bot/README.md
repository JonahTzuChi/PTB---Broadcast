# public-bot
User interact with this bot, which include subscribe and receive broadcast.

# Inside This Folder
* 📁 config - container specific parameters are stored here
* 📁 src    - source code are stored here
* 📄 Dockerfile - This file define the steps needed to build up the container
* 📄 requirements.txt - This file list down the python packages needed
* 📄 README.md - You are here :smile:

# Do These
*  Inside the config directory, rename these files
    * example.config.env -> config.env
    * example.config.yml -> config.yml
*  Add Telegram Bot API token to __config.env__. You may get it from __@BotFather__, refer to __/docs/setup/get_telegram_bot_token.md__
*  Add your own __Telegram ID__ to __config.yml__ like below (optional)
    ```
    # inside config.yml
    SYSTEM_ADMINS: [<Telegram ID>] # List of telegram_id that has full access to the bot
    ```