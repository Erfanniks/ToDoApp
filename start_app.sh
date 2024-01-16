#!/bin/bash

# Check if the network exists, if not create it
NETWORK_NAME="mynetwork"
if [ -z "$(docker network ls --filter name=^${NETWORK_NAME}$ --format="{{ .Name }}")" ] ; then
  echo "Creating Docker network: $NETWORK_NAME"
  docker network create $NETWORK_NAME
fi

# Create and start the PostgreSQL container
docker volume create --name db_volume
docker run -d --name postgres --network $NETWORK_NAME \
       -p 5432:5432 \
       --env-file database.conf \
       -v db_volume:/var/lib/postgresql postgres:latest

# Build and start Flask app container
docker build -t flask-app-image .
docker run -d --name flask-app --network $NETWORK_NAME \
       -p 5000:5000 \
       -e FLASK_APP=src/run.py \
       -e DB_USER=postgres \
       -e DB_PASSWORD=postgres \
       -e DB_NAME=todolistdb \
       -e DB_HOST=postgres \
       -e DB_PORT=5432 \
       flask-app-image

# Wait for the containers to initialize completely
echo "Waiting for the containers to initialize..."
sleep 10

# Show logs from the Flask container
docker logs flask-app
