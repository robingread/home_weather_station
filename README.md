# Readme

## Setup Steps

### Setup InfluxDB

- create `.env` file
- setup influxdb by going to the web UI, adding a username/password, org and bucket
- Add InfluxDB API token to the `.env` file.

### Setup Mosquitto

- create `mosquitto/config/passwd` file
- start mqtt-broker service
- execute password setup (see below)

### Setup Grafana

- connect to web UI (e.g., <http://localhost:3000>), login with admin/admin
- change password
- change username

## InfluxDB

Pull the latest [InfluxDB Docker](https://hub.docker.com/_/influxdb) image:

```bash
docker pull influxdb:2.7
```

```bash
docker run --rm influxdb:2.7. influxd print-config > config.yaml
```

```bash
docker run --name influxdb -d \
-p 8086:8086 \
--volume `pwd`/influxdb2:/var/lib/influxdb2 \
--volume `pwd`/config.yaml:/etc/influxdb2/config.yaml \
influxdb:2.7
```

## Mosquito Setup

Create a password file (`mqtt_config/passwd`) and mounting it in the container, and run the following to add a password for a given user:

```bash
touch mosquitto/config/passwd
sudo chmod 0700 mosquitto/config/passwd
```

```bash
docker exec -it <container_name> mosquitto_passwd -c /mosquitto/config/passwd <username>
```

```bash
chown root mosquitto/config/passwd
``````

## `.env` File

The following variables should be set in a `.env` file:

| Name | Description |
|--|--|
| `INFLUXDB_HOST` | Hostname of the InfluxDB service.
| `INFLUXDB_PORT` | Port to connect to for the InfluxDB database.
| `INFLUXDB_TOKEN` | Access token for the InfluxDB database.

## Speed up SSH Access to the Pi over WiFi

```bash
sudo pico /etc/ssh/sshd_config

# Add this line
IPQoS 0x00
```

## Docker Images

[Eclipse Mosquito MQTT Broker](https://hub.docker.com/_/eclipse-mosquitto)
[InfluxDB Database](https://hub.docker.com/_/influxdb)
[Grafana Visualisation](https://hub.docker.com/r/grafana/grafana)

## Useful links

Some bullshit to setup the Grafana connection, but this issue outlines it very well: <https://github.com/grafana/grafana/issues/32252>
Increasing SWAP memory on a Raspberry Pi: <https://pimylifeup.com/raspberry-pi-swap-file/>
