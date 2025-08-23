import json
import os
import random
import sys

import logging
import paho.mqtt.client as mqtt

# Set up the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout)],
)
LOGGER = logging.getLogger("pseudo-sensor")

# Setup MQTT Variables
TRIGGER_TOPIC = "sensors/trigger"
TOPIC = "sensors/temp"
SENSOR_ID = "pseudo-sensor"
HOST = str(os.getenv("MQTT_HOST"))
PORT = int(os.getenv("MQTT_PORT"))
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")


def on_connect(client, userdata, flags, rc, props) -> None:
    LOGGER.info("Connected with result code: %s", str(rc))
    if rc != 0:
        return
    LOGGER.info("Subscribing to topic: %s", TRIGGER_TOPIC)
    client.subscribe(TRIGGER_TOPIC)


def on_message(client, userdata, msg) -> None:
    topic = msg.topic
    LOGGER.info("Received trigger signal. Topic: %s", topic)

    temp = random.uniform(10.0, 40.0)
    humidity = random.uniform(10.0, 40.0)
    pressure = random.uniform(10.0, 40.0)

    data = {
        "device_id": SENSOR_ID,
        "readings": [
            {"name": "temperature", "value": temp},
            {"name": "humidity", "value": humidity},
            {"name": "pressure", "value": pressure},
        ],
    }

    payload = json.dumps(data)
    client.publish(topic=TOPIC, payload=payload)
    LOGGER.info("Published reading: %s", payload)


def main() -> None:
    """Main function to setup the pseudo sensor"""
    client = mqtt.Client(
        client_id="pseudo-mqtt-sensor",
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    )
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username=USERNAME, password=PASSWORD)
    client.connect(host=HOST, port=PORT, keepalive=60)
    client.loop_forever()


if __name__ == "__main__":
    main()
