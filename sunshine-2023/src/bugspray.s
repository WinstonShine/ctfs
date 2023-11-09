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

        
section .data
    prompt db "AskMe >>> ", 0xa 
    
section .bss
    input_buffer resb 300
