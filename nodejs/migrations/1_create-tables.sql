DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS projects;
-- DROP TABLE IF EXISTS migrations;

CREATE TABLE users(
    id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    email VARCHAR(200) NOT NULL,
    password VARCHAR(200) NOT NULL,
    phone VARCHAR(20),
    profile json,
    bio VARCHAR(500)
);

CREATE TABLE projects(
    id SERIAL PRIMARY KEY,
    userId INT,
    title VARCHAR(300) NOT NULL,
    description VARCHAR(500) NOT NULL,
    link VARCHAR(300),
    category VARCHAR(200),
    tags VARCHAR[],
    likes INT,
    createdAt TIMESTAMP,
    CONSTRAINT fk_user
        FOREIGN KEY(userId)
            REFERENCES users(id)
);