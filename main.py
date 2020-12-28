import json
import time

import paho.mqtt.client as mqtt
import requests
from requests.auth import HTTPBasicAuth

from env_var import *
from update_db import database_update


# connection notification that the script is running
def on_connect(client, userdata, flags, rc):
    print("connected with code: " + str(rc))
    client.subscribe(MQTT_TOPIC)


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    payload = json.loads(msg.payload.decode("utf-8", "ignore"))
    vehicle = payload["objects"]
    if vehicle:
        ring_phone()
        database_update(vehicle)
        time.sleep(5)
        return 200

# Ring the IP phone
def ring_phone():
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    data = 'XML=<CiscoIPPhoneExecute><ExecuteItem Priority="0" URL="Dial:{0}"/></CiscoIPPhoneExecute>'.format(phone_number)
    r = requests.post(base_url, headers=headers, data=data, auth=HTTPBasicAuth(username, password))
    print(r)
    return r.status_code


if __name__ == "__main__":
    MQTT_TOPIC = "/merakimv/" + CAMERA_SERIAL + "/raw_detections"
    try:
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.connect(MQTT_SERVER, MQTT_PORT, 60)
        client.loop_forever()

    except Exception as ex:
        print("[MQTT]failed to connect or receive msg from mqtt, due to: \n {0}".format(ex))
