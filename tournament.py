#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def executeStatement(query,parameter=''):
    """Connects to database, executes statement, and commits the statement execution."""
    conn = connect()
    cur = conn.cursor()
    cur.execute(query,parameter)
    conn.commit()
    #if not "Delete" in query and not "insert" in query:
    try:
        result = cur.fetchall()
    except:
        result = ''
    conn.close()
    
    return result

def deleteMatches():
    """Remove all the match records from the database."""
    executeStatement('Delete from matches')

def deletePlayers():
    """Remove all the player records from the database."""
    executeStatement('Delete from players')

def countPlayers():
    """Returns the number of players currently registered."""
    numPlayers = executeStatement('select count(*) from players')
    
    return numPlayers[0][0]

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    executeStatement("insert into players(name) values (%s)", (name,))


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    return executeStatement('select * from playerStandings')


def reportMatch(winner, loser, isDraw):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
      isDraw:  whether the match was a draw
    """
    
    if isDraw:
        result = -1
    else:
        result = winner
    
    executeStatement("insert into matches(player1,player2,winner) values (%s,%s,%s)", ((winner,),(loser,),(result,)))
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    standings = playerStandings()
    nextRoundMatches = []
    for i in xrange(0,len(standings),2):
        t = standings[i][0],standings[i][1],standings[i+1][0],standings[i+1][1]
        nextRoundMatches.append(t)
        
    return nextRoundMatches