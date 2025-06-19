#!/bin/bash

intervall=$1

if [ -z "$intervall" ]; then
    echo "No Intervall given";
    echo "Show Usage once:";
    top -n 10 -stats pid,command,cpu,time,mem -l 2
    exit 1
else
    top -n 10 -stats pid,command,cpu,time,mem -s $intervall
fi