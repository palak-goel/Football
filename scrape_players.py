from bs4 import BeautifulSoup
import urllib.request as ur
import sqlite3, re, requests

def get_stats(pos, week):
    r = ur.urlopen('http://sports.yahoo.com/nfl/stats/byposition?pos=' + str(pos) + '&conference=NFL&year=season_2016&timeframe=Week' + str(week) + '&sort=626&old_category=' + str(pos)).read()
    soup = BeautifulSoup(r, "html.parser")
    soup.get_text()
    players = []
    for tr in soup.find_all('tr', {'class': re.compile(r'ysprow.*')}):
        stats = tr.text.split()
        players.append(stats)
    return players
