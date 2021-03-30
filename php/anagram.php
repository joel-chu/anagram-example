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

// The $argv will present even the command line include this script
// therefore we need to add a variable from the callee to identify it
if (!defined('IN_SCRIPT') && $argv) {
  // should also check if there is a 1
  if (count($argv) > 1) {
    main($argv[1]);
  } else {
    echo "You need to provide a word";
  }
}
?>
