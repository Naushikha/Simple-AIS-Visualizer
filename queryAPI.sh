#!/bin/bash

API_KEY="PASTE HERE"

# There's a limit to querying the API as 2 mins. So we query every 2 min to max out AMAP
while :
do
    myDate="$(date +"%Y_%m_%d_%H_%_M_%S")"
    curl "https://services.marinetraffic.com/api/exportvessels/${API_KEY}?v=1&timespan=2&msgtype=simple&protocol=jsono" > "${myDate}.json"
    echo "${myDate}"
    sleep 2m
done
