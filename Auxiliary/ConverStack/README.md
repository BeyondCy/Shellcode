#Version II Updated !
Now working on all strings or paths.


#Some test results 
         python stack.py --type "AT&T" --target "Test"
         push $0x74736554

         python stack.py --type "Intel" --target "/bin/bash"
         push 0x68736162
         push 0x2f6e6962
         push 0x2f2f2f2f

         python stack.py --type "AT&T" --target "My lovely push string "
         push $0x6e697274
         push $0x73206873
         push $0x75702079
         push $0x6c65766f
         push $0x6c20794d
         pushw  0x2067
         
         python stack.py --type "Intel" --target "Command to execute"
         push 0x75636578
         push 0x65206f74
         push 0x20646e61
         push 0x6d6d6f43
         push  word 0x6574
         
         
         python stack.py --type "Intel" --target "C:\Program Files"
         push 0x73656c69
         push 0x46206d61
         push 0x72676f72
         push 0x505c3a43
   
#b3mb4m@gmail.com
   





