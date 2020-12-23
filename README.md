# Tiktok API 
API Tiktok use Python
## Get video no watermark from URL
```python
import requests

url = "https://tiktok-video-no-watermark1.p.rapidapi.com/"

querystring = {"type":"urlPro","search":"https://www.tiktok.com/@tiktok/video/6801895105885195526"}

headers = {
    'x-rapidapi-key': [YOUR-API-KEY],
    'x-rapidapi-host': "tiktok-video-no-watermark1.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
```
https://rapidapi.com/AdKT36/api/tiktok-video-no-watermark1

###Result:
```python
    {
   "statusCode":0,
   "info":{
      "type":"video",
      "detail":"https:\/\/www.tiktok.com\/@tiktok\/video\/6801895105885195526"
   },
   "items":[
      {
         "id":"6801895105885195526",
         "desc":"Happy International Women\u2019s Day! #shecandoit",
         "createTime":1583689617,
         "video":{
            "height":1280,
            "width":720,
            "duration":48667,
            "ratio":1280,
            "cover":"https:\/\/www.tiktok.com\/api\/img\/?itemId=6801895105885195526&location=0",
            "originCover":"https:\/\/p16-sign-sg.tiktokcdn.com\/tos-maliva-p-0068\/2a91b69551974041bde1771ee7e2dbbb_1583689623~tplv-tiktokx-360p.webp?x-expires=1608706800&x-signature=LAazMZxJ70nAV22oXi5zxJXc%2FGo%3D",
            "dynamicCover":"https:\/\/p16-sign-sg.tiktokcdn.com\/obj\/tos-maliva-p-0068\/9b6fdeff54e64f399fe7c228723684fd_1583689624?x-expires=1608706800&x-signature=pquQZaX4jkBUdhuxqD2vLka4ULA%3D",
            "playAddr":"https:\/\/v16.tiktokcdn.com\/53f8b27a63eeb319721b5e105ff5720b\/5fe2f69a\/video\/tos\/useast2a\/tos-useast2a-ve-0068c001\/b9734df5bcfb47f498b53918bc80be71\/?a=1180&br=2908&bt=1454&cd=0%7C0%7C0&cr=0&cs=0&cv=1&dr=0&ds=6&er=&l=202012230148580102341090805F46E183&lr=all&mime_type=video_mp4&qs=0&rc=ams6NHZoaHdsczMzZzczM0ApZDRoZjtkZjs1NzVoPGg1Omc1NnFeZzBlcmZfLS0uMTZzczJeYDM0L2BfYGM0Yl9fYi86Yw%3D%3D&vl=&vr=",
            "downloadAddr":"https:\/\/v16.tiktokcdn.com\/e35c1d32987cbda8ffab50754410769e\/5fe2f69a\/video\/tos\/useast2a\/tos-useast2a-pve-0068\/b4a119d13da14038be98757346eb30f5\/?a=1180&br=3248&bt=1624&cd=0%7C0%7C0&cr=0&cs=0&cv=1&dr=0&ds=3&er=&l=202012230148580102341090805F46E183&lr=all&mime_type=video_mp4&qs=0&rc=ams6NHZoaHdsczMzZzczM0ApOTU2OWU3O2U6Nzk8ZTNpN2c1NnFeZzBlcmZfLS0uMTZzc2FhLmM0Xi02MC8vMzQuMjI6Yw%3D%3D&vl=&vr="
         },
         "author":{
            "id":"107955",
            "uniqueId":"tiktok",
            "nickname":"TikTok",
            "avatarThumb":"https:\/\/p16-sign-sg.tiktokcdn.com\/musically-maliva-obj\/1645136815763462~c5_100x100.webp?x-expires=1608771600&x-signature=JS3XfDMOucOvrYhvW7Z2bLwPLfQ%3D",
            "avatarMedium":"https:\/\/p16-sign-sg.tiktokcdn.com\/musically-maliva-obj\/1645136815763462~c5_720x720.webp?x-expires=1608771600&x-signature=641jFbzKyV2DDprsVm%2FZtH%2BPj2E%3D",
            "avatarLarger":"https:\/\/p16-sign-sg.tiktokcdn.com\/musically-maliva-obj\/1645136815763462~c5_1080x1080.webp?x-expires=1608771600&x-signature=9JWzMVwixKgMrd8R9fU%2B5Tt%2BZAY%3D",
            "signature":"It Starts On TikTok",
            "verified":"",
            "secUid":"MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM"
         },
         "music":{
            "id":6801885499343571718,
            "title":"nh\u1ea1c n\u1ec1n - TikTok",
            "playUrl":null,
            "coverThumb":"https:\/\/p16-sign-sg.tiktokcdn.com\/musically-maliva-obj\/1645136815763462~c5_100x100.webp?x-expires=1608771600&x-signature=JS3XfDMOucOvrYhvW7Z2bLwPLfQ%3D",
            "coverMedium":"https:\/\/p16-sign-sg.tiktokcdn.com\/musically-maliva-obj\/1645136815763462~c5_720x720.webp?x-expires=1608771600&x-signature=641jFbzKyV2DDprsVm%2FZtH%2BPj2E%3D",
            "coverLarge":"https:\/\/p16-sign-sg.tiktokcdn.com\/musically-maliva-obj\/1645136815763462~c5_1080x1080.webp?x-expires=1608771600&x-signature=9JWzMVwixKgMrd8R9fU%2B5Tt%2BZAY%3D",
            "authorName":"TikTok",
            "original":null
         },
         "stats":{
            "diggCount":956589,
            "shareCount":5558,
            "commentCount":18864,
            "playCount":10632268
         }
      }
   ],
   "hasMore":false,
   "minCursor":"0",
   "maxCursor":" 0"
}
```

## Tool download All video
- Support downloading all video users on 4 platforms: TikTok, TikTok China (Douyin), Kwai, Kwai China (Kuaishou)
- Video quality full HD
- Download multiple channels at the same time
- Automatically create cross-platform folders and download IDs
=>  https://youtu.be/btpZPN7kFOU
=>  anhk1996@gmail.com
# Install
pip install requests

# How to use
```python
import TiktokApi
Api = TiktokApi.Tiktok()
```
## getUser
```python
user = Api.getUser('vtkh2004')
print(user)
```
## getUserFeed
```python
userfeed  = Api.getUserFeed('vtkh2004', '0')
print(userfeed)
```
## getMusic
```python
music = Api.getMusic('6896022404674800386')
print(music)
```
## getMusicFeed
```python
musicfeed  = Api.getMusicFeed('6896022404674800386', '0')
print(musicfeed)
```
## getChallenge
```python
challenge = Api.getChallenge('foryou')
print(challenge)
```
## getChallengeFeed
```python
challengefeed  = Api.getChallengeFeed('foryou', '0')
print(challengefeed)
```
## getTredingFeed
```python
trending = Api.getTrendingFeed('0')
print(trending)
```

## getInfoVideo
```python
vid = Api.getInfoVideo('https://www.tiktok.com/@tiktok/video/6801895105885195526')
print(vid)
```

## DownloadVideoNoWatermark
Download video no watermark by id, select folder save: video
```python
Api.DownloadVideoNoWatermark('6897853325761350913', 'video')
```
