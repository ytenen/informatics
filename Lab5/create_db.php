<?php
# FileName="Connection_php_mysql.htm"
# Type="MYSQL"
# HTTP="true"

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

echo 'Success: A proper connection to MySQL was made.';
echo '<br>';
echo 'Host information: '.$connection->host_info;
echo '<br>';
echo 'Protocol version: '.$connection->protocol_version;
echo '<br>';

$create_db = "CREATE DATABASE IF NOT EXISTS MySiteDB";
if ($connection->query($create_db)) {
    echo "Create successful";
} else {
    echo "Error ".$connection->error;
}
echo "<br>";

$create_db = "CREATE DATABASE IF NOT EXISTS MySiteDB";
if ($connection->query($create_db)) {
    echo "Create successful";
} else {
    echo "Error ".$connection->error;
}
echo "<br>";

mysqli_query($connection, "SET NAMES cp1251;");
mysqli_query($connection, "SET CHARACTER SET cp1251;");


$db = "MySiteDB";
$select = mysqli_select_db($connection, $db);
if ($select){
    echo "Succcess pick"."<br>";
} else {
    echo "Cant pick"."<br>";
}
?>