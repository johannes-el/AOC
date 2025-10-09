#!/usr/bin/bash

mkdir -p ./src/bin

for i in {1..24}
do
    if [ $i -lt 10 ]; then
        touch ./src/bin/day0$i.rs
    else
        touch ./src/bin/day$i.rs
    fi
done

