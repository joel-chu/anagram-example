<?php

// this is very different behavior
chdir( dirname ( __FILE__ ) );

define('WORK_DIR', '../share');
// put a placeholder here first
global $jsonData;

/**
 * Wrap the get json in one method
 * because when we call it like this, the $jsonData is missing sometime
 * due to the blocking nature of PHP
 */
function getJsonData() {
  $jsonConfigFile = WORK_DIR . "/config.json";
  return json_decode(file_get_contents($jsonConfigFile),true);
}

/**
 * import the text file and turn into an array for use later
 * We add the $jsonData as parameter here becasue it might not be available
 * by the time it gets call
 */
function getWords($name, $jsonData) {
  $filename = join($jsonData["DOT"], array($name, $jsonData['FILE_EXT']));
  $filepath = WORK_DIR . "/$filename";
  $fileContent = trim(file_get_contents($filepath));

  return explode(" ", $fileContent);
}

/**
 * get the total combination number - maximum try
 *
 */
function getMaxTryNum($n, $total = 0) {
  if ($n == 1) {
    return $total;
  }
  if ($total == 0) {
    $total = $n;
  }
  $n -= 1;
  $total *= $n;
  return getMaxTryNum($n, $total);
}


/**
 * find a combination which not already tried
 *
 */
function getPossibleWord($str, $triedWords) {
  $possibleWord = str_shuffle($str);
  if (in_array($possibleWord, $triedWords)) {
    return getPossibleWord($str, $triedWords);
  }
  return $possibleWord;
}

/**
 * I could never guess a simple array_filter create such a problem
 * 1. Using anonymous function, it couldn't access the variable outside which is $str for comparison
 * 2. Using expression - there is no way to pass a parameter to such function when array_filter calls the function
 *    which is a string (then PHP finds it for you if any)
 * Therefore need to create a closure method like this one
 * based on this https://stackoverflow.com/questions/5482989/php-array-filter-with-arguments/5483102#5483102 discussion
 */
function createFilterFn($str) {
  return function($w) use($str) {
    return $w != $str;
  }; // <-- this is important!
}


/**
 * The main method to get the Anagram
 *
 */
function getAnagram($str, $words) {
  if (!in_array($str, $words)) {
    return false;
  }
  // Throw a strange error said $str is undefined
  // if I use an anonymous function
  $filterFn = createFilterFn($str);

  $dict = array_filter($words, $filterFn);

  $maxTried = getMaxTryNum(strlen($str));
  $tried = 0;
  $possibleWords = array();

  while ($tried <= $maxTried) {
    $word = getPossibleWord($str, $possibleWords);
    if (in_array($word, $dict)) {
      return $word;
    }
    array_push($possibleWords, $word);
    ++$tried;
  }
  return false;
}

// pretty crappy way
if (!$jsonData) {
  $jsonData = getJsonData();
}

?>
