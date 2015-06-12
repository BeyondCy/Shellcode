Linux/x86 - exit - 5 bytes

#Greetz : Bomberman(Leader)
#Author : B3mB4m
#My Leader the BEST.


Disassembly of section .text:

08048060 <.text>:
 8048060:	31 c0                	xor    %eax,%eax
 8048062:	40                   	inc    %eax
 8048063:	cd 80                	int    $0x80

#include <stdio.h>

const char stopbich[] = "\x31\xc0\x40\xcd\x80";


main(){
	int (*shell)();
	shell=stopbich;
	printf("Hello world\n");
	shell();
	printf("Hello world 2\n");
}

//Output : Hello world
