import sqlite3

conn = sqlite3.connect("boxoffice.db")

cur = conn.cursor()

cur.execute('''CREATE TABLE Actor (
	actor_id INT NOT NULL,
    fname VARCHAR(40),
    lname VARCHAR(40),
    age INT,
    sex CHAR,
    PRIMARY KEY (actor_id)
);''')

conn.commit()

cur.execute('''CREATE TABLE Director (
	director_id INT NOT NULL,
	fname VARCHAR(40),
    lname VARCHAR(40),
    age INT,
    sex CHAR,
    PRIMARY KEY (director_id)
);''')

conn.commit()

cur.execute('''CREATE TABLE Studio (
	studio_id INT NOT NULL,
    studio_name VARCHAR(40),
    PRIMARY KEY (studio_id)
);''')

conn.commit()

cur.execute('''CREATE TABLE Producer (
	producer_id INT NOT NULL,
	fname VARCHAR(40),
    lname VARCHAR(40),
    age INT,
    sex CHAR,
    PRIMARY KEY (producer_id)
);''')
conn.commit()

cur.execute('''CREATE TABLE Cast (
    movie_id INT NOT NULL,
	actor_id INT NOT NULL,
    is_star BIT,
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
	FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
);''')
conn.commit()

cur.execute('''
CREATE TABLE ProducingCredit (
	movie_id INT NOT NULL,
    producer_id INT NOT NULL,
    PRIMARY KEY (movie_id, producer_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
	FOREIGN KEY (producer_id) REFERENCES Producer(producer_id)
);''')
conn.commit()

cur.execute('''CREATE TABLE SalesRecord (
	sales_record_id INT NOT NULL,
    opening_weekend INT,
    worldwide_total INT,
    domestic_total INT,
    foreign_total INT,
    PRIMARY KEY (sales_record_id)
);''')
conn.commit()


cur.execute('''CREATE TABLE Movie (
	movie_id INT NOT NULL,
    movie_title VARCHAR(50),
    release_date DATE,
    budget INT,
    director_id INT,
    studio_id INT,
    sales_record_id INT,
    PRIMARY KEY (movie_id),
    FOREIGN KEY (director_id) REFERENCES Director(director_id),
    FOREIGN KEY (studio_id) REFERENCES Studio(studio_id),
	FOREIGN KEY (sales_record_id) REFERENCES SalesRecord(sales_record_id)
);''')
conn.commit()

conn.close()
