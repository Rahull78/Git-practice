<?php
$no=$_POST["n1"];
$fact=1;
while($no>0)
{
	$fact=$fact*$no;
	$no--;
}
echo"Factorial is :  $fact";
?>