#!/usr/bin/env python

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

try:
	from capstone import *
except:
	from sys import exit
	exit("This script requires capstone, please install before use it.")

class instructions(object):
	def __init__(self, bits=32):
		self.list = []
		if bits == 32:
			self.md = Cs(3, 4)
		else:
			return "This script is still beta and not support x64 bit."
			#self.md Cs(X, X)	

	def random1byte(self, instruction, registers):
		instruction = instruction.split(",")
		registers = registers.split(",")
		for instruct in instruction:
			for target in registers:
				target = "%s %s" % (instruct,target)
				for a in range(0,16):
					for b in range(0,16):
						string = hex(a)[2:]+hex(b)[2:]
						cache = string
						cache = r"\x%s" % cache[:2]
						for i in self.md.disasm(string.decode("hex"), 0x10):
							test =  "%s %s" % ( i.mnemonic, i.op_str)
							if target == test:
								self.list.append(cache)
		return self.list	


	def random2byte(self, instruction, registers):
		instruction = instruction.split(",")
		registers = registers.split(",")
		for instruct in instruction:
			for target in registers:
				target = "%s %s,%s" % (instruct,target,target)
				for a in range(0,16):
					for b in range(0,16):
						for c in range(0, 16):
							for d in range(0, 16):
								string = hex(a)[2:]+hex(b)[2:]+hex(c)[2:]+hex(d)[2:]
								cache = string
								cache = r"\x%s\x%s" % (cache[:2], cache[2:])
								for i in self.md.disasm(string.decode("hex"), 0x10):
									test =  "%s %s" % ( i.mnemonic, i.op_str)
									if target in test.replace(', ', ','):
										self.list.append(cache)
		return self.list


