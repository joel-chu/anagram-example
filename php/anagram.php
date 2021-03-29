<?php
chdir( dirname ( __FILE__ ) );
require "./mylib.php";

/**
 * The main method to get the anagram
 *
 */
function anagram($str) {
  $l = strlen($str);
  $max = $jsonData["MAX_CHAR"];
  $min = $jsonData["MIN_CHAR"];

  if ($l > $max || $l < $min) {
    echo "Error: please proide a word between $min and $max";
  } else {
    $words = getWords();

    return getAnagram($str, $words);
  }
}


/**
 * The main method for the command line interface
 *
 */
function main($word) {
  $result = anagram($word);
  if ($result) {
    echo "We found an anagram for $word > $result";
  } else {
    echo "Sorry could not find anything";
  }
}

// @TODO how can we tell if it's calling from command line

var_dump($jsonData);

?>
