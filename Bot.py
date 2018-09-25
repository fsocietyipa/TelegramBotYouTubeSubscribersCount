import requests
import time
import telepot
from telepot.loop import MessageLoop

def getSubscribersCount(name):
    key = "GOOGLEAPI_KEY"
    r = requests.get("https://www.googleapis.com/youtube/v3/channels?part=statistics&forUsername="+name+"&key="+key)

    if not r.json()["items"]:
        return "Null"
    else:
        subs = r.json()["items"][0]["statistics"]["subscriberCount"]
        return name + " has " + "{:,d}".format(int(subs)) + " subscribers!🎉"



def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    print('Got command: %s' % command)


    if command:
        if getSubscribersCount(command) == "Null":
            bot.sendMessage(chat_id, "Cannot find that user")
        else:
            bot.sendMessage(chat_id, getSubscribersCount(command))


bot = telepot.Bot('TELEGRAM_BOT_TOKEN')

MessageLoop(bot, handle).run_as_thread()
print('I am listening ...')

while 1:
    time.sleep(10)