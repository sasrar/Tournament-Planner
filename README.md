# Tournament-Planner
This is a Python module to keep track of players and matches in a game tournament.

tournament.py:
    Includes code to connect to the database and populate it with player and match data. 
    It also includes code to get player standings and the next round match pairings.

tournament_test.py:
    Includes unit tests for various testing scenarios including adding and deleting matches,
    adding or deleting players, getting player standings, and getting the next round match pairings.
    
Steps to run:
	Before running the program you need to use the create database command in psql to create the database. Use the name 'tournament' for your database.
	
	Now you can connect to the tournament database and create the database tables and views written in tournament.sql. You can do this in two ways:
	1. Paste each statement from tournament.sql into the psql command line and executing the statement.
	2. Use the command "\i tournament.sql" to import the whole file into psql at once.
	
	Now you can run the unit tests by running "python tournament_test.py" in the command prompt.
	
	Note: you need to have the pscopg2 module installed on your machine to successfully connect to the database and run the tests.
