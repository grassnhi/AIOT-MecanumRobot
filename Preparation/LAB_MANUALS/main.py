import sys
from Adafruit_IO import MQTTClient
import time
import random
from ohstem_simplecamera import *

AIO_FEED_IDs = ["nutnhan1", "nutnhan2"]
AIO_USERNAME = "grassnhi"
AIO_KEY = "aio_ZaES78XvsIHKHsUZGYxYRD693IVq"

def connected(client):
    print("Ket noi thanh cong ...")
    for topic in AIO_FEED_IDs:
        client.subscribe(topic)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu: " + payload + " , feed id:" + feed_id)

client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()
counter = 0
sensor_type = 0
counter_ai = 5
ai_result = ""
previous_result = ""

while True:
    counter_ai = counter_ai - 1
    if counter_ai <= 0:
        counter_ai = 5
        previous_result = ai_result

        response = requests.get(img_url)
        if response.status_code:
            fp = open('Pics//greenland_' + str(counter_ai) +'.png', 'wb')
            fp.write(response.content)
            fp.close()

            ai_result, image = image_detector(counter_ai)
            print("AI Output: ", ai_result)
            if previous_result != ai_result:
                client.publish("ai", ai_result)
                client.publish("image", image)

            requests.get(control_url + ai_result)

    time.sleep(1)
    pass