#! /bin/bash

set -e

sudo rm -rf ./influxdb/data
sudo rm -rf ./mosquitto/config/passwd
sudo rm -rf ./grafana/data/*
sudo rm -rf ./prometheus/data/*