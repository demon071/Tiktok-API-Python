# API TIKTOK in Python

This is the unofficial TIKTOK API in Python. With this API you can get data of Treingding, User Post, Hashtag Post, Music Post.

## Install
```
git clone https://github.com/demon071/Tiktok-API-Python.git
cd Tiktok-API-Python
pip install -r requirements.txt
```

## Quick Start

```python
from TiktokApi import *

Api = Tiktok()
trending, _ = Api.getTrendingFeed(max_cursor= '0')
for trend in trending['itemListData']:
    print(trend['itemInfos']['text'])

# print caption video
```

## Download Video Trending Nowatermark
```python
from TiktokApi import *

Api = Tiktok()
trending, _ = Api.getTrendingFeed(max_cursor= '0')
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36",

    # Your device ID
    "iid": "",
    "openudid": "", 
    "device-id": "",

    # Your proxy
    "proxy-host": "",
    "proxy-port": "",
    "proxy-user": "",
    "proxy-pass": "",
       
 }
download = Download(path='trendingVideo')
items = []
for trend in trending['itemListData']:
    items.append(trend['itemInfos']['id'])

for item in items:
    result = download.downloadVideoNoWatermarkByID(id=item, file_name=item, headers=headers)
    if result:
        print("Download Video {}.mp4".format(item))
    else:
        print("ERROR")
```


### Buy me a Coffee

[Buy me a Coffee](https://www.buymeacoffee.com/demon071)

[Paypal](https://paypal.me/demon071)


### Contact 
[Telegram](https://t.me/demon071)
