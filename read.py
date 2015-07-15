#!/usr/bin/env python
#
# Keep reading a DYMO scale until too many errors
# Mainly taken from http://steventsnyder.com/reading-a-dymo-usb-scale-using-python/ with a few alterations
#

import usb.core
import usb.util
from time import sleep

VENDOR_ID = 0x0922
PRODUCT_ID = 0x8003

# find the USB device
device = usb.core.find(idVendor=VENDOR_ID, idProduct=PRODUCT_ID)

if not device:
  print 'ERROR: No device found.'
  exit(1)

# use the first/default configuration
device.set_configuration()
# first endpoint
endpoint = device[0][(0,0)][0]

# read a data packet
attempts = 10
while attempts > 0:
  try:
    data = device.read(endpoint.bEndpointAddress,
               endpoint.wMaxPacketSize)
    print data
    sleep (0.5)
  except usb.core.USBError as e:
    data = None
    if e.args == ('Operation timed out',):
      attempts -= 1
      continue

print 'Done.'
