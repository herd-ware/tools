'''
File: uart_display.py
Created Date: 2023-02-26 08:53:02 pm
Author: Mathieu Escouteloup
-----
Last Modified: 2023-02-26 08:54:00 pm
Modified By: Mathieu Escouteloup
-----
License: See LICENSE.md
Copyright (c) 2023 HerdWare
-----
Description: 
'''


import serial 
import random
import time


serial_port = serial.Serial()

serial_port.baudrate = 9600
serial_port.port = '/dev/ttyUSB2'
serial_port.timeout = 1
serial_port.bytesize = serial.EIGHTBITS
serial_port.stopbits = serial.STOPBITS_ONE
serial_port.parity = serial.PARITY_EVEN

serial_port.open()

s_display = ""
if (serial_port.is_open):
  while (serial_port.in_waiting != 0):
    serial_port.reset_input_buffer()

  print ("START COMMUNICATION VIA UART:")

  while True:
    if (serial_port.in_waiting != 0):
      v_read = serial_port.read(1)

      print(v_read)

#      if ((len(s_display) >= 4) & (s_display[0:4] == "[TC]")):
#        print("C1")
#        print(v_read)
#        v_int = int.from_bytes(v_read, "big")
#        print(v_int)
#
#        if (v_int == 10):
#          print(s_display)
#          s_display = ""
#
#      else:
#        v_dec = v_read.decode() 
#        if (v_dec == '\n'):
#          print(s_display)
#          s_display = ""
#        else:
#          s_display = s_display + v_dec

  serial_port.close()
