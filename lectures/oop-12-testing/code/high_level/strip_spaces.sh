#!/usr/bin/env bash

# Reads data from STDIN, and strips repeated spaces
# Outputs the stdin data with spaces removed to STDOUT

while read line
do
	a="$(echo "$line" | sed -r 's/ +/ /g')"
	echo "$a"
done < "${1:-/dev/stdin}"
