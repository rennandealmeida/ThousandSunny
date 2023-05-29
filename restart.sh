#!/bin/bash

docker-compose -f docker-compose.yaml down
#docker-compose -f docker-compose.yaml up -d --force-recreate --build
docker-compose -f docker-compose.yaml up -d --build