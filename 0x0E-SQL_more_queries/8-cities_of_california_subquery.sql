-- lists all records
SELECT id, name FROM states, cities
WHERE states.id=cities.state_id
ORDER BY cities.id ASC;
