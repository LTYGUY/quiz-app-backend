#!/bin/bash

while getopts n: flag
do
    case $flag in
        n) app_name=$OPTARG
    esac
done

if [ $OPTIND -eq 1 ]
then
    app_name=emanon
    echo "No flags were set, defaulting to app_name: $app_name"
fi

# Clear the port before beginning
sh ./clearport.sh

# Delete previous Docker image if any
docker stop $app_name
docker rm $app_name

# Build Docker image
docker build -t $app_name .

# Run Docker image
docker run --name $app_name $app_name
