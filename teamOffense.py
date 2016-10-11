import requests
from bs4 import BeautifulSoup
import re
import sqlite3

def getOffStats():
	# returns all stats except for points/game
	r = requests.get("https://sports.yahoo.com/nfl/stats/byteam?group=Offense&cat=Total&conference=NFL&year=season_2016&sort=530&old_category=Total&old_group=Offense")
	soup = BeautifulSoup(r.content,"html.parser")

	stats = soup.find_all('td', class_ = 'yspscores')
	teams = []
	for team in range(0,32):
		row = []
		for stat in range (0,27):
			row.append(stats[team * 27 + stat])
		teams.append(row)
	
	cleanTeams = []
	for t in teams:
		del t[1]
		del t[2]
		del t[2]
		del t[3]
		del t[4]
		del t[5]
		del t[6]
		del t[7]
		del t[8]
		del t[9]
		del t[10]
		del t[11]
		del t[12]
		del t[13]
		row = []
		name = t[0]
		row.append(cleanName(name))
		for stat in range(1,len(t)):
			s = cleanStat(t[stat])
			row.append(s)
		cleanTeams.append(row)

	return cleanTeams
	

def cleanName(name):
	name = str(name)
	splitOne = name.split('<')
	res = splitOne[2]
	splitTwo = res.split('>')
	return splitTwo[1]

def cleanStat(stat):
	stat = str(stat)
	splitOne = stat.split('<')
	res = splitOne[1]
	splitTwo = res.split('>')
	res = splitTwo[1]
	return cleanUp2(res)

def cleanUp2(stat):
	name = stat.replace(u'\xa0', '')
	return name

print(getOffStats())