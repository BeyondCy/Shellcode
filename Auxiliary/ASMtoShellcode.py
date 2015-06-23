import os
import sys
import commands

class complier(object):
	#Author : B3mB4m
	#Greetz : Bomberman
	#This script directly convert asm files to shellcode. 
	#That's only pre-release will be append windows,nasm etc.. 
	#Stay tuned ! 
	def __init__(self):	
		self.target = sys.argv[1]
		self.command1 = "nasm -f elf %s" % sys.argv[1]
		self.filename = sys.argv[1].split(".")[0]
		self.temporaryfile = "%s.o" % self.filename
		self.command2 = "ld -s -o %s %s.o" % (self.filename,self.filename)
		self.shellcode = command2 = r'''for i in $(objdump -d %s |grep "^ " |cut -f2); do echo -n '\x'$i; done; echo''' % (self.filename)
		self.getme = [self.command1, self.command2, self.shellcode]
		self.complie()
	
	def complie(self):
		if "NASM version" not in commands.getoutput("nasm -v"):
			print "You must install nasm complier .."
			print "Install command : apt-get install nasm" 
			print "Please wait .."
			command = 'apt-get install nasm' 
			process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True).stdout.read()
			if "NASM version" not in process.strip():
				print "Install failed.Please install it manual."
				sys.exit()
			else:
				print "Nasm installed.Process continues .. "	
			
		self.justincase()
		coutme = 0
		for i in self.getme:
			commands.getoutput(i)
			if coutme == 2:
				if "x00" in commands.getstatusoutput(i)[1]:
					print "\n#WARNING : NULL BYTES HERE !#\n";
					print "\n%s\n" % commands.getstatusoutput(i)[1]
				else:
					print "\n%s\n" %  (commands.getstatusoutput(i)[1])
			coutme += 1	
		self.justincase()	

	def justincase(self):
		if os.path.exists(self.filename) or os.path.exists(self.temporaryfile):
			try:
				os.remove(self.filename)
				os.remove(self.temporaryfile)
			except Exception as errorlog:
				print errorlog.message 
				sys.exit()


if __name__ == '__main__':
	if os.getuid() != 0:
		sys.exit("You need to have root privileges to run this script.")
		#Because as you can see that script using terminal commands ..
	else:	
		complier()				
