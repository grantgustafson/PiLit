CREATE TABLE modules (
	id INTEGER NOT NULL, 
	hostname VARCHAR(64) NOT NULL, 
	location VARCHAR(64) NOT NULL, 
	name VARCHAR(64), 
	PRIMARY KEY (id)
);


CREATE TABLE strips (
	id INTEGER NOT NULL, 
	length INTEGER NOT NULL, 
	PRIMARY KEY (id)
);


CREATE TABLE segments (
	id INTEGER NOT NULL, 
	num_pixels INTEGER NOT NULL, 
	module_startpixel INTEGER NOT NULL, 
	forwards BOOLEAN NOT NULL, 
	strip_startpixel INTEGER, 
	module_id INTEGER, 
	strip_id INTEGER, 
	PRIMARY KEY (id), 
	CHECK (forwards IN (0, 1)), 
	FOREIGN KEY(module_id) REFERENCES modules (id), 
	FOREIGN KEY(strip_id) REFERENCES strips (id)
);


