#!/usr/bin/python

import ctypes
import multiprocessing

"""
Python shellcode execution formwork.
                         -Philipp Hagemeister
TESTED ON : Ubuntu 14.04 -B3mB4m                         
"""



shellcode_data = (b"SHELLCODE")

shellcode = ctypes.c_char_p(shellcode_data)
function = ctypes.cast(shellcode, ctypes.CFUNCTYPE(None))

addr = ctypes.cast(function, ctypes.c_void_p).value
libc = ctypes.CDLL('libc.so.6')
pagesize = libc.getpagesize()
addr_page = (addr // pagesize) * pagesize
for page_start in range(addr_page, addr + len(shellcode_data), pagesize):
    assert libc.mprotect(page_start, pagesize, 0x7) == 0
function()    
