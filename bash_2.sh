#!/bin/bash
#wetter="$(curl -s wttr.in/Berlin?0?Q | grep °C)"
wetter="$(curl "https://api.brightsky.dev/current_weather?lat=52.44&lon=13.40")"
echo "${wetter}"

if [[ "$wetter" =~ "temperature:"([0-9]+)$ ]]; then
  fruit="${BASH_REMATCH[1]}"
  number="${BASH_REMATCH[2]}"
  echo "Fruit: $fruit"
#echo "${wetter//[^0-9.]/}"

#$degrees=$wetter 
