import requests
from bs4 import BeautifulSoup
import re
import sqlite3

conn = sqlite3.connect('nflPlayers.db')
c = conn.cursor()
divider = 24 
def create_qb_table():
    c.execute('CREATE TABLE IF NOT EXISTS QuarterBacks(name TEXT PRIMARY KEY, team TEXT, games TEXT, qbRating TEXT, completions TEXT, attempts TEXT, passingYards TEXT, passYdsPerAttempt TEXT, longestPass TEXT, interceptions TEXT, passTDS TEXT, rushes TEXT, rushYds TEXT, rushYdsPerAttempt TEXT, longestRush TEXT, rushTDs TEXT, sacks TEXT, ydsLost TEXT, fumbles TEXT, fumblesLost TEXT)')

def qb_in_table():
	qb = getQBRatings()
	for stats in qb:
		name = stats[0]
		team = stats[1]
		games = stats[2]
		qbRating = stats[3]
		passCompletions = stats[4]
		passAttempts =  stats[5]
		passingYards = stats[6]
		passingYdsPerAttempt = stats[7]
		passingLongestYds = stats[8]
		interceptions = stats[9]
		passingTDs = stats[10]
		rushAttempts = stats[12]
		rushingYds = stats[13]
		avgRush = stats[14]
		rushingLongestYds = stats[15]
		rushTDs = stats[16]
		sacks = stats[18]
		ydsLost = stats[19]
		fumbles = stats[21]
		fumblesLost = stats[22]

		c.execute("INSERT INTO QuarterBacks(name, team, games, qbRating, completions, attempts, passingYards, passYdsPerAttempt, longestPass, interceptions, passTDS, rushes, rushYds, rushYdsPerAttempt, longestRush, rushTDs, sacks, ydsLost, fumbles, fumblesLost) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
			(name, team, games, qbRating, passCompletions, passAttempts, passingYards, passingYdsPerAttempt, passingLongestYds, interceptions, passingTDs, rushAttempts, rushingYds, avgRush, rushingLongestYds, rushTDs, sacks, ydsLost, fumbles, fumblesLost))
		conn.commit()

def getQBRatings():
	r = requests.get("http://sports.yahoo.com/nfl/stats/byposition?pos=QB")
	soup = BeautifulSoup(r.content,"html.parser")
	
	#QB Ratings
	qbRatingsSearch = soup.find_all('td', {'class': re.compile(r'ysptblclbg6')})
	qbRatings = []
	for qb in qbRatingsSearch:
		rating = cleanUpQBRat(str(qb))
		qbRatings.append(rating)

	#Other Stats 
	statisticsSearch = soup.find_all('td', {'class':re.compile(r'yspscores')})
	numQBs = len(statisticsSearch)/divider
	old_count = 0
	new_count = divider
	qbNum = 0

	player = []
	while (old_count < len(statisticsSearch)):
		el_stats = []
		for i in range(old_count, new_count):
			if i < old_count+2:
				el_stats.append(cleanUpQBRat(str(statisticsSearch[i])))
			elif i == old_count + 3:
				el_stats.append(qbRatings[qbNum])
			else:
				el_stats.append((cleanUp2(cleanUp(str(statisticsSearch[i])))))
		old_count += divider
		new_count += divider
		qbNum += 1
		player.append(el_stats)
	return player

def cleanUp(stat):
	split1 = stat.split('>')
	split2 = split1[1].split('<')
	name = split2[0]
	return name

def cleanUpQBRat(stat):
	split1 = stat.split('<')
	split2 = split1[2].split('>')
	return split2[1]

def cleanUp2(stat):
	name = stat.replace(u'\xa0', '')
	return name

create_qb_table()
qb_in_table()


