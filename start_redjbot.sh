#!/bin/sh
while [ true ]
do
        echo "Starting up server..."
        python redjbot.py
        echo "Bot has shut down. Will restart in 2 seconds (use CTRL-C to cancel)"
        sleep 2
done
