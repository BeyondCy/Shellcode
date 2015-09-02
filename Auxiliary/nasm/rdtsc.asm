;Coded By B3mB4m  
;Concat : b3mb4m@tuta.io   
; ___            _                             ___ 
;| _ ) ___ _ __ | |__  ___ _ _ _ __  __ _ _ _ / __|
;| _ \/ _ \ '  \| '_ \/ -_) '_| '  \/ _` | ' \\__ \
;|___/\___/_|_|_|_.__/\___|_| |_|_|_\__,_|_||_|___/
;                             Bomberman & B3mB4m & T-Rex   

;Tested on : Kali Linux


;nasm -f elf testvm.asm
;gcc -m32 -o testvm testvm.o


extern  printf                          
section .text                           
        global main		   
main:				       
        mov  ebx,0x0A 

loop:
        push    ebp		;Set stack frame
        mov     ebp,esp
        xor     edi,edi
        xor     ecx,ecx

        rdtsc 
        add     edi,eax
        rdtsc 
        sub     eax,edi

        push    eax
        add     [total],eax

        push    dword printformat             
        call    printf                  
        add     esp, 8          

        mov     esp, ebp	       
        pop     ebp		   

        dec  ebx
        jnz  loop
        jz   average

average:
        xor eax,eax
        xor edx,edx
        mov eax,[total]
        mov ecx,0x0A
        div ecx

        ;Divinded  :  EDX:EAX   
        ;Quotient  :  EAX       
        ;Remainder :  EDX       

        push eax
        push dword printformat2
        call printf


        cmp eax,0xc8
        jg  vm    
        jl  notvm


vm:
        xor ebx,ebx
        push ebx
        push vmdetect
        call printf
        jmp  exit

notvm:
        xor ebx,ebx
        push ebx
        push vmnotpresent
        call printf
        jmp  exit

exit:

        xor  eax,eax
        inc  al
        int  0x80


section .data  
        vmdetect: db "VM Detected", 10, 0
        vmnotpresent db "VM not present", 10, 0          
        printformat:    db "RDTSC difference : %d", 10, 0 ; The printf format, "\n",'0'
        printformat2:    db "RDTSC average : %d ", 10, 0    
        total: dd 0



