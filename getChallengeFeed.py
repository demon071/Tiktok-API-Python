from TiktokApi import *

Api = Tiktok()

limit = 40 
count = 0
setFlag = 0
max_cursor = 0
while True:
    Feed, cookie = Api.getChallengeFeed(challenge='funny', max_cursor=max_cursor)
    dl = Download(cookie=cookie, path='video')
    for post in Feed['itemListData']:
        video_url = post['itemInfos']['video']['urls'][0]
        video_id = post['itemInfos']['id']
        print(video_id)
        # download video
        # dl.downloadVideo(url=video_url, file_name=video_id)
        # print('Download video {}.mp4'.format(video_id))
        count += 1
        if count == limit:
            setFlag = 1
            break
    max_cursor += 30 
    if setFlag == 1:
        break