import sqlite3

conn = sqlite3.connect("boxoffice.db")

cur = conn.cursor()

cur.execute('''CREATE TABLE Actor (
	actor_id INTEGER NOT NULL,
    fname VARCHAR(40),
    lname VARCHAR(40),
    age INTEGER,
    sex CHAR,
    PRIMARY KEY (actor_id)
);''')

conn.commit()

cur.execute('''CREATE TABLE Director (
	director_id INTEGER NOT NULL,
	fname VARCHAR(40),
    lname VARCHAR(40),
    age INTEGER,
    sex CHAR,
    PRIMARY KEY (director_id)
);''')

conn.commit()

cur.execute('''CREATE TABLE Studio (
	studio_id INTEGER NOT NULL,
    studio_name VARCHAR(40),
    PRIMARY KEY (studio_id)
);''')

conn.commit()

cur.execute('''CREATE TABLE Producer (
	producer_id INTEGER NOT NULL,
	fname VARCHAR(40),
    lname VARCHAR(40),
    age INTEGER,
    sex CHAR,
    PRIMARY KEY (producer_id)
);''')
conn.commit()

cur.execute('''CREATE TABLE Cast (
    movie_id INTEGER NOT NULL,
	actor_id INTEGER NOT NULL,
    is_star BIT,
    role VARCHAR(30),
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
	FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
);''')
conn.commit()

cur.execute('''
CREATE TABLE ProducingCredit (
	movie_id INTEGER NOT NULL,
    producer_id INTEGER NOT NULL,
    PRIMARY KEY (movie_id, producer_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
	FOREIGN KEY (producer_id) REFERENCES Producer(producer_id)
);''')
conn.commit()

cur.execute('''CREATE TABLE SalesRecord (
	sales_record_id INTEGER NOT NULL,
    domestic_opening INTEGER,
    worldwide_total INTEGER,
    domestic_total INTEGER,
    foreign_total INTEGER,
    PRIMARY KEY (sales_record_id)
);''')
conn.commit()


cur.execute('''CREATE TABLE Movie (
	movie_id INTEGER NOT NULL,
    movie_title VARCHAR(50),
    release_date DATE,
    budget INTEGER,
    director_id INTEGER,
    studio_id INTEGER,
    sales_record_id INTEGER,
    PRIMARY KEY (movie_id),
    FOREIGN KEY (director_id) REFERENCES Director(director_id),
    FOREIGN KEY (studio_id) REFERENCES Studio(studio_id),
	FOREIGN KEY (sales_record_id) REFERENCES SalesRecord(sales_record_id)
);''')
conn.commit()


# inserting into SalesRecord
cur.execute('''INSERT INTO SalesRecord (sales_record_id, domestic_opening, worldwide_total, domestic_total, foreign_total)
VALUES
(1, 162022044, 1445638421, 636238421, 809400000),
(2, 146361865, 1361972248, 574934330, 787037918),
(3, 82455420, 957775395, 329203395, 628572000),
(4, 118414021, 845555777, 358995815, 486559962),
(5, 67017410, 704875015, 146126015, 558749000),
(6, 120663589, 690615475, 381311319, 309304156),
(7, 39005800, 625420096, 217320096, 408100000),
(8, 95578040, 569626289, 298172056, 271454233),
(9, 54688347, 567535383, 172135383, 395400000),
(10, 29602429, 496444308, 154426697, 342017611),
(11, 106109650, 476071180, 214504909, 261566271),
(12, 73817950, 440157245, 187131806, 253025439),
(13, 61045464, 438966392, 157066392, 281900000),
(14, 27686211, 434336589, 124436589, 309900000),
(15, 30002735, 397700317, 82600317, 315100000),
(16, 60368101, 383963057, 174480468, 209482589),
(17, 44607143, 337128867, 166350594, 170778273),
(18, 80001720, 291493620, 137275620, 154218000),
(19, 12453275, 278879060, 125331060, 153548000),
(20, 58370007, 276148615, 156248615, 119900000),
(21, 55043679, 271333313, 108133313, 163200000),
(22, 32603336, 269467073, 86267073, 183200000),
(23, 93224755, 261656269, 180756269, 80900000),
(24, 19698228, 252579504, 63947165, 188632339),
(25, 19680879, 250570396, 184178046, 66392350),
(26, 20638887, 220993117, 61524375, 159468742),
(27, 37205784, 208177026, 93277026, 114900000),
(28, 6000344, 207710447, 88107085, 119603362),
(29, 30002525, 207571582, 102996915, 104574667),
(30, 46110859, 206102524, 84500223, 121602301),
(31, 22764354, 202231360, 65231360, 137000000),
(32, 34604229, 191067560, 92373751, 98693809),
(33, 33013036, 189086877, 82156962, 106929915),
(34, 28007544, 180513586, 118613586, 61900000),
(35, 44447270, 168961389, 108161389, 60800000),
(36, 13011722, 167767226, 46076328, 121690898),
(37, 23253655, 156955813, 67955813, 89000000),
(38, 24504315, 147033054, 67233054, 79800000),
(39, 26497600, 136274553, 65537395, 70737158),
(40, 30111158, 134038006, 57638006, 76400000),
(41, 25030225, 130788072, 72488072, 58300000),
(42, 6892182, 128780000, 17487476, 95095974),
(43, 14279529, 122290456, 42471412, 79819044),
(44, 17410552, 121987262, 44428554, 77558708),
(45, 24082475, 117449790, 67653287, 49796503),
(46, 18309301, 111820712, 53607898, 58212814),
(47, NULL, 106770959, NULL, 106770959),
(48, 11419975, 106722608, 56418793, 50303815),
(49, 661230, 105045025, 33840640, 71204385),
(50, 14079512, 104272136, 40774679, 63497457);
''')
conn.commit()

