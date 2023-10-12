#!/bin/bash

# Získání argumentů z uživatele
read -p "Zadejte alias klíče: " alias

# Spuštění Python skriptu s argumenty
python3 genereate_ssh_keys.py "$alias"

# Kontrola návratové hodnoty z Python skriptu
if [ $? -eq 0 ]; then
    echo "Skript úspěšně dokončen."
else
    echo "Skript selhal."
fi
