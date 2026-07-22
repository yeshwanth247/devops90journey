#!/bin/bash

read number
echo "the $number table: "
for i in $(seq 1 10)
do
  multi=$((number * i))
  echo "$number x $i = $multi "
done

