"""
This script implements and schedules the Trigger that is used to tell all the IoT
sensors in the MQTT network to publish their reading. It is currently setup to publish
a trigger signal four times an hour, every 15 minutes.
"""

import time

import schedule


def publish_trigger() -> None:
    """Publish the trigger signal to the MQTT network."""

    print("Publishing trigger...", flush=True)


def main() -> None:
    """Main function to setup the scheduler."""

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
