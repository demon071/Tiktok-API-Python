import requests
import json
import base64
import time
import re
import urllib.parse
import pickle

class Tiktok:
	def __init__(self):
		
		self.BASE_URL = 'https://www.tiktok.com/node/'
		self.headers = {
			'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.66 Safari/537.36 OPR/72.0.3815.378',
			}

	def getChallenge(self, challenge):
		if(challenge == ''):
			return False
		challenge = urllib.parse.quote(challenge)
		url = self.BASE_URL + 'share/tag/' + challenge
		data = requests.get(url, headers=self.headers)
		self.save_cookies(data.cookies, 'cookie.txt')
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
			self.save_cookies(data.cookies, 'cookie.txt')
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
		self.save_cookies(data.cookies, 'cookie.txt')
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
			self.save_cookies(data.cookies, 'cookie.txt')
			try:
				data = data.json()
				return data['body']
			except:
				return False
		return False

	def getTrendingFeed(self, maxCursor = 0):
		
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
		url = self.BASE_URL + 'video/feed'
		data = requests.get(url, params=param, headers=self.headers)
		print(data.request.url)
		self.save_cookies(data.cookies, 'cookie.txt')
		try:
			data = data.json()
			return data['body']
		except:
			return False

	def getUser(self, username):
		if(username==''):
			return False
		username = urllib.parse.quote(username)
		url = self.BASE_URL + 'share/user/@' + username
		data = requests.get(url, headers=self.headers)
		self.save_cookies(data.cookies, 'cookie.txt')
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
			self.save_cookies(data.cookies, 'cookie.txt')
			try:
				data = data.json()
				return data['body']
			except:
				return False
		return False

	def getInfoVideo(self, url):
		s = requests.Session()
		if(url == ''): return False
		match = re.findall(r'https://www\.tiktok\.com/@(.*?)/video/([0-9]+)', url)
		if(match):
			username = match[0][0]
			video_id = match[0][1]
			api_url = 'https://www.tiktok.com/node/share/video/@' + username + '/' + video_id
			data = s.get(api_url, headers=self.headers)
			self.save_cookies(data.cookies, 'cookie.txt')
			try:
				data = data.json()
				return data['itemInfo']['itemStruct']
			except:
				return False
		return False

	def save_cookies(self, requests_cookiejar, filename):
		with open(filename, 'wb') as f:
			pickle.dump(requests_cookiejar, f)

	def load_cookies(self, filename):
		with open(filename, 'rb') as f:
			return pickle.load(f)
