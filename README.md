Hiện mình có cung cấp công cụ tải video tiktok, douyin, kuaishou.
Liên hệ Fb để biết thêm thông tin: www.facebook.com/AdK.T36
# Tiktok API 
API Tiktok use Python

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

