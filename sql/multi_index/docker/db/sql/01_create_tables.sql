DROP TABLE IF EXISTS users;

CREATE TABLE users (
    id INT(11) AUTO_INCREMENT NOT NULL,
    age INT(11) NOT NULL,
    name VARCHAR(64) NOT NULL,
    PRIMARY KEY (id)
);

CREATE INDEX name_age_index on users(name, age)