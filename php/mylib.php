<?php

// this is very different behavior
chdir( dirname ( __FILE__ ) );
$workDir = "../share";
$jsonConfigFile = "$workDir/config.json";
$jsonData = json_decode(file_get_contents($jsonConfigFile),true);

/**
 * import the text file and turn into an array for use later
 * We add the $jsonData as parameter here becasue it might not be available
 * by the time it gets call
 */
function getWords($dir, $name, $jsonData) {
  $filename = join($jsonData["DOT"], array($name, $jsonData['FILE_EXT']));
  $filepath = "$dir/$filename";
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
 * The main method to get the Anagram
 *
 */
function getAnagram($str, $words) {
  if (!in_array($str, $words)) {
    return false;
  }
  $dict = array_filter($words, function($w) {
    return $w != $str;
  });
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

?>
