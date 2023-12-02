<?php
$db_host = 'localhost';
$db_user = 'root';
$db_password = 'root';
 
$connection = @new mysqli(
$db_host,
$db_user,
$db_password
);
	
if ($connection->connect_error) {
    echo 'Errno: '.$connection->connect_errno;
    echo '<br>';
    echo 'Error: '.$connection->connect_error;
    exit();
}

$create_use = mysqli_query($connection,"GRANT ALL PRIVILEGES ON *.* TO 'daddy'@'localhost'
IDENTIFIED BY 'daddy'
WITH GRANT OPTION");
if ($create_use) {
    echo "Creating success<br>";
} else {
    echo "Creating failed<br>";
}
?>