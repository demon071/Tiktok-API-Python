import requests, os
from pathlib import Path

class Download:
    def __init__(self, cookie = {}, path = ''):
        self.cookie = cookie
        self.path = path
        try:
            path = str(Path().absolute())
            if not os.path.exists(self.path):
                os.makedirs(self.path)
        except:
            pass

    def downloadVideo(self, url, file_name = 'video'):
        res = requests.get(
            url,
            headers={
                    "Referer": "https://www.tiktok.com/",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                },
            cookies=self.cookie
        )
        with open(self.path+"/{}.mp4".format(file_name), 'wb') as out:
            out.write(res.content)


    def downloadVideoNoWatermarkByID(self, id, file_name = 'video', headers = {'user-agent': 'okhttp'}):
        api = 'https://toolav.herokuapp.com/id/?video_id='+id
        r = requests.get(
            api, 
            headers = headers
        )

        response = r.json()
        
        aweme_id = response.get('item', '').get('aweme_id', '')
        
        if aweme_id != '':
            url = 'https://api-h2.tiktokv.com/aweme/v1/play/?video_id='+aweme_id+'&vr_type=0&is_play_url=1&source=PackSourceEnum_FEED&media_type=4&ratio=default&improve_bitrate=1'
            res = requests.get(
                url,
                headers = {
                    'User-Agent' : 'okhttp',
                }
            )
            with open(self.path+"/{}.mp4".format(file_name), 'wb') as out:
                out.write(res.content)
            return True
        else:
            return False
