#!/usr/bin/env python3
import sys
import time
import argparse
import json
import paho.mqtt.client as mqtt

def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        data = json.loads(payload)
        # Annahme: {"hostname": "myhost", "metric": 42, "status": "OK"}
        hostname = data.get("hostname")
        if not hostname:
            return
        piggy_file = f"/var/lib/check_mk_agent/spool/piggyback/{hostname}/mqtt_status"
        os.makedirs(os.path.dirname(piggy_file), exist_ok=True)
        with open(piggy_file, "w") as f:
            print("<<<mqtt_status>>>", file=f)
            print(json.dumps(data), file=f)
    except Exception as e:
        # Optional: Fehlerhandling/Logging
        pass

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--mqtt_host", required=True)
    parser.add_argument("--mqtt_port", type=int, default=1883)
    parser.add_argument("--mqtt_topics", required=True)  # Kommagetrennte Liste
    args = parser.parse_args()

    client = mqtt.Client()
    client.on_message = on_message
    client.connect(args.mqtt_host, args.mqtt_port, 60)

    for topic in args.mqtt_topics.split(","):
        client.subscribe(topic.strip())

    client.loop_forever()

if __name__ == "__main__":
    main()

