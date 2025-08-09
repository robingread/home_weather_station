import json
import os
import random

import paho.mqtt.client as mqtt

TRIGGER_TOPIC = "sensors/trigger"
TOPIC = "sensors/temp"
SENSOR_ID = "pseudo-sensor"
HOST = str(os.getenv("MQTT_HOST"))
PORT = int(os.getenv("MQTT_PORT"))
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")


def on_connect(client, userdata, flags, rc, props) -> None:
    print("Connected with result code " + str(rc), flush=True)
    if rc != 0:
        return
    print(f"Subscribing to topic: {TRIGGER_TOPIC}")
    client.subscribe(TRIGGER_TOPIC)


def on_message(client, userdata, msg) -> None:
    print(msg.topic + " " + str(msg.payload.decode()), flush=True)

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
    print(f"Publishing reading: {payload}", flush=True)


if __name__ == "__main__":
    # TODO: Optionally, pass the sensor name as an argument to this script
    client = mqtt.Client(
        client_id="pseudo-mqtt-sensor",
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    )
    client.on_connect = on_connect
    client.on_message = on_message
    client.username_pw_set(username=USERNAME, password=PASSWORD)
    client.connect(host=HOST, port=PORT, keepalive=60)
    client.loop_forever()
