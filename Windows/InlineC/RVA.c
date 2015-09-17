#include <Windows.h>
#include <stdio.h>

//Coded by B3mB4m
//gcc -masm=intel RVA.c -o RVA.exe


DWORD ExportTable( void )
{
	__asm__
 	(
 		".intel_syntax noprefix;"
 		"xor ecx,ecx;"
	    "mov ecx,[fs:0x30];"   
	    //Certain nullbyte fs:0x30
	    "mov ecx,[ecx+0xc];"            
	    "mov ecx,[ecx+0x14];"          
	    "mov ecx,[ecx];"        
	    "mov ecx,[ecx];" 
	    //Two nullbyte again              
	    "mov ebx,[ecx+0x10];"                         

	    "mov edx,[ebx+0x3c];"             
	    "add edx,ebx;"
	    "mov edx,[edx+0x78];"             
	    "add edx,ebx;" 

	    //RVA + Module Base Address = VA

	    "xchg edx,eax"    
	   
	  
	);

}



int main( void )
{
	printf("Kernel32 ExportTable : 0x%08X\n", ExportTable());
}
