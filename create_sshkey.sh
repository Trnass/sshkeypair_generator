#!/bin/bash

read -p "Alias: " alias

python3 genereate_ssh_keys.py "$alias"

if [ $? -eq 0 ]; then
    echo "Done."
else
    echo "Crashed."
fi
