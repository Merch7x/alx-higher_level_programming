-- lists all cities contained in hbtn_0d_usa
SELECT id, name
FROM cities
JOIN states ON citites.state_id = states.id;
