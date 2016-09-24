import sqlite3
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import re

def visualize(stat):
	conn = sqlite3.connect('nflPlayers.db')
	c = conn.cursor()

	qbRawNames = c.execute("SELECT name, %s FROM QuarterBacksWeek2" % stat)
	rowRaw = c.fetchall()
	qbNames = []
	ratings = []
	for row in rowRaw:
		qbNames.append(row[0])
		ratings.append(float(row[1]))


	pos = np.arange(len(qbNames))

	plt.barh(pos, ratings, align='center', alpha=0.5)
	plt.yticks(pos, qbNames)

	plt.xlabel(stat)
	 
	plt.show()

visualize('passingYards')