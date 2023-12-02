<?php
$db_host = 'localhost';
$db_user = 'root';
$db_password = 'root';
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

$note_id = $_GET['note'];
$comm = mysqli_query($connection,"SELECT `created`,`title`,`article` FROM notes WHERE `id` = $note_id;");
if ($comm){
    while ($com = mysqli_fetch_array($comm)){
        echo "Created: ".$com['created']."<br>";
        echo "Title: ".$com['title']."<br>";
        echo "Article: ".$com['article']."<br>";
    }
} else{
    echo "Error selecting<br>";
}
$sel_comm = mysqli_query($connection,"SELECT * FROM comments WHERE art_id = $note_id");
if ($sel_comm){
    $nom = 0;
    while ($i = mysqli_fetch_array($sel_comm)) { 
        echo "Reply:<br>";
        echo "Created: ".$i['created']."<br>";
        echo "Author: ".$i['author']."<br>";
        echo "Comment: ".$i['comment']."<br>";
        $nom++;
    }
    if ($nom == 0) {
        echo "Эту запись еще никто не комментировал";
    }
} else{
    echo "Error selecting<br>";
}

?>