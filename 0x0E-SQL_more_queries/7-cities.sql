-- creates the database hbtn_0d_usa and the table cities
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.cities (
	id INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
	state_id INR NOT NULL,
	name VARCHAR(256) NOT NULL, 
	FOREIGN KEY (state_id) REFERENCES hbtn_0d_usa.states(id)
);
