import sys
from telethon import TelegramClient
import time
import datetime
starttime = time.time()

# For API from my.telegram.org
api_id = 14438048
api_hash = 'b8fa33d70d474ee47fe268a90bf9c119'

groups = ['bdtest02','bdtest01']

messages = input('Type the text you want to show: ')

failcount = 0

while True:
    with TelegramClient('info', api_id, api_hash) as client:
        for x in groups:
            try:
                client.loop.run_until_complete(client.send_message(x, messages))
            except:
                print(x, sys.exc_info()[0])
                failcount += 1
    print(datetime.datetime.now(), str(failcount/len(groups) * 100) + '%')
    time.sleep(10800 - ((time.time() - starttime) % 10800))