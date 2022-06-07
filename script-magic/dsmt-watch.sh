#!/bin/bash
while true
do
	echo MEMORY USAGE:
	dsmt mem 10
	echo
	echo CPU USAGE:
	dsmt cpu 10
	echo; echo
	sleep 1
	clear
done
