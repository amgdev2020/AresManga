<?php


$type = $_GET['type'];
$input = $_GET['input'];
switch($type){
    case 'search':
        $command = escapeshellcmd('search.py -u ' . $input);
        $output = shell_exec($command);
        echo $output;
        break;
    case 'home': 
        $command = escapeshellcmd('home.py');
        $output = shell_exec($command);
        echo $output;
        break;
    case 'manga': 
        $command = escapeshellcmd('manga.py -u ' . $input);
        $output = shell_exec($command);
        echo $output;
        break;
    case 'last_updates': 
        $command = escapeshellcmd('last_update.py');
        $output = shell_exec($command);
        echo $output;
        break;
    case 'series': 
        $command = escapeshellcmd('series.py');
        $output = shell_exec($command);
        echo $output;
        break;
    case 'chapters': 
        $command = escapeshellcmd('chapters.py -u ' . $input);
        $output = shell_exec($command);
        echo $output;
        break;
    case 'home_page': 
        $command = escapeshellcmd('home_page.py -u ' . $input);
        $output = shell_exec($command);
        echo $output;
        break;
    default:
        echo 'INVALID TYPE';
}
/*
$command = escapeshellcmd($file);
$output = shell_exec($command);
echo $output;
*/
?>
