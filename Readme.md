# Python based Telegram bot / eMail bridge

this bot checks every 300 seconds, if an email was received and if so, sends it into a group-topic.
### important
this script was especially designed, so the bot sends only into a specific topic (for example "Communications"), meaning, your group needs to be one with topics!


Create a ```.env``` file containing:

```
#telegram config
TELEGRAM_CHAT_ID=-1234
TELEGRAM_TOPIC_ID=15
TELEGRAM_API_TOKEN=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

#mail config
MAIL_SERVER=web.de
MAIL_ADDRESS=contact@web.de
MAIL_PASSWORD=yoursecureandlongpassword
MAIL_FOLDER=INBOX
WEBMAIL_LOGIN_URL=https://mail.google.com/

```

### get a bot
text @Botfather in telegram:
```
/newbot
```
store the received token in ```.env``` file


### add bot to your desired group and send any message in a specific topic of the group
at the following link:
```
https://api.telegram.org/{INSERT_YOUR_TOKEN_HERE}/getUpdates
```
you will get:
- the chat_ID of your group
- the response id of your topic
add these along with your email credentials and server into the ```.env``` file and simply ```docker compose up -d```

# this is based on work of https://github.com/c4k3man