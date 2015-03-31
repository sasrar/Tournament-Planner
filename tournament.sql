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
    --wins integer default 0,
    --matches integer default 0
);

create table matches (
	id serial primary key,
	player1 integer references players(id),
	player2 integer references players(id),
	winner integer references players(id)
);

create view playerWins as
select p.id, p.name, count(m.winner) as wins
from players p
left join matches m on m.winner = p.id
group by p.id, p.name
order by wins;

create view playerMatches as
select player, sum(num) as matches from
(select p.id as player, count(m.player1) as num
from players p
left join matches m on p.id = m.player1
group by p.id
union all
select p.id as player, count(m.player2) as num
from players p
left join matches m on p.id = m.player2
group by p.id
) as playerMatchesUnion
group by player;

create view playerStandings as
select w.id, w.name, w.wins, m.matches
from playerWins w
left join playerMatches m on w.id = m.player
order by w.wins desc, w.id;
