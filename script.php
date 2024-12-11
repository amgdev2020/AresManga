<?php


$type = $_GET['type'];
$input = $_GET['input'];
switch($type){
    case 'search':
        $command = escapeshellcmd('AresManaga/search.py -u ' . $input);
        $output = shell_exec($command);
        echo $output;
        break;
    case 'home': 
        $command = escapeshellcmd('AresManaga/home.py');
        $output = shell_exec($command);
        echo $output;
        break;
    case 'manga': 
        $command = escapeshellcmd('AresManaga/manga.py -u ' . $input);
        $output = shell_exec($command);
        echo $output;
        break;
    case 'last_updates': 
        $command = escapeshellcmd('AresManaga/last_update.py');
        $output = shell_exec($command);
        echo $output;
        break;
    case 'series': 
        $command = escapeshellcmd('AresManaga/series.py');
        $output = shell_exec($command);
        echo $output;
        break;
    case 'chapters': 
        $command = escapeshellcmd('AresManaga/chapters.py -u ' . $input);
        $output = shell_exec($command);
        echo $output;
        break;
    case 'home_page': 
        $command = escapeshellcmd('AresManaga/home_page.py -u ' . $input);
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
