import time
import random
import paho.mqtt.client as mqtt

# MQTT broker details
broker_address = "localhost"  # Replace with your MQTT broker address
broker_port = 1883  # Replace with your MQTT broker port
topic = "inpt/infrastructure"

# Possible values for the "zone" tag
zones = ["zone1", "zone2", "zone3"]

# Generate and publish the message every 1 second
while True:
    # Generate random values for the data fields
    temperature = random.uniform(10, 50)
    humidity = random.uniform(40, 60)
    pressure = random.uniform(1000, 1020)
    voltage = random.uniform(220, 240)
    current = random.uniform(1, 20)
    energy_consumption = random.uniform(0, 1000)

    # Select a random zone from the list of possible zones
    zone = random.choice(zones)

    # Construct the message payload
    message = f"energy,zone={zone} temperature={temperature},humidity={humidity},pressure={pressure},voltage={voltage},current={current},energy_Consumption={energy_consumption}"

    # Create an MQTT client and connect to the broker
    client = mqtt.Client()
    client.connect(broker_address, broker_port)

    # Publish the message
    client.publish(topic, message)

    # Disconnect from the broker
    client.disconnect()

    # Wait for 1 second before publishing the next message
    time.sleep(1)
