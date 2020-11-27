import TiktokApi

Api = TiktokApi.Tiktok()

# get user info
uid = Api.getUserId('vtkh2004')
# print(uid)

#get user post
feed  = Api.getUserFeed(uid, '0')
# print(feed)

#get video trending
trending = Api.getTrendingFeed()
# print(trending)

#get video id 
vid = Api.getVideoById('6897853325761350913')
# print(vid)
