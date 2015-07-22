import ctypes
import sys
import platform
import locale

"""
 ___            _                             ___ 
| _ ) ___ _ __ | |__  ___ _ _ _ __  __ _ _ _ / __|
| _ \/ _ \ '  \| '_ \/ -_) '_| '  \/ _` | ' \\__ \
|___/\___/_|_|_|_.__/\___|_| |_|_|_\__,_|_||_|___/
 				|_   _|__ __ _ _ __  
				  | |/ -_) _` | '  \ 
				  |_|\___\__,_|_|_|_|

arwin - win32 address resolution program
Steve hanna v.01[C]
B3mB4m v.01[Python]

This program finds the absolute address
of a function in a specified DLL.
Happy shellcoding!
"""

 

print "arwin.py - win32 address resolution program - by b3mb4m - v.01\n"
if len(sys.argv) != 3:
	print "%s <Library Name> <Function Name>\n" % sys.argv[0]
kernel32 = ctypes.windll.kernel32
if kernel32 == None:
	print "Error: could not load library!\n";
	sys.exit()


info = platform.uname()
print """
Platform  : %s
Machine   : %s
Language  : %s
""" % (platform.platform(), platform.uname()[4],locale.windows_locale[kernel32.GetUserDefaultUILanguage()])

try:
	handle = kernel32.GetModuleHandleA(sys.argv[1])
	address = kernel32.GetProcAddress(handle, sys.argv[2])
	print "\n%s is located at %s in %s" % (sys.argv[2], hex(address), sys.argv[1])
except Exception as Errorlog:
	print Errorlog
