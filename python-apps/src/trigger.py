"""
This script implements and schedules the Trigger that is used to tell all the IoT
sensors in the MQTT network to publish their reading. It is currently setup to publish
a trigger signal four times an hour, every 15 minutes.
"""

import functools
import os
import time

import logging
import paho.mqtt.client as mqtt
import schedule
import sys

# Set up the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[logging.StreamHandler(stream=sys.stdout)],
)
LOGGER = logging.getLogger("trigger")

# Setup MQTT variables
TRIGGER_TOPIC = "sensors/trigger"
HOST = str(os.getenv("MQTT_HOST"))
PORT = int(os.getenv("MQTT_PORT"))
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")


def publish_trigger() -> None:
    """Publish the trigger signal to the MQTT network."""
    LOGGER.info("Publishing trigger...")
    client = mqtt.Client(
        client_id="trigger",
        callback_api_version=mqtt.CallbackAPIVersion.VERSION2,
    )
    client.username_pw_set(username=USERNAME, password=PASSWORD)
    client.connect(host=HOST, port=PORT, keepalive=60)
    client.publish(topic=TRIGGER_TOPIC, payload=str(True))
    client.disconnect()


def main() -> None:
    """Main function to setup the scheduler."""
    job = functools.partial(publish_trigger)

    LOGGER.info("Starting trigger...")
    schedule.every().hour.at(":00").do(job)
    schedule.every(5).minutes.do(job)
    LOGGER.info(schedule.jobs)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
