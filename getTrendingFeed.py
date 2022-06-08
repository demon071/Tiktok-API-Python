from TiktokApi import *

Api = Tiktok()

# Khởi động tình duyệt trước khi lấy dữ liệu
Api.openBrowser()

limit = 40
count = 0
first = True
flag = 0
while True:
    data = Api.getTrendingFeed(first=first)
    if first == True:
        for x in data['ItemModule']:
            print(data['ItemModule'][x]['id'])
            # print(data['ItemModule'][x]['desc'])
            count += 1
            if count == limit:
                flag = 1
                break
    else:
        for x in data['itemList']:
            # print(str(x['desc']))
            print(str(x['id']))
            count += 1
            if count == limit:
                flag = 1
                break
    if flag == 1:
        break
    first = False


# Đóng tình duyệt sau khi đã chạy xong
Api.closeBrowser()

