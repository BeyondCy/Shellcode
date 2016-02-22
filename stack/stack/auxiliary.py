import re

def port( port):
	db = []
	if not (1 <= int(port) <= 65555):
		from sys import exit
		exit("Out of range ..")
	else:
		fixmesempai = re.findall('..?', hex(int(port))[2:])
		reg = 'push word 0x{0}'.format("".join(fixmesempai[::-1]))
		ret = {
			'register': reg,
			'raw' : "\\x"+"\\x".join(fixmesempai[::-1]),
		}
		return ret

def ip( ip):
	ip = str(ip).split(".")
	db = []
	db2 = []
	for x in ip:
		db.append(hex( int(x))[2:])
	for x in db: 
		if len(x) == 1:
			x = "0"+x
		db2.append(x)

	ret = {
		'register': 'push dword 0x'+"".join(db2[::-1]),
		'raw' :"\\x"+"\\x".join(db2[::-1]),
		}
	return ret
