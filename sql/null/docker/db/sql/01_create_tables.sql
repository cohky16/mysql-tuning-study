DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT(11) AUTO_INCREMENT NOT NULL,
    age INT(11),
    name VARCHAR(64),
    PRIMARY KEY (id)
);

CREATE INDEX name_index on users(name)