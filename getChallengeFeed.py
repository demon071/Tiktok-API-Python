from TiktokApi import *

Api = Tiktok()

# hashtag's name
challengename = 'funny'

url = 'https://tiktok.com/tag/%s' % challengename


Api.openBrowser(url)

limit = 40
count = 0
first = True
flag = 0
cursor = 0
secUid = ''
dl = Download()
while True:
    if first == True:
        data = Api.getChallengeFeed(first=first)
        for x in data['ItemModule']:
            # show video ID
            print(data['ItemModule'][x]['id'])
            # show video caption

            # print(data['ItemModule'][x]['desc'])
            count += 1
            if count == limit:
                flag = 1
                break
        if not data['ItemList']['challenge']['hasMore']:
            break
        cursor = data['ItemList']['challenge']['cursor']
        ch_id = data['ChallengePage']['challengeInfo']['challenge']['id']

        
    else:
        data = Api.getChallengeFeed(ch_id=ch_id, cursor=cursor, first=first)
        for x in data['itemList']:
            
            # print(str(x['desc']))

            print(str(x['id']))
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