#!/usr/bin/env bash

for filename in *C.mp3; do
    name=$(echo ${filename} | grep -oP "[0-9][0-9]")
    mv ${filename} ${name}.mp3
done
