# -*- coding: utf-8 -*-

'''''''''''''''''''''''''''''''''
@Author : Vic P.
@Email  : vic4key@gmail.com
@Name   : Serial Port
'''''''''''''''''''''''''''''''''

import sys
from PyVutils import Others

# python3 -m serial.tools.list_ports
# python3 -m serial.tools.miniterm
# python3 -m serial.tools.miniterm <port_name>

from serial import Serial
from pprint import *

com = Serial(port="COM6", baudrate=9600, timeout=0)

if not com.is_open: com.open()

pp = PrettyPrinter(indent=4)
pp.pprint(com)
pp.pprint(com.get_settings())

try:
	while True:
		com.reset_input_buffer()
		com.reset_output_buffer()

		data = com.readline()
		if len(data) > 0:
			print(f"<= `%s`" % data)
		else:
			data = input("Enter: ") + "\n"
			data = data.encode()
			print(f"=> `%s`" % data)
			com.write(data)
		pass
	pass

except (Exception, KeyboardInterrupt):
	com.close()
	Others.LogException(sys.exc_info())

#$ Serial<id=0x219d7bd0be0, open=True>(port='COM6', baudrate=9600, bytesize=8, parity='N', stopbits=1, timeout=0, xonxoff=False, rtscts=False, dsrdtr=False)
#$ {   'baudrate': 9600,
#$     'bytesize': 8,
#$     'dsrdtr': False,
#$     'inter_byte_timeout': None,
#$     'parity': 'N',
#$     'rtscts': False,
#$     'stopbits': 1,
#$     'timeout': 0,
#$     'write_timeout': None,
#$     'xonxoff': False}
#$ Enter: I
#$ => `b'I\n'`
#$ <= `b'Arduino reply : I\n'`
#$ <= `b'\n'`
#$ Enter: am
#$ => `b'am\n'`
#$ <= `b'Arduino reply : am\n'`
#$ <= `b'\r\n'`
#$ Enter: Vic
#$ => `b'Vic\n'`
#$ <= `b'Arduino reply : Vic\n'`
#$ <= `b'\n'`