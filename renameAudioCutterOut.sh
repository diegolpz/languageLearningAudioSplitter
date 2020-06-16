#!/usr/bin/env bash

preName="GlossikaRussian"
# The input is the number of the file whitch helps to off set the output names
for filename in out*; do
    name=$(echo ${filename} | sed -e 's/out\(.*\).mp3/\1/' -)
    # grep -oP "[0-9][0-9]?")
    newname=$((${name} + ($1 - 1) * 50))
    echo ${filename}, ${name}, ${newname}
    mv ${filename} ${preName}${newname}.mp3
done
