from turtle import Turtle
import requests
import json
import base64
import time
import re, traceback
import urllib.parse
import pickle
from urllib.parse import urlencode, quote
from .browser import Browser
from .ultis import set_url, get_param_url
from .encryption import get_tt_param

class Tiktok:
    def __init__(self):
        self.BASE_URL = 'https://www.tiktok.com/node/'
        
    def openBrowser(self, url = 'https://tiktok.com/', show_br = False):
        self.browser = Browser(url, show_br)
        self.browser.launch_borwser()
        self.default_params = self.browser.get_defaut_params()

    def closeBrowser(self):
        self.browser.close_browser()

    def getTrendingFeed(self, cookies = {}, limit = 40, first = True):
        if first == True:
            return self.browser.first_data()
        try:
            params = {
                'count': "30"
            }
            params.update(self.default_params)
            params = dict(sorted(params.items(), key=lambda item: item[1]))
            api_url = set_url('/api/recommend/item_list/', params)
            data = self.browser.fetch_browser(api_url)
            return data
        except Exception:
            import traceback 
            print(traceback.format_exc())
            return False

    def getUserFeed(self, secUid = '', cursor = 0, first = True):
        if first == True:
            return self.browser.first_data()
        try:
            params = {
                'secUid': secUid,
                'count': '30',
                'cursor': cursor,
                'userId': 'undefined',
            }
            params.update(self.default_params)
            params = dict(sorted(params.items(), key=lambda item: item[1]))
            api_url = set_url('/api/post/item_list/', params)
            tt_params = get_tt_param(get_param_url(params))
            data = self.browser.fetch_browser(api_url, tt_params)
            return data
        except Exception:
            import traceback 
            print(traceback.format_exc())
            return False
        


    def getChallengeFeed(self, challenge = '', max_cursor = 0, ch_id = '0'):
        if challenge == '' and ch_id == '0':
            return 'Challenge or Ch_id is required'
        param = {
            "type": 3,
            "secUid": "",
            "id": '',
            "count": 30,
            "minCursor": 0,
            "maxCursor": max_cursor,
            "shareUid": "",
            "lang": "",
            "verifyFp": "",
        }
        if ch_id != '0':
            param['id'] = ch_id
        else:
            ch = self.getInfoChallenge(challenge)
            if ch:
                param['id'] = ch['challengeInfo']['challenge']['id']
            else:
                return False
        try:
            url = self.BASE_URL + 'video/feed'
            res = requests.get(
                url, 
                params=param,
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "authority": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Host": "www.tiktok.com",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                }
            )
            resp = res.json()
            return resp['body'], res.cookies.get_dict()
        except Exception:
            print(traceback.format_exc())
            return False

    def getMusicFeed(self, music = '', max_cursor = 0):
        if music == '':
            return 'Challenge or Ch_id is required'
        param = {
            "type": 4,
            "secUid": "",
            "id": '',
            "count": 30,
            "minCursor": 0,
            "maxCursor": max_cursor,
            "shareUid": "",
            "lang": "",
            "verifyFp": "",
        }
        
        # ch = self.getInfoMusic(music)
        if music:
            param['id'] = music
        else:
            return False
        try:
            url = self.BASE_URL + 'video/feed'
            res = requests.get(
                url, 
                params=param,
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "authority": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Host": "www.tiktok.com",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                }
            )
            resp = res.json()
            return resp['body'], res.cookies.get_dict()
        except Exception:
            print(traceback.format_exc())
            return False


    def getInfoUser(self, username = '', user_url = '', use_selenium = False):
        if username != '':
            url = 'http://www.tiktok.com/@{}?lang=en'.format(quote(username))
        if user_url != '':
            url = user_url
        try:
            if use_selenium == True:
                from selenium import webdriver
                from webdriver_manager.chrome import ChromeDriverManager
                options = webdriver.ChromeOptions()
                options.add_argument('--disable-gpu')
                # options.add_argument('--headless')
                driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
                driver.get(url)
                html = driver.page_source
                if 'tiktok-verify-page' in html:
                    input('Please bypass captcha and enter any character to continue:')
                html = driver.page_source
                driver.close()
                driver.quit()
            else:
                res = requests.get(
                    url,
                    headers={
                        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                        "authority": "www.tiktok.com",
                        # "path": "/@{}".format(quote(username)),
                        "Accept-Encoding": "gzip, deflate",
                        "Connection": "keep-alive",
                        "Host": "www.tiktok.com",
                        "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                    }
                )
                html = res.text
                # print(html)


            resp = self.__extra_next_data__(html)

            return json.loads(resp)['UserModule']
        except Exception:
            print(traceback.format_exc())
            return False

    def getInfoChallenge(self, challenge):
        if challenge == '':
            return 'Challenge is required'
        try:
            res = requests.get(
                'https://www.tiktok.com/tag/{}'.format(quote(challenge)),
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "authority": "www.tiktok.com",
                    "path": "/tag/{}".format(quote(challenge)),
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Host": "www.tiktok.com",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                }
            )
            resp = self.__extra_next_data__(res.text)
            return json.loads(resp)['ChallengePage']
        except Exception:
            print(traceback.format_exc())
            return False

    def getInfoMusic(self, music_url):
        if music_url == '':
            return 'Challenge is required'
        try:
            res = requests.get(
                music_url,
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "authority": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Host": "www.tiktok.com",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                }
            )
            resp = self.__extra_next_data__(res.text)
            return json.loads(resp)['props']['pageProps']
        except Exception:
            print(traceback.format_exc())
            return False

    def getInfoVideo(self, url):
        if url == '':
            return 'URL is required'
        try:
            res = requests.get(
                url,
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "authority": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Host": "www.tiktok.com",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                }
            )
            resp = self.__extra_next_data__(res.text)
            video_info = json.loads(resp)['ItemModule']
            vid = list(video_info.keys())[0]
            return video_info[vid], res.cookies.get_dict()
        except Exception:
            print(traceback.format_exc())
            return False


    def __extra_next_data__(self, html):
        resp = self.r1(r'window\[\'SIGI_STATE\'\]=(.*?);window\[\'SIGI_RETRY\'\]', html) or \
        self.r1(r'<script id="SIGI_STATE" type="application/json">(.*?)</script>', html)
        return resp

    def r1(self, pattern, text):
        m = re.search(pattern, text)
        if m:
            return m.group(1)

    

    
