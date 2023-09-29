from ast import NotIn
from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

import requests

import keyboard

import time
from datetime import datetime

#Recibir arduino
import argparse
import struct
import sys
import time
import traceback

import pigpio
from nrf24 import *


from functions_reader import *
from functions_utils import *
from config import *

COM = "COM4"

client = InfluxDBClient(url="http://localhost:8086",
                        token=token,
                       org=org)

END = False


print("FS Real Time Raspberry pi 4\n")

#print("\nPress PLAY to start RSHIFT to end")
while not END:

    #print(keyboard.read_key())
    #if keyboard.read_key() == "play/pause media":

    print("Programa inicializado\n")

    piloto,circuito = rundata()

    bucketnever = createbucket(piloto,circuito)
    print(f"Bucket created with ID - {bucketnever}")

    rxnrf24(bucketnever,bucket,piloto,circuito)

    print("\nPress PLAY to start RSHIFT to end")

    #para Flux, si quieres seleccionr un bucket por ID en vez del nombre -> from bucketID... 