<?php
header("Content-Type: text/html; charset=UTF-8");
$a = 10;
$b = 20;
echo "a = $a<br>";
echo "b = $b<br>";
$c = $a + $b;
echo "c = $c<br>";
$c = $c*3;
echo "c = $c<br>";
$c = $c/($b-$a);
echo "c = $c<br>";
$p = "Программа";
$b = "работает";
$result = $p." ".$b;
echo $result."<br>";
$result.= " хорошо";
echo $result."<br>";
$q = 5;
$w = 7;
$q = $q + $w;
$w = $q - $w;
$q = $q - $w;
echo "q = $q<br>";
echo "w = $w<br>";
for ($i = 23; $i <=78;$i++){
    echo $i."<br>";
}
echo "<ul>";
echo "<li>"."First"."</li>"; 
echo "<li>"."Second"."</li>";
echo "<li>"."Third"."</li>";
echo "<li>"."Forth"."</li>";
echo "<li>"."Fifth"."</li>";
echo "<li>"."Sixth"."</li>";
echo "<li>"."Seventh"."</li>";
echo "<li>"."Eighth"."</li>";
echo "<li>"."Nineth"."</li>";
echo "<li>"."Tenth"."</li>";
echo "</ul>";

$vector = array();
for ($i = 0;$i <100;$i++){
    $vector[] = rand();
}
$i=0;
while ($i<100){
    echo $vector[$i]."<br>";
    $i++;
}
echo "_________________________<br>";
foreach ($vector as $key => $val) {
	echo $val . '<br>';
}
switch (date('N')){
    case 1:
        echo "Понедельник<br>";
        break;
    case 2:
        echo "Вторник<br>";
        break;
    case 3:
        echo "Среда<br>";
        break;
    case 4:
        echo "Четверг<br>";
        break;
    case 5:
        echo "Пятница<br>";
        break;
    case 6:
        echo "Суббота<br>";
        break;
    case 7:
        echo "Воскресенье<br>";
        break; 
}

function getPlus10($a){
    return $a+10;
}
echo getPlus10(15);
?>