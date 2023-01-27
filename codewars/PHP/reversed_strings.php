<?php 
/*
    Write a funtion to reverse the string given
*/

function reverse_string($str) {
    echo "Original: ".$str;
    echo "\nReversed: ".strrev($str);
}

$text = readline("Enter your text: ");
reverse_string($text);
?>