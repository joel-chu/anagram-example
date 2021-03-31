#!/usr/bin/env php
<?php
define('IN_SCRIPT', true);
require('anagram.php');

// wrapper for interactive version
function run() {
  echo("Please provide a word: ");
  $input = strtolower(trim(fgets(STDIN)));

  $test = explode(" ", $input);
  if (count($test) > 1 && $test[1] === '--max') {
    main($test[0], true);
  } else {
    main($input);
  }
}

run();

?>
