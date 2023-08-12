--  creates a table users with the columns:
-- id, email, name and country
CREATE TABLE IF NOT EXISTS users (
    id INT NOT NULL AUTO_INCREMENT,
    email VARCHAR(225) NOT NULL UNIQUE,
    name VARCHAR(225),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US',
    PRIMARY KEY(id)
)
