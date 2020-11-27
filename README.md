# Tiktok API 
API Tiktok use Python

# Install
pip install requests

# get user info
```python
uid = Api.getUserId('vtkh2004')
print(uid)
```

# get user post
```python
feed  = Api.getUserFeed(uid, '0')
print(feed)
```

# get video trending
```python
trending = Api.getTrendingFeed()
print(trending)
```

# get video id 
```python
vid = Api.getVideoById('6897853325761350913')
print(vid)
```
