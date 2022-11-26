import sys
sys.stdin.reconfigure(encoding='utf-8')
sys.stdout.reconfigure(encoding='utf-8')
from TiktokApi import *

Api = Tiktok()

# edit username  here
username = 'tiktok'

url = 'https://tiktok.com/@%s' % username

Api.openBrowser(url, True)
input('Skip the captcha, press Enter to continue ')
limit = 40
count = 0
first = True
flag = 0
cursor = 0
secUid = ''
while True:
    if first == True:
        data = Api.getUserFeed(first=first)
        for x in data['ItemModule']:

            video_id = data['ItemModule'][x]['id']
            caption = data['ItemModule'][x]['desc']
            print("Video <<%s>> <<%s>>" % (str(video_id), str(caption)))

            count += 1
            if count == limit:
                flag = 1
                break
        if not data['ItemList']['user-post']['hasMore']:
            break
        cursor = data['ItemList']['user-post']['cursor']
        secUid = data['UserPage']['secUid']
    else:
        data = Api.getUserFeed(secUid=secUid, cursor=cursor, first=first)
        for x in data['itemList']:
           
            caption = str(x['desc'])
            video_id = str(x['id'])
            print("Video <<%s>> <<%s>>" % (str(video_id), str(caption)))

            count += 1
            if count == limit:
                flag = 1
                break
        if not data['hasMore']:
            break
        cursor = data['cursor']
    if flag == 1:
        break
    first = False
    # break



Api.closeBrowser()