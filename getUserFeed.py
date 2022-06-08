from TiktokApi import *

Api = Tiktok()

# nhập tên người dùng
username = 'tiktok'

url = 'https://tiktok.com/@%s' % username

# Khởi động tình duyệt trước khi lấy dữ liệu
Api.openBrowser(url)

limit = 40
count = 0
first = True
flag = 0
cursor = 0
secUid = ''
while True:
    if first == True:
        data = Api.getUserFeed(first=first)
        for x in data['ItemModule']:
            print(data['ItemModule'][x]['id'])
            # print(data['ItemModule'][x]['desc'])
            count += 1
            if count == limit:
                flag = 1
                break
        if not data['ItemList']['user-post']['hasMore']:
            break
        cursor = data['ItemList']['user-post']['cursor']
        secUid = data['UserPage']['secUid']
    else:
        data = Api.getUserFeed(secUid=secUid, cursor=cursor, first=first)
        for x in data['itemList']:
            # print(str(x['desc']))
            print(str(x['id']))
            count += 1
            if count == limit:
                flag = 1
                break
        if not data['hasMore']:
            break
        cursor = data['cursor']
    if flag == 1:
        break
    first = False
    # break


# Đóng tình duyệt sau khi đã chạy xong
Api.closeBrowser()