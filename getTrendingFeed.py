from TiktokApi import *

Api = Tiktok()


Api.openBrowser()

limit = 40
count = 0
first = True
flag = 0
while True:
    data = Api.getTrendingFeed(first=first)
    if first == True:
        for x in data['ItemModule']:
        
            video_id = data['ItemModule'][x]['id']
            caption = data['ItemModule'][x]['desc']
            print("Video <<%s>> <<%s>>" % (str(video_id), str(caption)))

            count += 1
            if count == limit:
                flag = 1
                break
    else:
        for x in data['itemList']:

            caption = str(x['desc'])
            video_id = str(x['id'])
            print("Video <<%s>> <<%s>>" % (str(video_id), str(caption)))

            count += 1
            if count == limit:
                flag = 1
                break
    if flag == 1:
        break
    first = False



Api.closeBrowser()

