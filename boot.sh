#!/bin/bash

echo "Would you like to play rock, paper, scissors? (yes/no)"
read answer

if [ "$answer" = "yes" ]; then
    python3 rock_paper_scis.py
else
    echo "That is too bad, maybe next time."
fi