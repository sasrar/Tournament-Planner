-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create table players (
	id serial primary key,
	name text
);

create table matches (
	id serial primary key,
	player1 integer references players(id),
	player2 integer references players(id),
	winner integer
);

-- Creating view to get aggregate of wins for each player in the players table
create view playerWins as
select p.id, p.name, count(case m.winner when p.id then 1 else NULL end) as wins, count(case m.winner when -1 then 1 else NULL end) as draws
from players p
left join matches m on m.player1 = p.id or m.player2 = p.id
group by p.id, p.name;

-- Creating view to get aggregate of matches for each player in the players table according to the matches table
create view playerMatches as
select p.id as player, count(m.player1) as matches
from players p
left join matches m on p.id = m.player1 or p.id = m.player2
group by p.id;

-- Creating view to get standings for each player in the players table according to the wins, draws, and losses they have
create view playerStandings as
select w.id, w.name, w.wins, m.matches
from playerWins w
left join playerMatches m on w.id = m.player
order by w.wins desc, w.draws desc, w.id;
