import requests
from bs4 import BeautifulSoup
import re
import sqlite3

conn = sqlite3.connect('nflPlayers.db')
c = conn.cursor()

def create_qb_table():
    c.execute('CREATE TABLE IF NOT EXISTS QuarterBacksWeek2(name TEXT PRIMARY KEY, team TEXT, games TEXT, qbRating TEXT, completions TEXT, attempts TEXT, passingPercentage TEXT, passingYards TEXT, passYdsPerGame TEXT, passYdsPerAttempt TEXT, passTDs TEXT, interceptions TEXT, rushes TEXT, rushYds TEXT, rushYdsPerGame TEXT, rushYdsPerAttempt TEXT, rushTDs TEXT, sacks TEXT, ydsLost TEXT, fumbles TEXT, fumblesLost TEXT)')

def qb_in_table():
	qb = getQBRatings()
	for stats in qb:
		name = stats[0]
		team = stats[1]
		games = stats[2]
		qbRating = stats[3]
		passCompletions = stats[4]
		passAttempts =  stats[5]
		passingPercentage = stats[6]
		passingYards = stats[7]
		passYdsPerGame = stats[8]
		passingYdsPerAttempt = stats[9]
		passingTDs = stats[10]
		interceptions = stats[11]
		rushAttempts = stats[13]
		rushingYds = stats[14]
		rushYdsPerGame = stats[15]
		avgRush = stats[16]
		rushTDs = stats[17]
		sacks = stats[19]
		ydsLost = stats[20]
		fumbles = stats[22]
		fumblesLost = stats[23]

		c.execute("INSERT INTO QuarterBacksWeek2(name,team,games,qbRating,completions,attempts,passingPercentage,passingYards,passYdsPerGame,passYdsPerAttempt,passTDs,interceptions,rushes,rushYds,rushYdsPerGame,rushYdsPerAttempt,rushTDs,sacks,ydsLost,fumbles,fumblesLost) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
			(name,team,games,qbRating, passCompletions, passAttempts, passingPercentage, passingYards, passYdsPerGame, passingYdsPerAttempt, passingTDs, interceptions, rushAttempts, rushingYds, rushYdsPerGame, avgRush, rushTDs, sacks, ydsLost, fumbles, fumblesLost))
		conn.commit()

def getQBRatings():
	r = requests.get("https://sports.yahoo.com/nfl/stats/byposition?pos=QB&conference=NFL&year=season_2016&timeframe=ToDate&qualified=1&sort=49&old_category=QB")
	#https://sports.yahoo.com/nfl/stats/byposition?pos=QB&conference=NFL&year=season_2016&timeframe=Week1&sort=626&old_category=QB
	soup = BeautifulSoup(r.content,"html.parser")
	
	#QB Ratings
	qbRatingsSearch = soup.find_all('td', {'class': re.compile(r'ysptblclbg6')})
	qbRatings = []
	for qb in qbRatingsSearch:
		rating = cleanUpQBRat(str(qb))
		qbRatings.append(rating)

	#Other Stats 
	statisticsSearch = soup.find_all('td', {'class':re.compile(r'yspscores')})

	numQBs = len(statisticsSearch)/25
	print(numQBs)
	old_count = 0
	new_count = 25
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
		old_count += 25
		new_count += 25
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


