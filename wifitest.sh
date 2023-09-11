#!/bin/bash

result=$(/home/ubuntu/.local/bin/speedtest-cli)

filtered_result=$(echo "$result" | grep "Mbit/s")

values=$(echo "$filtered_result" | awk -F' ' '{print $2}' | paste -sd ",")

echo "$values"

mosquitto_pub -h "test.mosquitto.org" -p 1883 -t "measurements" -m "$values"





