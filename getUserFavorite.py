from TiktokApi import *
import json, requests
Api = Tiktok()

username = 'playbabybabyy'
info = Api.getInfoUser(username=username, use_selenium=True)
print(info)
# sec_user_id = info['users'][username]['secUid']

# limit = 40
# count = 0
# setFlag = 0
# max_cursor = 0
# while True:
#     api_url = f'https://toolav.herokuapp.com/favorite/?sec_user_id={sec_user_id}&max_cursor={max_cursor}'
#     resp = requests.get(api_url, headers= {
#         "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36"
#     })
#     try:
#         dl = resp.json()
#         aweme_list = dl.get('aweme_list', None)
#         if aweme_list:
#             for item in aweme_list:
#                 print(item['share_url'])
#                 count += 1
#                 if count == limit:
#                     setFlag = 1
#                     break
#             if setFlag == 1:
#                 break
#             if dl['has_more'] != 1:
#                 break
#             max_cursor = dl['max_cursor']

#     except:
#         print('Can not get data')