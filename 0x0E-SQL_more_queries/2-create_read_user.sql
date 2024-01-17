-- create a database and a user
CREATE DATABASE 'hbtn_0d_2' IF NOT EXISTS;

Use `hbtn_0d_2`;

CREATE USER 'user_0d_2'@'localhost';

GRANT SELECT ON *.* TO 'user_0d_2'@'localhost';
