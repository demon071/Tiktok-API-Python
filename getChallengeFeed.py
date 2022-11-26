from TiktokApi import *
import time
Api = Tiktok()

# hashtag's name
challengename = 'funny'

url = 'https://tiktok.com/tag/%s' % challengename


Api.openBrowser(url, show_br=True)
input('Skip the captcha, press Enter to continue ')
limit = 40
count = 0
first = True
flag = 0
cursor = 0
secUid = ''
while True:
    if first == True:
        data = Api.getChallengeFeed(first=first)
        for x in data['ItemModule']:
            video_id = data['ItemModule'][x]['id']
            caption = data['ItemModule'][x]['desc']
            print("Video <<%s>> <<%s>>" % (str(video_id), str(caption)))
            count += 1
            if count == limit:
                flag = 1
                break
        if not data['ItemList']['challenge']['hasMore']:
            break
        cursor = data['ItemList']['challenge']['cursor']
        ch_id = data['ChallengePage']['challengeInfo']['challenge']['id']

    else:
        data = Api.getChallengeFeed(ch_id=ch_id, cursor=str(cursor), first=first)
        for x in data['itemList']:
            
            video_id = x['id']
            caption = x['desc']
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