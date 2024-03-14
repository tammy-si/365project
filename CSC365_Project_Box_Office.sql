-- create database and tables

CREATE DATABASE boxoffice;
USE boxoffice;

CREATE TABLE People (
    person_id INTEGER AUTO_INCREMENT,
    fname VARCHAR(40),
    lname VARCHAR(40),
    age INTEGER,
    sex CHAR,
    PRIMARY KEY (person_id)
);
ALTER TABLE People AUTO_INCREMENT=100;
    
CREATE TABLE Actor(
    actor_id INTEGER NOT NULL AUTO_INCREMENT,
    roles_played INT,
    acting_awards INT,
    person_id INT,
    PRIMARY KEY (actor_id),
    FOREIGN KEY (person_id) REFERENCES People(person_id)
);
ALTER TABLE Actor AUTO_INCREMENT=100;

CREATE TABLE Director (
    director_id INTEGER NOT NULL AUTO_INCREMENT,
    movies_directed INT,
    directing_awards INT,
    person_id INT,
    PRIMARY KEY (director_id),
    FOREIGN KEY (person_id) REFERENCES People(person_id)
);
ALTER TABLE Director AUTO_INCREMENT=100;

CREATE TABLE Producer (
    producer_id INTEGER NOT NULL AUTO_INCREMENT,
    movies_produced INT,
    person_id INT,
    PRIMARY KEY (producer_id),
    FOREIGN KEY (person_id) REFERENCES People(person_id)
);
ALTER TABLE Producer AUTO_INCREMENT=100;

CREATE TABLE Studio (
    studio_id INTEGER NOT NULL AUTO_INCREMENT,
    studio_name VARCHAR(40),
    PRIMARY KEY (studio_id)
);
ALTER TABLE Studio AUTO_INCREMENT=100;

CREATE TABLE SalesRecord (
    sales_record_id INTEGER NOT NULL AUTO_INCREMENT,
    domestic_opening INTEGER,
    worldwide_total INTEGER,
    domestic_total INTEGER,
    foreign_total INTEGER,
    PRIMARY KEY (sales_record_id)
);
ALTER TABLE SalesRecord AUTO_INCREMENT=100;

CREATE TABLE Movie (
    movie_id INTEGER NOT NULL AUTO_INCREMENT,
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
);
ALTER TABLE Movie AUTO_INCREMENT=1;

