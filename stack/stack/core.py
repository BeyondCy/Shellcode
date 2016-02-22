#!/usr/bin/env python

__author__ = "B3mB4m"
__copyright__ = "Copyright 2016 B3mB4m"

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


import sys
import re
from linux_32 import *
from linux_64 import *
from auxiliary import *

class stack(object):
	def __init__(self, syntaxtype=None, target=None, bits=32, endian="little"):
		self.bits = bits
		self.endian = endian.lower()
		self.mul = [4 if self.bits == 32 else 8]
		self.generate = target
		self.syntaxtype = ["Intel" if syntaxtype == None else syntaxtype][0]
		self.cout = 0
		self.registers = [
				"rbx",
				"rdi",
				"rsi",
				"rdx",
				"r10",
				"r8",
				"r9",
		]
		self.string = None
		self.raw = ""
		self.newlist = [x for x in range(len(str(self.generate)))]
		for i in xrange(0, len(self.generate)):
			self.newlist[i] = self.generate[i]
			self.cout += 1;	

		if "/" in self.generate:
			self.string = self.calculatorifpath( self.generate)	
		else:
			self.string = self.calculatorifstring( self.generate)



		self.string = self.string[::-1]
		if self.bits == 64:
			self.register = {
				'r9':'',
				'r8':'',
				'r10':'',
				'rdx':'',
				'rsi':'',
				'rdi':'',
				'rbx':'',
			}
			for x in self.string:
				if len(x) >= 2:
					x = x[::-1]
				if "r9" in x[0]:
					self.register['r9'] = self.rearrange(x)
				elif "r8" in x[0]:
					self.register['r8'] = self.rearrange(x)
				elif "r10" in x[0]:
					self.register['r10'] = self.rearrange(x)
				elif "rdx" in x[0]:
					self.register['rdx'] = self.rearrange(x)
				elif "rsi" in x[0]:
					self.register['rsi'] = self.rearrange(x)
				elif "rdi" in x[0]:
					self.register['rdi'] = self.rearrange(x)
				elif "rbx" in x[0]:
					self.register['rbx'] = self.rearrange(x)	
			self.string = [x[::-1] for x in self.string]

		else:
			for x in self.string:
				x = x.replace("push  0x", "").replace("push 0x", "").replace("pushw  0x", "").replace("push $0x", "").replace("push  word 0x", "").replace("push 0x", "")
				second = re.findall("..?", x)[::-1]
				self.raw += "\\x68"+"\\x"+"\\x".join(second)
	

		del self.newlist
		del self.mul
		del self.bits
		del self.endian
		del self.generate
		del self.syntaxtype
		del self.cout
		del self.registers

	def calculatorifstring(self, string):
		self.empty = []
		if len(string) == self.mul[0]:
			if self.syntaxtype == "Intel":
				stack = "push 0x%s" % (string[::-1].encode('hex'))
			elif self.syntaxtype == "AT&T":
				stack = "push $0x%s" % (string[::-1].encode('hex'))
			return stack

		elif len(string) % self.mul[0] == 0:
			return self.splitter( string)
		else:
			dwordpart = string[0:(len(string)-len(string)%4)]
			wordpart = string[(len(string)-len(string)%4):len(string)]
			self.empty += self.splitter( dwordpart)
			self.empty += self.splitter(  wordpart, "WordTime")
			return self.empty


	def calculatorifpath(self, hexme):
		self.fill = "/"
		stack = []
		if len(hexme) % 4 == 0:
			self.fill = self.fill 
		elif  len(hexme) % 4 == 1:
			self.fill = self.fill * 4
		elif len(hexme)	% 4 == 2:
			self.fill = self.fill * 3
		elif len(hexme) % 4 == 3:
			self.fill = self.fill * 2

		if self.cout == self.mul[0]: 
			if self.bits == 64	:
				for x in self.registers:
					if self.syntaxtype == "Intel":
						stack.append("mov %s,0x%s" % (x,hexme[::-1].encode('hex')))
					elif self.syntaxtype == "AT&T":
						x = x.replace("r", "%r")
						stack.append("movabs $0x%s,%s" % (hexme[::-1].encode('hex'), x))
				return stack
			else:
				if self.syntaxtype == "Intel":
					stack.append("push 0x%s" % (hexme[::-1].encode('hex')))
				elif self.syntaxtype == "AT&T":
					stack.append("push $0x%s" % (hexme[::-1].encode('hex')))
				return stack
				
		elif self.cout > 4:
			if  len(hexme) % 4 == 0:
				return self.hextime(self.fill, hexme)
			elif len(hexme) % 4 == 1:
				return self.hextime(self.fill, hexme)
			elif len(hexme) % 4 == 2:
				return self.hextime(self.fill, hexme)
			elif len(hexme) % 4 == 3:
				return self.hextime(self.fill, hexme)		



	def hextime(self, putmein, hexme):
		for i in xrange(0, len(hexme)):
			if hexme[i] == "/":
				self.newlist[i] = putmein
				fixstring = self.complie( self.newlist)
				return self.splitter(fixstring)


	def complie(self, givemethatstring):
		compliestring = ""
		for i in givemethatstring:
			compliestring += i
		return compliestring			


	def splitter(self, hexdump, pushword="None"):
		self.mylist = []
		if pushword == "None":
			fixmesempai = re.findall('....?', hexdump)
			for x in fixmesempai:
				self.syntaxtyper( str(x[::-1].encode("hex")), "dword")
		else:
			dot = "." * len(hexdump)
			fixmesempai = re.findall(dot+'?', hexdump)
			for x in fixmesempai[::-1]:
				if dot > 2:
					self.syntaxtyper( str(x[::-1].encode("hex")), "dword")
				else:
					self.syntaxtyper( str(x[::-1].encode("hex")), "word")

		if self.bits == 64:
			self.mylist = [x.replace("push  0x", "").replace("push $0x", "") for x in self.mylist]	
			cache = []
			for reg in self.registers:
				if self.syntaxtype == "Intel":
					cache.append([("mov {0},0x{1}").format(reg,"".join(x)) for x in [self.mylist[x:x+2][::-1] for x in range(0, len(self.mylist), 2)]])	
				else:
					cache.append([("movabs $0x{0},%{1}").format("".join(x),reg) for x in [self.mylist[x:x+2][::-1] for x in range(0, len(self.mylist), 2)]])
			return cache
		else:
			return self.mylist


	def syntaxtyper(self, getstring, dwordORword):
		if self.syntaxtype == "Intel":
			if dwordORword == "dword":
				getstring = "push  0x%s" % getstring
				self.mylist.append(getstring)
			elif dwordORword == "word":
				getstring = "push  word 0x%s" % getstring
				self.mylist.append(getstring)
		elif self.syntaxtype == "AT&T":
			if dwordORword == "dword":
				getstring = "push $0x%s" % getstring
				self.mylist.append(getstring)
			elif dwordORword == "word":
				getstring = "pushw  0x%s" % getstring
				self.mylist.append(getstring)


	def rearrange(self, relist):
		padd = ""
		check = relist[0]

		if "r9" in check:
			padd = "r9"
		elif "r8" in check:
			padd = "r8"
		elif "r10" in check:
			padd = "r10"
		elif "rdx" in check:
			padd = "rdx"
		elif "rsi" in check:
			padd = "rsi"
		elif "rdi" in check:
			padd = "rdi"
		elif "rbx" in check:
			padd = "rbx"


		xor = "xor {},{}".format(padd, padd)
		push = "push {}".format(padd)
		lea = "lea {}, [rsp]".format(padd)

		cache = []
		for x in relist:
			if x == relist[0]:
				cache.append(xor)
				cache.append(x)
			else:
				cache.append(push)
				cache.append(x)

			if x == relist[-1]:
				cache.append(push)		
				cache.append(lea)
		return cache

		