#!/usr/bin/env bash

# Gets the first two columns of a space-seperated input on STDIN
# Outputs the first two columns on STDOUT

while read line
do
	a="$(echo "$line" | cut -d ' ' -f 1,2)"
	echo "$a"
done < "${1:-/dev/stdin}"
