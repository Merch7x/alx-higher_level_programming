-- lists all cities contained in hbtn_0d_usa
SELECT id, name
FROM cities AS c JOIN states AS s on c.state_id=s.id;
