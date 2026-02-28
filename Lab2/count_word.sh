#!/bin/bash

if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <filename> <word>"
  exit 1
fi

file="$1"
word="$2"

if [ ! -f "$file" ]; then
  echo "Error: File not found."
  exit 1
fi

count=$(grep -o "$word" "$file" | wc -l | tr -d ' ')
echo "The word '$word' appears $count times in '$file'."
