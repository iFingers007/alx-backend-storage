-- creates a table users following some requirements
CREATE TABLE IF NOT EXISTS users (
       id INT PRIMARY KEY AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255)
       );
       
