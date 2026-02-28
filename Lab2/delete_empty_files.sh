#!/bin/bash

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <directory>"
  exit 1
fi

dir="$1"

if [ ! -d "$dir" ]; then
  echo "Error: Directory not found."
  exit 1
fi

find "$dir" -type f -empty -print -delete
