import requests
import json
import base64
import time
import re
import urllib.parse

class Tiktok:
	def __init__(self):
		pass


	def getUserId(self, username):
		if(username==''):
			return False
		headers = {
			'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.378',
			}
		url = 'https://t.tiktok.com/node/share/user/@{}'.format(username)
		result = requests.get(url, headers=headers)
		dl = result.json()
		try:
			return dl['userInfo']['user']['id']
		except:
			return None

	def getUserFeed(self, userId, maxCursor):
		if(userId==''):
			return False
		headers = {
			'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.378',
			}
		url = 'https://www.tiktok.com/node/video/feed?id={}&minCursor=0&maxCursor={}&count=100&type=1'.format(userId, maxCursor)
		result = requests.get(url, headers=headers)
		dl = result.json()
		try:
			return dl['body']
		except:
			return None

	def getTrendingFeed(self):
		headers = {
			'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.378',
			}
		url = 'https://www.tiktok.com/node/video/feed?id=1&minCursor=0&maxCursor=0&count=100&type=5'
		result = requests.get(url, headers=headers)
		dl = result.json()
		try:
			return dl['body']
		except:
			return None

	def getVideoById(self, vid):
		if(vid == ''):
			return False
		headers = {
			'user-agent' : 'Googlebot',
			}
		url = 'https://m.tiktok.com/v/{}.html'.format(vid)
		while True:
			result = requests.get(url, headers=headers)
			try:
				pattern = re.compile('type="application/json">(.*?)\\</script>')
				match = re.search(pattern, result.text)
				match1 = match.group().replace('type=\"application/json\">', "").replace('</script>', "")
				dl1 = urllib.parse.unquote_plus(match1)
				dl = json.loads(dl1)
				return dl['response']['videoData']['videoId']
				break
			except:
				pass
			