# all studio entries
studio_data = [
    ("Warner Bros."),
    ("Universal Pictures"),
    ("Walt Disney Studios Motion Pictures"),
    ("Columbia Pictures"),
    ("Paramount Pictures"),
    ("Lionsgate Films"),
    ("United Artists Releasing"),
    ("AMC Theaters"),
    ("Angel Studios"),
    ("GKIDS"),
    ("Yash Raj Films USA Inc."),
    ("Sony Pictures Releasing"),
    ("Toho International"),
    ("Searchlight Pictures"),
    ("Screen Gems")
]
for studio_entry in studio_data:
    cur.execute("INSERT INTO Studio (studio_name) VALUES (?);", (studio_entry,))

conn.commit()

director_data = [
    ('Greta', 'Gerwig', 38, 'F'),
    ('Aaron', 'Horvath', 43, 'M'),
    ('Christopher', 'Nolan', 53, 'M'),
    ('James', 'Gunn', 57, 'M'),
    ('Louis', 'Leterrier', 50, 'M'),
    ('Joaquim', 'Dos Santos', 46, 'M'),
    ('Paul', 'King', 45, 'M'),
    ('Rob', 'Marshall', 63, 'M'),
    ('Christopher', 'McQuarrie', 55, 'M'),
    ('Peter', 'Sohn', 46, 'M'),
    ('Peyton', 'Reed', 59, 'M'),
    ('Chad', 'Stahelski', 55, 'M'),
    ('Steven', 'Caple Jr.', 36, 'M'),
    ('James', 'Wan', 47, 'M'),
    ('Ben', 'Wheatley', 51, 'M'),
    ('James', 'Mangold', 60, 'M'),
    ('Emma', 'Tammi', 54, 'F'),
    ('Benjamin', "Renner", 40, 'M'),
    ('Micheal', 'B. Jordan', 37, 'M'),
    ('Andres', 'Muschietti', 50, 'M'),
    ('Micheal', 'Chaves', 39, 'M'),
    ('Sam', 'Wrench', 33, 'M'),
    ('Chris', 'Buck', 66, 'M'),
    ('Alejandro', 'Monteverde', 46, 'M'),
    ('Ridley', 'Scott', 86, 'M'),
    ('John', 'Francis Daley', 38, 'M'),
    ('Will', "Gluck", 45, 'M'),
    ('Walt', 'Dohrn', 53, 'M'),
    ('Nia', 'DaCosta', 34, 'F'),
    ('Cal', 'Brunker', 45, 'M'),
    ('Antoine', 'Fuqua', 58, 'M'),
    ('Patrick', 'Wilson', 50, 'M'),
    ('Jeff', 'Rowe', 37, 'M'),
    ("Tyler", "Gillet", 42, 'M'),
    ("Hayao", "Miyazaki", 83, 'M'),
    ('Martin', 'Scorsese', 81, 'M'),
    ('Lee', 'Cronin', 50, 'M'),
    ('David', 'Green', 48, 'M'),
    ('David', 'Sandberg', 43, 'M'),
    ('Angel', 'Soto', 41, 'M'),
    ('Siddharth', 'Anand', 45, 'M'),
    ('Kenneth', 'Branagh', 63, 'M'),
    ('Neill', 'Blomkamp', 44, 'M'),
    ('Justin', 'Simien', 40, 'M'),
    ('Kevin', 'Greutert', 58, 'M'),
    ('Yuzuru', 'Tachikawa', 42, 'M'),
    ('Takashi', 'Yamazaki', 59, 'M'),
    ('Yorgos', 'Lanthimos', 50, 'M'),
    ('Gareth', 'Edwards', 48, 'M')
]

