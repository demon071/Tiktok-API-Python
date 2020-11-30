import requests
import json
import base64
import time
import re
import urllib.parse

class Tiktok:
	def __init__(self, cookie = None, verifyFp = None, region = "IN"):
		
		self.BASE_URL = 'https://www.tiktok.com/node/'
		self.ALTERNATIVE_BASE_URL = 'https://t.tiktok.com/api/'
		self.cookie = cookie
		self.verifyFp = verifyFp
		self.region = region
		self.headers = {
			'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.378',
			'cookie' : self.cookie
		}

	def getCookie(self, cookies):
		ck = ''
		if(cookies):
			for value in cookies:
				ck = ck + value + ':' + cookies[value]
				ck = ck + '; '
			return ck
		return None

	def getChallenge(self, challenge):
		if(challenge == ''):
			return False
		challenge = urllib.parse.quote(challenge)
		url = self.BASE_URL + 'share/tag/' + challenge
		data = requests.get(url, headers=self.headers)
		try:
			data = data.json()
			return data['challengeInfo']
		except:
			return False

	def getChallengeFeed(self, challenge, maxCursor = 0):
		if(challenge == ''):
			return False
		challenge = self.getChallenge(challenge)
		if(challenge):
			param = {
				"type"      : 3,
				"secUid"    : "",
				"id"        : challenge['challenge']['id'],
				"count"     : 30,
				"minCursor" : 0,
				"maxCursor" : maxCursor,
				"shareUid"  : "",
				"lang"      : "",
				"verifyFp"  : "",
				}
			url = self.BASE_URL + 'video/feed'
			data = requests.get(url, params=param, headers=self.headers)
			try:
				data = data.json()
				return data['body']
			except:
				return False
		return False

	def getMusic(self, musicId):
		if(musicId == ''):
			return False
		musicId = urllib.parse.quote(musicId)
		url = self.BASE_URL + 'share/music/original-sound-' + musicId
		data = requests.get(url, headers=self.headers)
		try:
			data = data.json()
			return data['musicInfo']
		except:
			return False

	def getMusicFeed(self, music, maxCursor = 0):
		if(music == ''):
			return False
		music = self.getMusic(music)
		if(music):
			param = {
				"type"      : 4,
				"secUid"    : "",
				"id"        : music['music']['id'],
				"count"     : 30,
				"minCursor" : 0,
				"maxCursor" : maxCursor,
				"shareUid"  : "",
				"lang"      : "",
				"verifyFp"  : "",
				}
			url = self.BASE_URL + 'video/feed'
			data = requests.get(url, params=param, headers=self.headers)
			try:
				data = data.json()
				return data['body']
			except:
				return False
		return False

	def getTrendingFeed(self, maxCursor = 0, region = None):
		
		param = {
			"type"      : 5,
			"secUid"    : "",
			"id"        : 1,
			"count"     : 30,
			"minCursor" : 0,
			"maxCursor" : maxCursor,
			"shareUid"  : "",
			"lang"      : "",
			"verifyFp"  : "",
			}
		if region == None:
			url = self.BASE_URL + 'video/feed'
			data = requests.get(url, params=param, headers=self.headers)
			try:
				data = data.json()
				return data['body']
			except:
				return False
		else:
			url = self.ALTERNATIVE_BASE_URL + 'item_list/'
			params['region'] = region
			data = requests.get(url, params=param, headers=self.headers)
			try:
				return json.loads(data.content)
			except:
				return False

	def getUser(self, username):
		if(username==''):
			return False
		username = urllib.parse.quote(username)
		url = self.BASE_URL + 'share/user/@' + username
		data = requests.get(url, headers=self.headers)
		try:
			data = data.json()
			return data['userInfo']
		except:
			return False

	def getUserFeed(self, username, maxCursor):
		if(username==''):
			return False
		user = self.getUser(username)
		if(user):
			param = {
				"type"      : 1,
				"secUid"    : "",
				"id"        : user['user']['id'],
				"count"     : 30,
				"minCursor" : 0,
				"maxCursor" : maxCursor,
				"shareUid"  : "",
				"lang"      : "",
				"verifyFp"  : "",
				}
			url = self.BASE_URL + 'video/feed'
			data = requests.get(url, params=param, headers=self.headers)
			try:
				data = data.json()
				return data['body']
			except:
				return False
		return False

	def getVideoById(self, vid):
		if(vid == ''):
			return False
		base_url = 'https://api.wppress.net/tiktok/nwm/{}'.format(vid)
		data = requests.get(base_url, headers=self.headers)
		try:
			data = data.json()
			return data
		except:
			return False

	def getVideoByUrl(self, video_url):
		if(video_url == ''):
			return False
		vid = re.findall(r'video\/([0-9]+)',video_url)[0]
		base_url = 'https://api.wppress.net/tiktok/nwm/{}'.format(vid)
		data = requests.get(base_url, headers=self.headers)
		try:
			data = data.json()
			return data
		except:
			return False

	def DownloadVideoByUrl(self, video_url):
		# download video no water mark 
		if(video_url == ''):
			return False
		video = self.getVideoByUrl(video_url)
		if(video):
			vid = video['id']
			res = requests.get(f'https://api-h2.tiktokv.com/aweme/v1/play/?video_id={vid}&vr_type=0&is_play_url=1&source=PackSourceEnum_FEED&media_type=4&ratio=default&improve_bitrate=1', headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.378', 'referer': 'https://www.tiktok.com/'})
			with open('{}.mp4'.format(video['id']), 'wb') as fb:
				fb.write(res.content)
			return True
		return False

	def DownloadVideoById(self, vid):
		# download video no water mark 
		if(vid == ''):
			return False
		video = self.getVideoById(vid)
		if(video):
			vid = video['id']
			res = requests.get(f'https://api-h2.tiktokv.com/aweme/v1/play/?video_id={vid}&vr_type=0&is_play_url=1&source=PackSourceEnum_FEED&media_type=4&ratio=default&improve_bitrate=1', headers = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.378', 'referer': 'https://www.tiktok.com/'})
			with open('{}.mp4'.format(video['id']), 'wb') as fb:
				fb.write(res.content)
			return True
		return False







				
