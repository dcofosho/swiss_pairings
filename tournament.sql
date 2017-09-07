-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament

CREATE TABLE players ( id SERIAL PRIMARY KEY, name TEXT  );


CREATE TABLE matches ( id SERIAL PRIMARY KEY, 
	winner INTEGER REFERENCES players(id) ON DELETE CASCADE, 
	loser INTEGER REFERENCES players(id) ON DELETE CASCADE );

create view view_wins as
select players.id as id, count(matches.id) as wins
from players left outer join matches
    on players.id = matches.winner
group by players.id;

create view view_played as
select players.id as id, count(matches.id) as played
from players left outer join matches
    on players.id = matches.winner or players.id = matches.loser
group by players.id;

create view standings as
	select view_wins.id as id, view_wins.wins as wins, view_played.played as played
	from view_wins join view_played
		on view_wins.id = view_played.id
	ORDER BY wins;

create view full_standings as
	select players.id, players.name, standings.wins, standings.played
	from players join standings
		on players.id = standings.id
	ORDER BY standings.wins DESC;