import mailbot
import time
import os

# Umgebungsvariablen laden
chatId     = os.getenv('TELEGRAM_CHAT_ID')
topicId    = int(os.getenv('TELEGRAM_TOPIC_ID'))
tgApiToken = os.getenv('TELEGRAM_API_TOKEN')
mailServer = os.getenv('MAIL_SERVER')
mailAddress = os.getenv('MAIL_ADDRESS')
mailPassword = os.getenv('MAIL_PASSWORD')
mailFolder  = os.getenv('MAIL_FOLDER', 'INBOX')  # Standardwert: INBOX
webmailLoginURL = os.getenv('WEBMAIL_LOGIN_URL')

mailbox = mailbot.Mailbox(mailServer, mailAddress, mailPassword, mailFolder)
sender  = mailbot.TgSender(tgApiToken, chatId, topicId, webmailLoginURL)

print('Start checking..')
while True:
    emails = mailbox.getUnseenMails(False)
    for email in emails:
        print(email)
        data = f"{email['sender']}\n{email['subject']}\n{email['body']}"
        data = data.replace('&', '&amp;').replace('<', '(').replace('>', ')').replace('"', '&quot;')
        print(data)
        sender.send(data)
    time.sleep(300)
