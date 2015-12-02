import pefile
import re
import sys

#Coded By B3mB4m
#02.12.2015

def getOPcodes( exe):
	pe = pefile.PE( exe)
	db = pe.sections[0].get_data().encode("hex")
	db = db.split("ffffffff00000000ffffffff")[0]
	db = re.findall("..?", db)
	return "\\x"+"\\x".join(db)


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print "Usage : python exe2shellcode.py [ExePath]"
		sys.exit()
	else:
		print "\n\n"+getOPcodes( sys.argv[1])
