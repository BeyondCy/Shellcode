import sys
import re
from optparse import OptionParser
#Deprecated since version 2.6
#The commands module has been removed in Python 3. Use the subprocess module instead.
#I'm still using 2.x, so fuck it lol.
try:
	from colorama import init,Fore
	init()
except:
	print "Please, install colorama module!"
	print "pip install colorama"

#Author  : B3mB4m
#Title   : Shellcode Helper(x86 Litle Endian Stack Converter)
#Concat  : b3mb4m@gmail.com
#Version : v2
#Supported  AT&T - Intel Syntaxs
#Most boring part shellcoding turning strings to stack but from now on its not !

def helper():
	print r"""	
 ___            _                             ___ 
| _ ) ___ _ __ | |__  ___ _ _ _ __  __ _ _ _ / __|
| _ \/ _ \ '  \| '_ \/ -_) '_| '  \/ _` | ' \\__ \
|___/\___/_|_|_|_.__/\___|_| |_|_|_\__,_|_||_|___/
     				Bomberman & B3mB4m & T-Rex                                             



root~/Desktop$ python stack.py --type "AT&T"  --target "MyString" or "PATH"
root~/Desktop$ python stack.py --type "Intel" --target "MyString" or "PATH"
	""";
	sys.exit()


class B3mB4mPusheR(object):
	def __init__(self, syntaxtype, target):
		self.generate = target
		self.syntaxtype = syntaxtype
		self.cout = 0
		self.fill = "/"
		self.newlist = [x for x in range(len(str(self.generate)))]
		for i in xrange(0, len(self.generate)):
			self.newlist[i] = self.generate[i]
			self.cout += 1;	

		if "/" in self.generate:
			self.calculatorifpath( self.generate)	
		else:
			self.calculatorifstring( self.generate)


	def calculatorifstring(self, string):
		if len(string) == 4:
			if self.syntaxtype == "Intel":
				stack = "push 0x%s" % (string[::-1].encode('hex'))
			elif self.syntaxtype == "AT&T":
				stack = "push $0x%s" % (string[::-1].encode('hex'))
			print(Fore.GREEN + stack)
			sys.exit()
		elif len(string) % 4 == 0:
			self.splitter( string)
		else:
			dwordpart = string[0:(len(string)-len(string)%4)]
			wordpart = string[(len(string)-len(string)%4):len(string)]
			self.splitter( dwordpart)
			self.splitter(  wordpart, "WordTime")


	def calculatorifpath(self, hexme):
		#In linux doesnt matter how many / in path.
		#So we can use that our purpose.
		#Therefore,we dont need convert to words too. 
		if len(hexme) % 4 == 0:
			self.fill = self.fill 
		if  len(hexme) % 4 == 1:
			self.fill = self.fill * 4
		elif len(hexme)	% 4 == 2:
			self.fill = self.fill * 3
		elif len(hexme) % 4 == 3:
			self.fill = self.fill * 2

		if self.cout == 4: 
			if self.syntaxtype == "Intel":
				stack = "push 0x%s" % (hexme[::-1].encode('hex'))
			elif self.syntaxtype == "AT&T":
				stack = "push $0x%s" % (hexme[::-1].encode('hex'))
			print(Fore.GREEN + stack)
			sys.exit()
			
		elif self.cout > 4:
			if  len(hexme) % 4 == 0:
				self.hextime(self.fill, hexme)
			elif len(hexme) % 4 == 1:
				self.hextime(self.fill, hexme)
				sys.exit()
			elif len(hexme) % 4 == 2:
				self.hextime(self.fill, hexme)
				sys.exit()
			elif len(hexme) % 4 == 3:
				self.hextime(self.fill, hexme)	
				sys.exit()	


	def hextime(self, putmein, hexme):
		for i in xrange(0, len(hexme)):
			if hexme[i] == "/":
				self.newlist[i] = putmein
				fixstring = self.complie( self.newlist)
				self.splitter(fixstring)
				break;	


	def complie(self, givemethatstring):
		compliestring = ""
		for i in givemethatstring:
			compliestring += i
		return compliestring			


	def splitter(self, hexdump, pushword="None"):
		self.mylist = []
		if pushword == "None":
			fixmesempai = re.findall('....?', hexdump)
			for x in fixmesempai[::-1]:
				self.syntaxtyper( str(x[::-1].encode("hex")), "dword")
		else:
			fixmesempai = re.findall('..?', hexdump)
			for x in fixmesempai[::-1]:
				self.syntaxtyper( str(x[::-1].encode("hex")), "word")

		for x in self.mylist:
			print (Fore.GREEN + x)	


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


if __name__ == '__main__':
	parser = OptionParser()
	parser.add_option('--type', action="store")
	parser.add_option('--target', action="store")
	options, args = parser.parse_args()

	if options.type:
		B3mB4mPusheR( options.type, options.target)
	else:
		helper()
