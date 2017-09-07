#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2
import operator

def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")

def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM players;") 
    conn.commit()
    cursor.close()
    conn.close()

def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM matches;") 
    conn.commit()
    cursor.close()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM players;")
    conn.commit()
    count = cursor.fetchall()[0][0]
    cursor.close()
    conn.close()
    return count

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    cursor = conn.cursor()
    sql = "INSERT INTO players (name) VALUES (%s);"
    data = (name, )
    cursor.execute(sql, data) 
    conn.commit()
    cursor.close()
    conn.close()

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    cursor = conn.cursor()
    sql = "INSERT INTO matches (winner, loser) VALUES (%s, %s);"
    data = (winner, loser)
    cursor.execute(sql, data)
    conn.commit()
    cursor.close()
    conn.close()

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
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM full_standings;")
    conn.commit()
    sorted_scores = cursor.fetchall()
    cursor.close()
    conn.close()
    return sorted_scores

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
    conn = connect()
    cursor = conn.cursor()
    swiss_pairs=[]
    standings = playerStandings()
    numStandings = len(standings)
    for x in range (0, numStandings-1, 2):
        sql = "SELECT name FROM players WHERE id = %s;"
        data = (standings[x][0], )
        cursor.execute(sql, data)
        name1 = cursor.fetchall()[0][0]
        data = (standings[x+1][0], )
        cursor.execute(sql, data)
        name2 = cursor.fetchall()[0][0]
        swiss_pairs.append((standings[x][0], name1, standings[x+1][0], name2))
    return swiss_pairs

