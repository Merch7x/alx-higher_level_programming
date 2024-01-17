-- create mysql user
CREATE USER `user_0d_1`@`localhost` IF NOT EXISTS IDENTIFIED BY `user_0d_1_pwd`;

GRANT SELECT
ON *.*
TO `user_0d_1`@`localhost`;
