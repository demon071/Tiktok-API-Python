# Tiktok API 
API Tiktok use Python

# Install
pip install requests

# get user info
uid = Api.getUserId('vtkh2004')\n
print(uid)

# get user post
feed  = Api.getUserFeed(uid, '0')\n
print(feed)

# get video trending
trending = Api.getTrendingFeed()\n
print(trending)

# get video id 
vid = Api.getVideoById('6897853325761350913')\n
print(vid)
