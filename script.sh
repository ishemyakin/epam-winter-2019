#!/bin/bash

function show_usage {
	echo "Использование: $0 $source_dir $dest_dir"
	exit 1
}
# Основная программа начинается здесь

if [ $# -ne 2 ]; then 
	show_usage
else
	if [ -d $1 ]; then 
		source_dir=$1
	else
		echo 'Недопустимый комментарий'
		show_usage
	fi
	if [ -d $2 ]; then
		dest_dir=$2
	else
		echo 'Недопустимый каталог'
		show_usage
	fi
fi

printf "Каталог-источник: ${source_dir}\n"
printf "Каталог-источник: ${dest_dir}\n"
