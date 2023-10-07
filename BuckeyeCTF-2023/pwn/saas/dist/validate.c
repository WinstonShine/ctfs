#include <stdio.h>
#include <string.h>
#include <sys/mman.h>
#include <stdlib.h>
#include <ctype.h>

#include <capstone/capstone.h>

#define die(x) do { puts(x); exit(-1); } while (0)


#define SHELLCODE_ADDR 0xdead0000
#define SHELLCODE_MAX_SIZE 0x100
#define INPUT_SIZE SHELLCODE_MAX_SIZE*2
size_t parsehex(char *src, char *dest) {
    size_t len = strlen(src);
    if (src[len-1] == '\n') {
        src[len-1] = '\0';
        len--;
    }
    if (len % 2 == 1)
        die("*** Bad hex (odd length) ***");
    size_t final_len = len / 2;
    for (size_t i=0, j=0; j<final_len; i+=2, j++) {
        if (!(isxdigit(src[i]) && isxdigit(src[i+1])))
            die("*** Bad hex (invalid char) ***");
        dest[j] = (src[i] % 32 + 9) % 25 * 16 + (src[i+1] % 32 + 9) % 25;
    }

    return final_len;
}

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    
    printf("Welcome to shell code as a shell\n");
    printf("Enter your shellcode (in hex please) up to %d chars\n", INPUT_SIZE);
    char input[INPUT_SIZE+1];
    void *shellcode;
    shellcode = mmap(SHELLCODE_ADDR, SHELLCODE_MAX_SIZE, PROT_WRITE | PROT_READ, MAP_PRIVATE | MAP_ANONYMOUS, -1, 0);
    fgets(input, sizeof(input), stdin);
    
    printf(input);
    size_t sz = parsehex(input, shellcode);
    printf(shellcode); 
    exit(0);
}
