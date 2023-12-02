<?php
$db_host = 'localhost';
$db_user = 'daddy';
$db_password = 'daddy';
$db = "MySiteDB";

$connection = @new mysqli(
$db_host,
$db_user,
$db_password,
$db
);

if ($connection->connect_error) {
echo 'Errno: '.$connection->connect_errno;
echo '<br>';
echo 'Error: '.$connection->connect_error;
exit();
}

$create_notes = "CREATE TABLE IF NOT EXISTS notes(
id INT NOT NULL AUTO_INCREMENT, 
PRIMARY KEY (id),
created DATE,
title VARCHAR(20),
article VARCHAR(225),
UNIQUE(created,title,article)
)";

$create_tbl = mysqli_query($connection, $create_notes);
if ($create_tbl) {
    echo "Create notes success"."<br>";
} else {
    echo "Cant create notes"."<br>";
}


$create_comms = "CREATE TABLE IF NOT EXISTS comments(
id INT NOT NULL AUTO_INCREMENT, 
PRIMARY KEY (id),
created DATE,
author VARCHAR(20),
comment VARCHAR(225),
art_id INTEGER,
UNIQUE(created,author,comment)
)";

$create_tbl = mysqli_query($connection, $create_comms);
if ($create_tbl) {
    echo "Create comms success"."<br>";
} else {
    echo "Create comms failed"."<br>";
}


$ins = mysqli_query($connection, "INSERT IGNORE INTO `notes` (`created`,`title`, `article`)
VALUES
('10-01-20','Programmer', 'Use C++ bro'),
('12-10-19','Money','Gazprom is very good paper to buy'),
('16-08-12','Star Wars', 'Hey guys, Darth Vader or Obi-van?'),
('22-01-11','Hu?p?p', 'Uga bunga yup yup'),
('23-02-23','Travel', 'Where shoud I go to te weekends?');");

if ($ins) {
    echo "Success"."<br>";
} else {
    echo "Error"."<br>";
}


$ins = mysqli_query($connection, "INSERT IGNORE INTO `comments` (`created`,`author`, `comment`,`art_id`)
VALUES
('10-01-21','Mike Tyson', 'Only Assembler only hardcore',1),
('19-10-19','Baffet','I dont think so..',2),
('20-08-12','Anakin Skywalker', 'definitely Darth Vader',3),
('22-03-11','Ben Kenobi', 'Obi-van is so cool',3),
('23-07-23','Vladimir Putin', 'I prefer taiga',5);");

if ($ins) {
    echo "Success"."<br>";
} else {
    echo "Error"."<br>";
}

?>