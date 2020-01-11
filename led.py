#!/usr/bin/python3

import board
import neopixel
import random
import time
import socket
import paho.mqtt.client as mqtt

hostname = socket.gethostname()
CLIENT_NAME = 'prusa_'+hostname
MQTT_HOST = 'hiome.local'
MQTT_PORT = 1883

topic = '_hiome/1/sensor/' + CLIENT_NAME + '/event/'

pixels = neopixel.NeoPixel(board.D18, 15)

OFF   = (0,0,0)
WHITE = (255,255,255)
RED   = (255,0,0)
YELLOW= (255,255,0)
GREEN = (0,128,0)

currentColor = OFF
def setLight(newColor):
  pixels.fill(newColor)
  currentColor = newColor

def onMessage(client, userdata, msg):
  if msg.topic == topic + 'PrintStarted':
    setLight(WHITE)
  elif msg.topic == topic + 'PrintDone':
    setLight(OFF)
  elif msg.topic == topic + 'PrintCancelling':
    setLight(YELLOW)
  elif msg.topic == topic + 'PrintCancelled':
    setLight(OFF)
  elif msg.topic == topic + 'PrintPaused':
    setLight(YELLOW)
  elif msg.topic == topic + 'PrintResumed':
    setLight(WHITE)
  elif msg.topic == topic + 'PrintFailed':
    setLight(RED)
  elif msg.topic == topic + 'Error':
    setLight(RED)
  elif msg.topic == topic + 'Upload':
    # flash green for 10 seconds
    oldColor = currentColor
    setLight(GREEN)
    time.sleep(5)
    setLight(oldColor)
    time.sleep(1)
    setLight(GREEN)
    time.sleep(4)
    setLight(oldColor)
  elif msg.topic == topic + 'Connecting':
    setLight(GREEN)
  elif msg.topic == topic + 'Connected':
    setLight(OFF)
  elif msg.topic == topic + 'Disconnecting':
    setLight(YELLOW)
  elif msg.topic == topic + 'Disconnected':
    setLight(OFF)
  elif msg.topic == '_hiome/1/sensor/' + CLIENT_NAME + '/status' and msg.payload == 'disconnected':
    setLight(RED)

def onConnect(client, userdata, flags, rc):
  client.subscribe('_hiome/1/sensor/' + CLIENT_NAME + '/#', qos=1)
  setLight(OFF)

client = mqtt.Client(client_id=CLIENT_NAME, clean_session=False)
client.on_connect = onConnect
client.on_message = onMessage
client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_forever()
