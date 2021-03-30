<?php
// this is different from all the other languages so far
chdir(dirname(__FILE__));
// we lock it at 7 but here we want to try more letters
define('MAX_ALLOW', 15);

require("mylib.php");

/**
 * The main method to get the anagram
 *
 */
function anagram($str, $maxChar) {
  $l = strlen($str);

  $jsonData = $GLOBALS['jsonData'] ? $GLOBALS['jsonData'] : getJsonData();

  $max = $maxChar === true ? MAX_ALLOW : $jsonData["MAX_CHAR"];
  $min = $jsonData["MIN_CHAR"];

  var_dump($max);

  if ($l > $max || $l < $min) {
    echo "Error: please proide a word between $min and $max\n";
  } else {
    $words = getWords($l, $jsonData);

    return getAnagram($str, $words);
  }
}


/**
 * The main method for the command line interface
 *
 */
function main($word, $max = false) {
  $startTime = microtime(true);
  $result = anagram($word, $max);
  if ($result && $result[0]) { // V1.5 return an array 0.result 1.tried 2.i
    $endTime = microtime(true) - $startTime;

    echo "We found an anagram for $word >> $result[0]. After $result[1]($result[2]) try in $endTime";
  } else {
    echo "Sorry could not find anything";
  }
  echo "\n";
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
