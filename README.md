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
## getVideoById
```python
vid = Api.getVideoById('6897853325761350913')
print(vid)
```
## getVideoByUrl
```python
vid = Api.getVideoByUrl('https://www.tiktok.com/@tiktok/video/6801895105885195526')
print(vid)
```

## DownloadVideoByUrl
```python
Api.DownloadVideoByUrl('https://www.tiktok.com/@tiktok/video/6801895105885195526')
```

## DownloadVideoByUrl
```python
Api.DownloadVideoById('6897853325761350913')
```
