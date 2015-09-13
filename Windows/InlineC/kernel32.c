#include <Windows.h>
#include <stdio.h>

//Coded By B3mB4m
//gcc -masm=intel kernel32.c -o kernel.exe


DWORD kernel( void )
{
	__asm__
 	(
 		".intel_syntax noprefix;"       
		"mov eax,[fs:0x30];" 				
		"mov eax,[eax+0xc];"				
		"mov eax,[eax+0x14];"			
		"mov eax,[eax];"					
		"mov eax,[eax];"					
		"mov eax,[eax+0x10];"	
	);

}


int main( void )
{
	printf("kernel32.dll : 0x%08X\n", kernel());
	//HMODULE lib = LoadLibrary("kernel32.dll");  Raw C codes
	//printf("0x%p\n", lib);
}