for director in director_data:
    cur.execute("INSERT INTO Director (	fname, lname, age, sex) VALUES (?,?,?,?);", director)

conn.commit()

actor_data = [
    ('Margot', 'Robbie', 33, 'F'),
    ('Ryan', 'Gosling', 43, 'M'),
    ('Issa', 'Rae', 39, 'F'),
    ('Kate', 'McKinnon', 40, 'F'),
    #mario
    ('Chris', 'Pratt', 44, "M"),
    ('Anya','Taylor-Joy', 27, 'F'),
    ('Charlie', 'Day', 48, 'M'),
    ('Jack', 'Black', 54, 'M'),
    # oppenheimer
    ('Cillian', "Murphy", 47, 'M'),
    ("Emily", "Blunt", 41, 'F'),
    ('Matt', 'Damon', 53, "M"),
    ('Robert', "Downey Jr.", 58, 'M'),
    # gotg
    ('Chukwudi', 'Iwuji', 48, 'M'),
    ('Bradley', 'Cooper', 49, 'M'),
    ('Pom', 'Klementieff', 37, 'F'),
    # fast X
    ('Vin', 'Diesel', 56, "M"),
    ("Michelle", 'Rodriguez', 45, 'F'),
    ('Jason', 'Statham', 56, 'M'),
    ('Jardana', 'Brewster', 43, 'F')
]

for actor in actor_data:
    cur.execute("INSERT INTO Actor (fname ,lname, age, sex) VALUES (?,?,?,?);", actor)


producer_data = [
    ('Robbie', 'Brenner', None ,'M'),
    ('David', 'Heyman', None, 'M'),
    ('Margot', 'Robbie', 33, 'F'),
    ('Christopher', 'Meledandri', 64, 'M'),
    ('Shigeru', 'Miyamoto', 71, 'M'),
    # oppenheimer
    ('Christopher', 'Nolan', 53, "M"),
    ('Charles', 'Roven', 74, 'M'),
    ('Emma', 'Thomas', 52, 'F'),
    # gotg
    ('Kevin', 'Feige', 50, 'M'),
    # Fast X
    ('Vin', 'Diesel', 56, 'M'),
    ('Jeff', 'Kirschenbaum', 56, 'M'),
    ('Justin', 'Lin', 52, 'M'),
    ('Neal', 'H. Moritz', 64, 'M'),
    ('Samantha', 'Vincent', None, 'F')
]

for producer in producer_data:
    cur.execute("INSERT INTO Actor (fname ,lname, age, sex) VALUES (?,?,?,?);", producer)


cast_data = [
    (1, 1, 1, 'Barbie'),
    (1, 2, 1, 'Ken'),
    (1, 3, 0, 'Barbie'),
    (1, 4, 0, 'Barbie'),
    (2, 5, 1, 'Mario'),
    (2, 6, 1, 'Princess Peach'),
    (2, 7, 1, 'Luigi'),
    (2, 8, 1, 'Bowser'),
    # oppenheimer
    (3, 9, 1, 'J. Robert Oppenheimer'),
    (3, 10, 1, 'Kitty Oppenheimer'),
    (3, 11, 1, 'Leslie Groves'),
    (3, 12, 1, 'Lewis Strauss'),
    # gotg
    (4, 5, 1, 'Star-Lord'),
    (4, 13, 0, 'The High Evolutionary'),
    (4, 14, 1, "Rocket"),
    (4, 15, 1, 'Mantis'),
    # fast X
    (5, 16, 1, 'Dominic Toretto'),
    (5, 17, 1, 'Michelle Rodriguez'),
    (5, 18, 1, 'Shaw'),
    (5, 19, 0, 'Mia')
]

for act in cast_data:
    cur.execute("INSERT INTO Cast (movie_id ,actor_id, is_star, role) VALUES (?,?,?,?);", act)

producing_credits = [
    (1, 1),
    (1, 2),
    (1, 3),
    (2, 4),
    (2, 5),
    (3, 6),
    (3, 7),
    (3, 8),
    (4, 9),
    (5, 10),
    (5, 11),
    (5, 12),
    (5, 13),
    (5, 14),
]

for prod in producing_credits:
    cur.execute("INSERT INTO ProducingCredit (movie_id ,producer_id) VALUES (?,?);", prod)


