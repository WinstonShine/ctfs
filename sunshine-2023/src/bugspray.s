; 64bit
; nasm -f elf64
; ld -o
;   _start:
;       write syscall to give user prompt "AskMe >>> "
;   bugspray:
;   loop:
;   off:

section .text
    _start:
        ; write prompt
        mov eax, 0x1
        mov edi, 0x1
        mov rsi,prompt
        mov edx, 0xc
        syscall

        ; mmap - not sure what the args all mean yet
        mov eax, 0x9
        mov edi, 0x777777
        mov esi, 0x12c
        mov edx, 0x7
        mov r10d, 0x22
        mov r8, 0xffffffffffffffff
        mov r9d, 0x0
        syscall
        mov r12d, 0x64

    loop:
        ; ?
        inc    r10
        cmp    r10,r12
        jne    loop
        mov    eax,0x0
        mov    edi,0x0
        mov    esi,0x777777
        mov    edx,0x1f4
        syscall
        add    rax,0x20
        mov    r11d,0x66
        cmp    rax,r10
        jl     bugspray
        cmp    rax,r11
        jge    bugspray
        mov    edi,0x0
        mov    esi,0x0
        mov    edx,0x0

        ;
        syscall
        test   rax,rax
        je     off
        xor    rax,rax
        mov    ecx,0x64

        bugspray:
        inc r10

    off:
        inc r10

section .data
    prompt db "AskMe >>> ", 0xa, 
    
section .bss
    input_buffer: resb 300
