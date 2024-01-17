-- set the default character set and collation for the database
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- convert table to new character set
AlTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;


ALTER TABLE hbtn_0c_0.first_table
MODIFY COLUMN name VARCHAR(255) CHARACTER SET utf8mb4 COLLATE
utf8mb4_unicode_ci;