CREATE TABLE MovieCast (
    movie_id INTEGER NOT NULL,
    actor_id INTEGER NOT NULL,
    is_star BIT,
    role VARCHAR(30),
    PRIMARY KEY (movie_id, actor_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (actor_id) REFERENCES Actor(actor_id)
);

CREATE TABLE ProducingCredit (
    movie_id INTEGER NOT NULL,
    producer_id INTEGER NOT NULL,
    PRIMARY KEY (movie_id, producer_id),
    FOREIGN KEY (movie_id) REFERENCES Movie(movie_id),
    FOREIGN KEY (producer_id) REFERENCES Producer(producer_id)
);

-- populating tables
INSERT INTO SalesRecord (domestic_opening, worldwide_total, domestic_total, foreign_total) VALUES
(162022044, 1445638421, 636238421, 809400000),
(146361865, 1361972248, 574934330, 787037918),
(82455420, 957775395, 329203395, 628572000),
(118414021, 845555777, 358995815, 486559962),
(67017410, 704875015, 146126015, 558749000),
(120663589, 690615475, 381311319, 309304156),
(39005800, 625420096, 217320096, 408100000),
(95578040, 569626289, 298172056, 271454233),
(54688347, 567535383, 172135383, 395400000),
(29602429, 496444308, 154426697, 342017611),
(106109650, 476071180, 214504909, 261566271),
(73817950, 440157245, 187131806, 253025439),
(61045464, 438966392, 157066392, 281900000),
(27686211, 434336589, 124436589, 309900000),
(30002735, 397700317, 82600317, 315100000),
(60368101, 383963057, 174480468, 209482589),
(44607143, 337128867, 166350594, 170778273),
(80001720, 291493620, 137275620, 154218000),
(12453275, 278879060, 125331060, 153548000),
(58370007, 276148615, 156248615, 119900000),
(55043679, 271333313, 108133313, 163200000),
(32603336, 269467073, 86267073, 183200000),
(93224755, 261656269, 180756269, 80900000),
(19698228, 252579504, 63947165, 188632339),
(19680879, 250570396, 184178046, 66392350),
(20638887, 220993117, 61524375, 159468742),
(37205784, 208177026, 93277026, 114900000),
(6000344, 207710447, 88107085, 119603362),
(30002525, 207571582, 102996915, 104574667),
(46110859, 206102524, 84500223, 121602301),
(22764354, 202231360, 65231360, 137000000),
(34604229, 191067560, 92373751, 98693809),
(33013036, 189086877, 82156962, 106929915),
(28007544, 180513586, 118613586, 61900000),
(44447270, 168961389, 108161389, 60800000),
(13011722, 167767226, 46076328, 121690898),
(23253655, 156955813, 67955813, 89000000),
(24504315, 147033054, 67233054, 79800000),
(26497600, 136274553, 65537395, 70737158),
(30111158, 134038006, 57638006, 76400000),
(25030225, 130788072, 72488072, 58300000),
(6892182, 128780000, 17487476, 95095974),
(14279529, 122290456, 42471412, 79819044),
(17410552, 121987262, 44428554, 77558708),
(24082475, 117449790, 67653287, 49796503),
(18309301, 111820712, 53607898, 58212814),
(NULL, 106770959, NULL, 106770959),
(11419975, 106722608, 56418793, 50303815),
(661230, 105045025, 33840640, 71204385),
(14079512, 104272136, 40774679, 63497457);

INSERT INTO Studio(studio_name) VALUES
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
("Screen Gems");

INSERT INTO People(fname, lname, age, sex) VALUES
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
('Francis', 'Lawrence', 52, 'M'),
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
('Gareth', 'Edwards', 48, 'M');

INSERT INTO Director(movies_directed, directing_awards, person_id) VALUES
(3, 4, 100),
(17, 2, 101),
(10, 2, 102),
(6, 5, 103),
(8, 2, 104),
(19, 3, 105),
(12, 5, 106),
(14, 1, 107),
(10, 2, 108),
(11, 3, 109),
(14, 0, 110),
(7, 2, 111),
(9, 2, 112),
(13, 3, 113),
(16, 4, 114),
(3, 1, 115),
(6, 1, 116),
(11, 5, 117),
(13, 2, 118),
(14, 5, 119),
(19, 2, 120),
(4, 4, 121),
(6, 1, 122),
(11, 3, 123),
(15, 4, 124),
(15, 1, 125),
(17, 4, 126),
(18, 5, 127),
(17, 4, 128),
(5, 0, 129),
(11, 2, 130),
(11, 5, 131),
(10, 2, 132),
(15, 0, 133),
(16, 4, 134),
(9, 4, 135),
(18, 0, 136),
(19, 2, 137),
(10, 3, 138),
(3, 3, 139),
(20, 2, 140),
(13, 1, 141),
(4, 1, 142),
(14, 3, 143),
(5, 3, 144),
(19, 1, 145),
(8, 5, 146),
(17, 5, 147),
(18, 5, 148),
(2, 2, 149);

INSERT INTO People(fname, lname, age, sex) VALUES
('Margot', 'Robbie', 33, 'F'),
('Ryan', 'Gosling', 43, 'M'),
('Issa', 'Rae', 39, 'F'),
('Kate', 'McKinnon', 40, 'F'),
('Chris', 'Pratt', 44, "M"),
('Anya', 'Taylor-Joy', 27, 'F'),
('Charlie', 'Day', 48, 'M'),
('Jack', 'Black', 54, 'M'),
('Cillian', "Murphy", 47, 'M'),
("Emily", "Blunt", 41, 'F'),
('Matt', 'Damon', 53, "M"),
('Robert', "Downey Jr.", 58, 'M'),
('Chukwudi', 'Iwuji', 48, 'M'),
('Bradley', 'Cooper', 49, 'M'),
('Pom', 'Klementieff', 37, 'F'),
('Vin', 'Diesel', 56, "M"),
("Michelle", 'Rodriguez', 45, 'F'),
('Jason', 'Statham', 56, 'M'),
('Jardana', 'Brewster', 43, 'F');

INSERT INTO Actor(roles_played, acting_awards, person_id) VALUES
(4, 3, 150),
(6, 2, 151),
(18, 0, 152),
(14, 2, 153),
(18, 5, 154),
(20, 3, 155),
(14, 5, 156),
(15, 4, 157),
(2, 1, 158),
(14, 0, 159),
(9, 1, 160),
(15, 4, 161),
(20, 2, 162),
(17, 4, 163),
(13, 2, 164),
(10, 3, 165),
(13, 3, 166),
(17, 2, 167),
(13, 5, 168);

INSERT INTO People(fname, lname, age, sex) VALUES
('Robbie', 'Brenner', -1, 'M'),
('David', 'Heyman', -1, 'M'),
('Margot', 'Robbie', 33, 'F'),
('Christopher', 'Meledandri', 64, 'M'),
('Shigeru', 'Miyamoto', 71, 'M'),
('Christopher', 'Nolan', 53, "M"),
('Charles', 'Roven', 74, 'M'),
('Emma', 'Thomas', 52, 'F'),
('Kevin', 'Feige', 50, 'M'),
('Vin', 'Diesel', 56, 'M'),
('Jeff', 'Kirschenbaum', 56, 'M'),
('Justin', 'Lin', 52, 'M'),
('Neal', 'H. Moritz', 64, 'M'),
('Samantha', 'Vincent', -1, 'F');

INSERT INTO Producer(movies_produced, person_id) VALUES
(7, 169),
(17, 170),
(19, 171),
(10, 172),
(9, 173),
(15, 174),
(18, 175),
(7, 176),
(18, 177),
(20, 178),
(20, 179),
(20, 180),
(11, 181),
(16, 182);

INSERT INTO Movie(movie_title, release_date, budget, director_id, studio_id, sales_record_id) VALUES
('Barbie', '2023-07-19', 145000000, 100, 100, 100),
('The Super Mario Bros. Movie', '2023-04-05', 100000000, 101, 101, 101),
('Oppenheimer', '2023-07-21', 100000000, 102, 101, 102),
('Guardians of the Galaxy Vol. 3', '2023-05-05', 250000000, 103, 102, 103),
('Fast X', '2023-05-19', 340000000, 104, 101, 104),
('Spider-Man: Across the Spider-Verse', '2023-06-02', 100000000, 105, 104, 105),
('Wonka', '2023-12-15', 125000000, 106, 100, 106),
('The Little Mermaid', '2023-05-26', 240200000, 107, 102, 107),
('Mission: Impossible - Dead Reckoning Part One', '2023-07-12', 291000000, 108, 104, 108),
('Elemental', '2023-06-16', 200000000, 109, 102, 109),
('Ant-Man and the Wasp: Quantumania', '2023-02-17', 275000000, 110, 102, 110),
('John Wick: Chapter 4', '2023-03-24', 100000000, 111, 105, 111),
('Transformers: Rise of the Beasts', '2023-06-09', 200000000, 112, 104, 112),
('Aquaman and the Lost Kingdom', '2023-12-22', 215000000, 113, 100, 113),
('Meg 2: The Trench', '2023-08-04', 185000000, 114, 100, 114),
('Indiana Jones and the Dial of Destiny', '2023-06-30', 294700000, 115, 102, 115),
("The Hunger Games: The Ballad of Songbirds & Snakes", '2023-11-17', 100000000, 116, 105, 116),
("Five Nights at Freddy's", '2023-10-27', 20000000, 117, 101, 117),
('Migration', '2023-12-22', 7200000, 118, 101, 118),
('Creed III', '2023-03-03', 7500000, 119, 106, 119),
('The Flash', '2023-06-16', 200000000, 120, 100, 120),
('The Nun II', '2023-09-08', 2850000, 121, 100, 121),
('Taylor Swift: The Eras Tour', '2023-10-13', 10000000, 122, 107, 122),
('Wish', '2023-11-22', 200000000, 123, 102, 123),
('Sound of Freedom', '2023-07-04', 14500000, 124, 109, 124),
('Napoleon', '2023-11-22', 200000000, 125, 104, 125),
('Dungeons & Dragons: Honor Among Thieves', '2023-03-31', 150000000, 126, 105, 126),
('Anyone But You', '2023-12-11', 25000000, 127, 104, 127),
('Trolls Band Together', '2023-10-12', 9500000, 128, 101, 128),
('The Marvels', '2023-11-10', 270000000, 129, 102, 129),
('PAW Patrol: The Mighty Movie', '2023-09-29', 30000000, 130, 104, 130),
('The Equalizer 3', '2023-09-01', 7000000, 131, 103, 131),
('Insidious: The Red Door', '2023-07-05', 16000000, 132, 114, 132),
('Teenage Mutant Ninja Turtles: Mutant Mayhem', '2023-08-02', 7000000, 133, 104, 133),
('Scream VI', '2023-03-10', 35000000, 134, 104, 134),
('The Boy and the Heron', '2023-12-08', 5000000, 135, 109, 135),
('Killers of the Flower Moon', '2023-10-20', 200000000, 136, 104, 136),
('Evil Dead Rise', '2023-04-21', 15000000, 137, 101, 137),
('The Exorcist: Believer', '2023-10-06', 30000000, 138, 102, 138),
('Shazam! Fury of the Gods', '2023-03-17', 125000000, 139, 101, 139),
('Blue Beetle', '2023-08-18', 104000000, 140, 101, 140),
('Pathaan', '2023-01-25', 28000000, 141, 110, 141),
('A Haunting in Venice', '2023-09-15', 7000000, 142, 102, 142),
('Gran Turismo', '2023-08-25', 6000000, 143, 111, 143),
('Haunted Mansion', '2023-07-15', 150000000, 144, 106, 144),
('Saw X', '2023-09-29', 13000000, 145, 106, 145),
('Detective Conan: Black Iron Submarine', '2023-04-14', 100, 146, 100, 146),
('Godzilla Minus One', '2023-12-01', 15000000, 147, 112, 147),
('Poor Things', '2023-09-01', 35000000, 148, 113, 148),
('The Creator', '2023-09-29', 8000000, 149, 102, 149);

INSERT INTO MovieCast VALUES
(1, 100, 1, 'Barbie'),
(1, 101, 1, 'Ken'),
(1, 102, 0, 'Barbie'),
(1, 103, 0, 'Barbie'),
(2, 104, 1, 'Mario'),
(2, 105, 1, 'Princess Peach'),
(2, 106, 1, 'Luigi'),
(2, 107, 1, 'Bowser'),
(3, 108, 1, 'J. Robert Oppenheimer'),
(3, 109, 1, 'Kitty Oppenheimer'),
(3, 110, 1, 'Leslie Groves'),
(3, 111, 1, 'Lewis Strauss'),
(4, 112, 1, 'Star-Lord'),
(4, 113, 0, 'The High Evolutionary'),
(4, 114, 1, "Rocket"),
(4, 115, 1, 'Mantis'),
(5, 116, 1, 'Dominic Toretto'),
(5, 117, 1, 'Michelle Rodriguez'),
(5, 118, 1, 'Shaw');

INSERT INTO ProducingCredit VALUES
(1, 100),
(1, 101),
(1, 102),
(2, 103),
(2, 104),
(3, 105),
(3, 106),
(3, 107),
(4, 108),
(5, 109),
(5, 110),
(5, 111),
(5, 112),
(5, 113);

-- test queries

-- Movie names and net gain
SELECT movie_title, worldwide_total - budget AS Profit
FROM Movie
JOIN SalesRecord
ON Movie.sales_record_id = SalesRecord.sales_record_id
ORDER BY Profit desc;

-- People who are both actors and directors
SELECT * FROM People
WHERE People.person_id IN (SELECT person_id FROM Director)
	AND People.person_id IN (SELECT person_id FROM Actor)
ORDER BY lname, fname;

-- Average income
SELECT AVG(worldwide_total) as "Average Grossing"
FROM SalesRecord;

-- Average movies directed for a director
SELECT AVG(movies_directed) as "Average Movies Per Director"
FROM Director;

-- Average credited roles in a movie
SELECT AVG(actors) as "Average Actors Per Movie"
FROM (SELECT COUNT(actor_id) as actors
	FROM MovieCast
    GROUP BY movie_id) a;
