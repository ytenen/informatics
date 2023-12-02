<?php
$db_host = 'localhost';
$db_user = 'root';
$db_password = 'root';
$db_name = 'MySiteDB';
 
$connection = mysqli_connect(
$db_host,
$db_user,
$db_password,
$db_name
);
	
if ($connection->connect_error) {
    echo 'Errno: '.$connection->connect_errno;
    echo '<br>';
    echo 'Error: '.$connection->connect_error;
    exit();
}


$sel = mysqli_query( $connection,'SELECT * FROM `notes`');
while ($note = mysqli_fetch_array($sel)) {
    echo $note ['id'], "<br>";
    ?>
    <a href="comments.php?note=<?php echo $note['id'];?>">
    <?php echo $note ['title'], "<br>";?></a>
    <?php
	echo $note ['created'], "<br>";
	echo $note ['article'], "<br>";
}

?>