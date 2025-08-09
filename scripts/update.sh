#! /bin/bash

set -e

docker compose down
docker compose pull
docker compose build
docker compose up -d