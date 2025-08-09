# Readme

| Service | Description | Web Interface |
|---|---|---|
| InfluxDB | ??? | [`localhost:8086`](http://localhost:8086) |
| Grafana | ??? | [`localhost:3001`](http://localhost:3001) |
| MQTT Inspector | ??? | [`localhost:3002`](http://localhost:3002) |
| Prometheus | ??? | [`localhost:3003`](http://localhost:3003) |

## Setup Steps

### Setup the `.env` file

Create a new `.env` file using the `.env.example`:

```bash
cp .env.example .env
```

### Setup InfluxDB

Start up the `influxdb` service:

```bash
docker compose up influxdb
```

Then open the Web interface at [`localhost:8086`](http://localhost:8086) to create a user and password. Set the Organization to `Home` and the Bucket to `Test Measurements`. When that is done, there will be an access token displayed. This needs to be assigned to the `INFLUXDB_TOKEN` in the `.env` file. You can then stop the docker service.

### Setup Mosquitto MQTT

First, create a password file:

```bash
touch mosquitto/config/passwd
sudo chmod 0700 mosquitto/config/passwd
```

Then start the `mqtt-broker` service:

```bash
docker compose up mqtt-broker
```

To set the username and password, run the following in a separate terminal:

```bash
docker exec -it <container_name> mosquitto_passwd -c /mosquitto/config/passwd <username>
```

Assign the username and password credentials to the `.env` file in the `MQTT_USERNAME` and `MQTT_PASSWORD` variables.

Finally, follow the instruction to change the ownership of the password file:

```bash
sudo chown root mosquitto/config/passwd
```

You can then stop the docker service.

### Setup Grafana

Then start the `grafana` service:

```bash
docker compose up grafana
```

You can then connect to web UI (e.g., <http://localhost:3001>), login with `admin`/`admin`. You will then be prompted to update the password for the `admin` user.

You can then stop the service.

## Setup for running on a Raspberry PI

### Speed up SSH Access to the Pi over WiFi

```bash
sudo pico /etc/ssh/sshd_config
```

Then add this line:

```
IPQoS 0x00
```

## References

### Docker Images

- [Eclipse Mosquito MQTT Broker](https://hub.docker.com/_/eclipse-mosquitto)
- [InfluxDB Database](https://hub.docker.com/_/influxdb)
- [Grafana Visualisation](https://hub.docker.com/r/grafana/grafana)

### Useful links

Some bullshit to setup the Grafana connection, but this issue outlines it very well: <https://github.com/grafana/grafana/issues/32252>
Increasing SWAP memory on a Raspberry Pi: <https://pimylifeup.com/raspberry-pi-swap-file/>
