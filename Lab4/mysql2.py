import mysql.connector
from mysql.connector import Error
def create_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

connection = create_connection("127.0.0.1", "root","Vlad03062005")
print(connection)
def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE IF NOT EXISTS sm_app"
create_database(connection, create_database_query)

def create_connection(host_name, user_name, user_password, db_name):
    connection = None
    try:
        connection = mysql.connector.connect(
        host=host_name,
        user=user_name,
        passwd=user_password,
        database=db_name
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection

def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


use_db = """
USE sm_app
"""
execute_query(connection,use_db)


delete_films = """
DROP TABLE IF EXISTS films;
"""

delete_viewers = """
DROP TABLE IF EXISTS viewers;
"""

delete_cinemas = """
DROP TABLE IF EXISTS cinemas;
"""

delete_comments = """
DROP TABLE IF EXISTS comments;
"""

execute_query(connection, delete_comments)
execute_query(connection, delete_cinemas)
execute_query(connection, delete_viewers)
execute_query(connection, delete_films)

create_films_table = """
CREATE TABLE IF NOT EXISTS films (
id INT AUTO_INCREMENT,
title TEXT NOT NULL,
year INT,
genre TEXT,
country_where_made TEXT,
PRIMARY KEY (id)
) ENGINE = InnoDB
"""
execute_query(connection, create_films_table)


create_viewers_table = """
CREATE TABLE IF NOT EXISTS viewers (
id INT AUTO_INCREMENT,
name TEXT NOT NULL,
gender TEXT NOT NULL,
film_id INT NOT NULL,
score FLOAT NOT NULL,
FOREIGN KEY (film_id) REFERENCES films (id),
PRIMARY KEY (id)
) ENGINE = InnoDB
"""
execute_query(connection, create_viewers_table)

create_cinemas_table = """
CREATE TABLE IF NOT EXISTS cinemas (
id INT AUTO_INCREMENT,
cinema_name TEXT NOT NULL,
film_id INT NOT NULL,
viewer_id INT NOT NULL,
FOREIGN KEY (film_id) REFERENCES films (id), FOREIGN KEY (viewer_id)
REFERENCES viewers (id),
PRIMARY KEY (id)
) ENGINE = InnoDB
"""
execute_query(connection, create_cinemas_table)

create_comments_table = """
CREATE TABLE IF NOT EXISTS comments (
id INT AUTO_INCREMENT,
text TEXT NOT NULL,
film_id INT NOT NULL,
viewer_id INT NOT NULL,
cinema_id INT NOT NULL,
FOREIGN KEY (film_id) REFERENCES films (id), FOREIGN KEY (viewer_id) REFERENCES viewers (id), FOREIGN KEY (cinema_id) REFERENCES cinemas (id),
PRIMARY KEY (id)
) ENGINE = InnoDB
"""
execute_query(connection, create_comments_table)

create_films = """
INSERT INTO
`films` (`title`, `year`, `genre`, `country_where_made`)
VALUES
('Game of Thrones', 2011, 'drama', 'USA,Britain'),
('The Last Kingdom', 2015, 'historical', 'Britain'),
('The Devil Wears Prada', 2006, 'drama', 'USA,France'),
('The Tourist', 2010, 'drama', 'USA,France,Italy'),
('The Intern', 2015, 'drama', 'USA');
"""
execute_query(connection, create_films)

create_viewers = """
INSERT INTO
`viewers` (`name`, `gender`, `film_id`, `score`)
VALUES
("Helen", "female", 2, 9.0),
("Mark", "male", 1, 9.9),
("Gregor Klygan", "the rock", 1, 3.0),
("Gregor Klygan", "the rock", 4, 5.0),
("Mitchell", "male", 4, 7.5),
("Steve", "male", 5, 8.5),
("Laura", "female", 3, 10.0);
"""
execute_query(connection, create_viewers)


create_cinemas = """
INSERT INTO
`cinemas` (`cinema_name`, `film_id`, `viewer_id`)
VALUES
('Cinema 5', 2, 1),
('The Victory', 1, 2),
('Konkord', 1, 3),
('Cinema City', 4, 4),
('Pleasure', 4, 3),
('Pleasure', 3, 7);
"""
execute_query(connection, create_cinemas)


create_comments = """
INSERT INTO
`comments` (`text`, `film_id`, `viewer_id`, `cinema_id`)
VALUES
('IM IN LOVE WITH DENY', 1, 6, 2),
('Uhtred is a real man', 2, 4, 1),
('Everybody knows that Im the strongest', 1, 3, 3),
('Jonny is sooo charming', 4, 1, 5),
('Ann Hathaway is beautiful as always', 3, 5, 4);
"""
execute_query(connection, create_comments)


add_film = """
INSERT INTO 
`films` (`title`, `year`, `genre`, `country_where_made`)
VALUES
('The Professor', 2018, 'comedy', 'USA');
"""
execute_query(connection, add_film)

add_viewer = """
INSERT INTO
`viewers` (`name`, `gender`, `film_id`, `score`)
VALUES
('Nick', 'male' , 6, 7.2);
"""
execute_query(connection, add_viewer)

add_comment = """
INSERT INTO
`comments` (`text`, `film_id`, `viewer_id`, `cinema_id`)
VALUES
('WHY HE KILLS HER' , 1, 6, 2);
"""
execute_query(connection, add_comment)

add_cinema = """
INSERT INTO
`cinemas` (`cinema_name`, `film_id`, `viewer_id`)
VALUES
('Turan', 6, 3);
"""
execute_query(connection, add_cinema)

print()
select_films = "SELECT * from films"
films = execute_read_query(connection, select_films)
for film in films:
    print(film)


print()
select_viewers = "SELECT * from viewers"
viewers = execute_read_query(connection, select_viewers)
for viewer in viewers:
    print(viewer)
print()
select_comments = "SELECT * from comments"
comments = execute_read_query(connection, select_comments)
for comment in comments:
    print(comment)
print()
select_cinemas = "SELECT * from cinemas"
cinemas = execute_read_query(connection, select_cinemas)
for cinema in cinemas:
    print(cinema)
print()
select_films_and_viewers = """
SELECT `films`.`title`, `films`.`genre`, `viewers`.`name`, `viewers`.`score` 
FROM `films`
INNER JOIN `viewers`
ON `films`.`id` = `viewers`.`film_id`;
"""
films_and_viewers = execute_read_query(connection, select_films_and_viewers)
for f in films_and_viewers:
    print(f)
print()

the_highest_score = """
SELECT `cinema_name` as `Organization`, 
MAX(`viewers`.`score`) as `Score` 
FROM 
`viewers`,
`cinemas`
WHERE
`viewers`.`id` = `cinemas`.`viewer_id`
GROUP BY `viewers`.`id`, `Organization`, `Score`;
"""
highest_score = execute_read_query(connection, the_highest_score)
for h in highest_score:
    print(h)
print('dfdg')

the_latest_film = """
SELECT `title`, `genre`, `year`
FROM `films`
WHERE `year` = (
SELECT MAX(`year`) FROM `films`
);
"""
latest_film = execute_read_query(connection, the_latest_film)
for l in latest_film:
    print(l)
print()
first_union = """
SELECT `name` AS `Name`, `score` AS `Score`
FROM `viewers`
UNION
SELECT `gender` AS `Name`,score AS `Score`
FROM `viewers`
WHERE `score` = (
SELECT MAX(`score`) FROM `viewers`
)
UNION
SELECT `gender` AS `Name`,`score` AS `Score`
FROM `viewers`
WHERE `score` = (
SELECT MIN(`score`) FROM `viewers`
) ORDER BY `Score`;
"""
fr_un  =execute_read_query(connection, first_union)
for f in fr_un:
    print(f)
print()
second_union = """
SELECT `films`.`title` AS `Name`, `viewers`.`score` AS `Score`
FROM `viewers`
INNER JOIN `films`
ON `films`.`id` = `viewers`.`film_id`
UNION
SELECT `films`.`title` AS `Name`,`viewers`.`score` AS `Score`
FROM `viewers`
INNER JOIN `films`
ON `films`.`id` = `viewers`.`film_id`
WHERE `viewers`.`score` = (
SELECT MAX(`score`) FROM `viewers`
)
UNION
SELECT `films`.`title` AS `Name`,`viewers`.`score` AS `Score`
FROM `viewers`
INNER JOIN `films`
ON `films`.`id` = `viewers`.`film_id`
WHERE `viewers`.`score` = (
SELECT MIN(`score`) FROM `viewers`
) ORDER BY `Score`;
"""
fr_un  =execute_read_query(connection, second_union)
for f in fr_un:
    print(f)
print()
dist = """
SELECT DISTINCT `name`
FROM `viewers`
"""
dis =  execute_read_query(connection,dist)
for d in dis:
    print(*d)
print()

update_films_description = """
UPDATE
films
SET
country_where_made = "USA,France,Italy,Britain"
WHERE
id = 4
"""
execute_query(connection, update_films_description)

update_viewers_description = """
UPDATE
viewers
SET
score = 4.3
WHERE
id = 3
"""
execute_query(connection, update_viewers_description)

set = "SET FOREIGN_KEY_CHECKS=0;"
execute_query(connection,set)

delete_comment = "DELETE FROM `comments` WHERE `id` = 1"
execute_query(connection, delete_comment)

delete_cinema = "DELETE FROM `cinemas` WHERE `id` = 5"
execute_query(connection, delete_cinema)

delete_viewer = "DELETE FROM `viewers` WHERE `id` = 4"
execute_query(connection, delete_viewer)

delete_film = "DELETE FROM `films` WHERE `id` = 1"
execute_query(connection, delete_film)

set = "SET FOREIGN_KEY_CHECKS=1;"
execute_query(connection,set)

delete_comments = """
DROP TABLE IF EXISTS comments;
"""
execute_query(connection,delete_comments)