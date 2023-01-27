<?php
/*
    Write a function to remove the spaces from the string given
*/

function no_space(String $s): String {
    return str_replace(" ", "", $s);
}

$str = readline("Enter a string: ");
print(no_space($str));
?>