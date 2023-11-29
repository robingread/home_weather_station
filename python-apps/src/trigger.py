"""
This script implements and schedules the Trigger that is used to tell all the IoT
sensors in the MQTT network to publish their reading. It is currently setup to publish
a trigger signal four times an hour, every 15 minutes.
"""

import functools
import os
import time

import paho.mqtt.client as mqtt
import schedule

TRIGGER_TOPIC = "sensors/trigger"

HOST = str(os.getenv("MQTT_HOST"))
PORT = int(os.getenv("MQTT_PORT"))
USERNAME = os.getenv("MQTT_USERNAME")
PASSWORD = os.getenv("MQTT_PASSWORD")


def publish_trigger(client: mqtt.Client) -> None:
    """Publish the trigger signal to the MQTT network."""
    print("Publishing trigger...", flush=True)
    client.publish(topic=TRIGGER_TOPIC, payload=str(True))


def main() -> None:
    """Main function to setup the scheduler."""

    client = mqtt.Client(client_id="trigger")
    client.username_pw_set(username=USERNAME, password=PASSWORD)
    client.connect(host=HOST, port=PORT, keepalive=60)

    publish_func = functools.partial(publish_trigger, client)
    print("Starting trigger...", flush=True)
    # Schedule four times an hour at 15-minute intervals starting at the top of the hour
    schedule.every().hour.at(":00").do(publish_trigger)
    schedule.every().hour.at(":15").do(publish_trigger)
    schedule.every().hour.at(":30").do(publish_trigger)
    schedule.every().hour.at(":45").do(publish_trigger)
    print(schedule.jobs, flush=True)

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()
