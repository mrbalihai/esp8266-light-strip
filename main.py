from light import solid
from network import WLAN, STA_IF
from umqtt.simple import MQTTClient
from time import sleep

SSID=""
WPA_PASSWORD=""
MQTT_SERVER=""

rgb = [1, 20, 1]
status = b"OFF"
client = MQTTClient("light-strip", MQTT_SERVER)

def connect_network():
    sta_if = WLAN(STA_IF)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, WPA_PASSWORD)
        while not sta_if.isconnected():
            pass
    print('connected to network', sta_if.ifconfig())

def mqtt_sub(topic, msg):
    global rgb
    print(str(topic, "utf-8"), str(msg, "utf-8"))
    if topic == b"study/light-strip/switch":
        if msg == b"ON":
            solid(*rgb)
        elif msg == b"OFF":
            solid(0, 0, 0)
        status = msg
        client.publish("study/light-strip/status", status)
    elif topic == b"study/light-strip/rgb/set":
        rgb = list(map(int, str(msg, "utf-8").split(",")))
        print(rgb)
        # client.publish("study/light-strip/rgb/status", rgb)

def connect_mqtt():
    client.set_callback(mqtt_sub)
    client.connect()
    client.subscribe("study/#")
    while True:
        if True:
            client.wait_msg()
        else:
            client.check_msg()
            time.sleep(1)
    client.disconnect()

def main():
    solid(0, 0, 0)
    connect_network()
    connect_mqtt()


main()