movie_data = [
    ('Barbie', '2023-07-19', 145000000, 1, 1, 1),
    ('The Super Mario Bros. Movie', '2023-04-05', 100000000, 2, 2, 2),
    ('Oppenheimer', '2023-07-21', 100000000, 3, 2, 3),
    ('Guardians of the Galaxy Vol. 3', '2023-05-05', 250000000, 4, 3, 4),
    ('Fast X', '2023-05-19', 340000000, 5, 2, 5),
    ('Spider-Man: Across the Spider-Verse', '2023-06-02', 100000000, 6, 4, 6),
    ('Wonka', '2023-12-15', 125000000, 7, 1, 7),
    ('The Little Mermaid', '2023-05-26', 240200000, 8, 3, 8),
    ('Mission: Impossible - Dead Reckoning Part One', '2023-07-12', 291000000, 9, 5, 9),
    ('Elemental', '2023-06-16', 200000000, 10, 3, 10),
    ('Ant-Man and the Wasp: Quantumania', '2023-02-17', 275000000, 11, 3, 11),
    ('John Wick: Chapter 4', '2023-03-24', 100000000, 12, 6, 12),
    ('Transformers: Rise of the Beasts', '2023-06-09', 200000000, 13, 5, 13),
    ('Aquaman and the Lost Kingdom', '2023-12-22', 215000000, 14, 1, 14),
    ('Meg 2: The Trench', '2023-08-04', 185000000, 15, 1, 15),
    ('Indiana Jones and the Dial of Destiny', '2023-06-30', 294700000, 16, 3, 16),
    ("The Hunger Games: The Ballad of Songbirds & Snakes", '2023-11-17', 100000000, 17, 6, 17),
    ("Five Nights at Freddy's", '2023-10-27', 20000000, 18, 2, 18),
    ('Migration', '2023-12-22', 72000000, 19, 2, 19),
    ('Creed III', '2023-03-03', 75000000, 20, 7, 20),
    ('The Flash', '2023-06-16', 200000000, 21, 1, 21),
    ('The Nun II', '2023-09-08', 28500000, 22, 1, 22),
    ('Taylor Swift: The Eras Tour', '2023-10-13', 10000000, 23, 8, 23),
    ('Wish', '2023-11-22', 200000000, 24, 3, 24),
    ('Sound of Freedom', '2023-07-04', 14500000, 25, 9, 25),
    ('Napoleon', '2023-11-22', 200000000, 26, 4, 26),
    ('Dungeons & Dragons: Honor Among Thieves', '2023-03-31', 150000000, 27, 5, 27),
    ('Anyone But You', '2023-12-11', 25000000, 28, 4, 28),
    ('Trolls Band Together', '2023-10-12', 95000000, 29, 2, 29),
    ('The Marvels', '2023-11-10', 270000000, 30, 3, 30),
    ('PAW Patrol: The Mighty Movie', '2023-09-29', 30000000, 31, 5, 31),
    ('The Equalizer 3', '2023-09-01', 70000000, 32, 4, 32),
    ('Insidious: The Red Door', '2023-07-05', 16000000, 33, 15, 33),
    ('Teenage Mutant Ninja Turtles: Mutant Mayhem', '2023-08-02', 70000000, 34, 5, 34),
    ('Scream VI', '2023-03-10', 35000000, 35, 5, 35),
    ('The Boy and the Heron', '2023-12-08', 50000000, 36, 10, 36),
    ('Killers of the Flower Moon', '2023-10-20', 200000000, 37, 5, 37),
    ('Evil Dead Rise', '2023-04-21', 15000000, 38, 1, 38),
    ('The Exorcist: Believer', '2023-10-06', 30000000, 39, 2, 39),
    ('Shazam! Fury of the Gods', '2023-03-17', 125000000, 40, 1, 40),
    ('Blue Beetle', '2023-08-18', 104000000, 41, 1, 41),
    ('Pathaan', '2023-01-25', 28000000, 42, 11, 42),
    ('A Haunting in Venice', '2023-09-15', 70000000, 43, 3, 43),
    ('Gran Turismo', '2023-08-25', 60000000, 44, 12, 44),
    ('Haunted Mansion', '2023-07-15', 150000000, 45, 6, 45),
    ('Saw X', '2023-09-29', 13000000, 46, 6, 46),
    ('Detective Conan: Black Iron Submarine', '2023-04-14', None, 47, None, 47),
    ('Godzilla Minus One', '2023-12-01', 15000000, 48, 13, 48),
    ('Poor Things', '2023-09-01', 35000000, 49, 14, 49),
    ('The Creator', '2023-09-29', 80000000, 50, 3, 50)
]

for movie in movie_data:
    cur.execute("INSERT INTO Movie (movie_title, release_date, budget, director_id, studio_id, sales_record_id) VALUES (?,?,?,?,?,?);", movie)

conn.commit()
conn.close()
