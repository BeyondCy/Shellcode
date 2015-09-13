#Before windows shellcode, we need practice.

    I'm not working on windows last 2 years, so I'm start debugging etc.. 
    Before shellcoding must be funny some inline assembly  :)



        ntdll!_PEB_LDR_DATA
           +0x000 Length           : 0x10000
           +0x004 Initialized      : 0xff ''
           +0x008 SsHandle         : 0x00400000 Void
           +0x00c InLoadOrderModuleList : _LIST_ENTRY [ 0x341ea0 - 0x20000 ]
    -->       +0x014 InMemoryOrderModuleList : _LIST_ENTRY [ 0x0 - 0x240000 ]
           +0x01c InInitializationOrderModuleList : _LIST_ENTRY [ 0x7c970620 - 0x7c8f1000 ]
           +0x024 EntryInProgress  : 0x7c8f10e0 Void
        
   
