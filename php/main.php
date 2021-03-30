#!/usr/bin/env php
<?php
define('IN_SCRIPT', true);
require('anagram.php');

// wrapper for interactive version
function run() {
  echo("Please provide a word: ");
  $input = strtolower(trim(fgets(STDIN)));
  main($input);
}

run();

?>
