import scrape_players as scrape, sqlite3

conn = sqlite3.connect('nflPlayers.db')
c = conn.cursor()

def create_QB():
    for week in range(1, 5):
        table_name = 'QuarterBacksWeek' + str(week)
        print(table_name)
        c.execute('CREATE TABLE IF NOT EXISTS ' + table_name + '(name TEXT PRIMARY KEY, team TEXT, games TEXT, qbRating TEXT, completions TEXT, attempts TEXT, passingYards TEXT, passYdsPerAttempt TEXT, passLong TEXT, interceptions TEXT, passTDs TEXT, rushes TEXT, rushYds TEXT, rushYdsPerAttempt TEXT, rushLong TEXT, rushTDs TEXT, sacks TEXT, ydsLost TEXT, fumbles TEXT, fumblesLost TEXT)')
        players = scrape.get_stats('QB', week)
        for stats in players:
            name = stats[0] + " " + stats[1]
            team = stats[2]
            games = stats[3]
            qbRating = stats[4]
            completions = stats[5]
            attempts = stats[6]
            passingYards = stats[7]
            passYdsPerAttempt = stats[8]
            passLong = stats[9]
            interceptions = stats[10]
            passTDs = stats[11]
            rushes = stats[12]
            rushYds = stats[13]
            rushYdsPerAttempt = stats[14]
            rushLong = stats[15]
            rushTDs = stats[16]
            sacks = stats[17]
            ydsLost = stats[18]
            fumbles = stats[19]
            fumblesLost = stats[20]
            c.execute("INSERT INTO " + table_name + '''(name, team, games, qbRating, completions, attempts, passingYards, passYdsPerAttempt, passLong, interceptions, passTDs, rushes, rushYds, rushYdsPerAttempt, rushLong, rushTDs, sacks, ydsLost, fumbles, fumblesLost)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (name, team, games, qbRating, completions, attempts, passingYards, passYdsPerAttempt, passLong, interceptions, passTDs, rushes, rushYds, rushYdsPerAttempt, rushLong, rushTDs, sacks, ydsLost, fumbles, fumblesLost))
            conn.commit()

def create_RB():
    for week in range(1, 5):
        table_name = 'RunningBacksWeek' + str(week)
        print(table_name)
        c.execute('CREATE TABLE IF NOT EXISTS ' + table_name + '(name TEXT PRIMARY KEY, team TEXT, games TEXT, rushes TEXT, rushYds TEXT, rushYdsPerAttempt TEXT, rushLong TEXT, rushTDs TEXT, receptions TEXT, targets TEXT, receivingYds TEXT, receivingYdsPerAttempt TEXT, receivingLong TEXT, receivingTDs TEXT, fumbles TEXT, fumblesLost TEXT)')
        players = scrape.get_stats('RB', week)
        for stats in players:
            name = stats[0] + " " + stats[1]
            team = stats[2]
            games = stats[3]
            rushes = stats[4]
            rushYds = stats[5]
            rushYdsPerAttempt = stats[6]
            rushLong = stats[7]
            rushTDs = stats[8]
            receptions = stats[9]
            targets = stats[10]
            receivingYds = stats[11]
            receivingYdsPerAttempt = stats[12]
            receivingLong = stats[13]
            receivingTDs = stats[14]
            fumbles = stats[15]
            fumblesLost = stats[16]
            c.execute("INSERT INTO " + table_name + '''(name, team, games, rushes, rushYds, rushYdsPerAttempt, rushLong, rushTDs, receptions, targets, receivingYds, receivingYdsPerAttempt, receivingLong, receivingTDs, fumbles, fumblesLost)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)''', (name, team, games, rushes, rushYds, rushYdsPerAttempt, rushLong, rushTDs, receptions, targets, receivingYds, receivingYdsPerAttempt, receivingLong, receivingTDs, fumbles, fumblesLost))
            conn.commit()

def create_WR():
    for week in range(1, 5):
        table_name = 'WideReceiversWeek' + str(week)
        print(table_name)
        c.execute('CREATE TABLE IF NOT EXISTS ' + table_name + '(name TEXT PRIMARY KEY, team TEXT, games TEXT, receptions TEXT, targets TEXT, receivingYds TEXT, receivingYdsPerAttempt TEXT, receivingLong TEXT, receivingTDs TEXT, fumbles TEXT, fumblesLost TEXT)')
        players = scrape.get_stats('WR', week)
        for stats in players:
            name = stats[0] + " " + stats[1]
            team = stats[2]
            games = stats[3]
            receptions = stats[4]
            targets = stats[5]
            receivingYds = stats[6]
            receivingYdsPerAttempt = stats[7]
            receivingLong = stats[8]
            receivingTDs = stats[9]
            fumbles = stats[10]
            fumblesLost = stats[11]
            c.execute("INSERT INTO " + table_name + '''(name, team, games, receptions, targets, receivingYds, receivingYdsPerAttempt, receivingLong, receivingTDs, fumbles, fumblesLost)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (name, team, games, receptions, targets, receivingYds, receivingYdsPerAttempt, receivingLong, receivingTDs, fumbles, fumblesLost))
            conn.commit()

def create_TE():
    for week in range(1, 5):
        table_name = 'TightEndsWeek' + str(week)
        print(table_name)
        c.execute('CREATE TABLE IF NOT EXISTS ' + table_name + '(name TEXT PRIMARY KEY, team TEXT, games TEXT, receptions TEXT, targets TEXT, receivingYds TEXT, receivingYdsPerAttempt TEXT, receivingLong TEXT, receivingTDs TEXT, fumbles TEXT, fumblesLost TEXT)')
        players = scrape.get_stats('TE', week)
        for stats in players:
            name = stats[0] + " " + stats[1]
            team = stats[2]
            games = stats[3]
            receptions = stats[4]
            targets = stats[5]
            receivingYds = stats[6]
            receivingYdsPerAttempt = stats[7]
            receivingLong = stats[8]
            receivingTDs = stats[9]
            fumbles = stats[10]
            fumblesLost = stats[11]
            c.execute("INSERT INTO " + table_name + '''(name, team, games, receptions, targets, receivingYds, receivingYdsPerAttempt, receivingLong, receivingTDs, fumbles, fumblesLost)
                        VALUES (?,?,?,?,?,?,?,?,?,?,?)''', (name, team, games, receptions, targets, receivingYds, receivingYdsPerAttempt, receivingLong, receivingTDs, fumbles, fumblesLost))
            conn.commit()

create_QB()
create_RB()
create_WR()
create_TE()
