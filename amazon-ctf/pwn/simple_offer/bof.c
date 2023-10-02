#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>

void win() {
  char buf[64];
  FILE *f = fopen("flag.txt","r");
  if (f == NULL) {
    printf("%s", "You are at the right place, create a local flag to test.\n");
    exit(0);
  }

  fgets(buf,64,f);
  printf(buf);
}

void vuln(){
  char buf[32];
  gets(buf);

  printf("Taking the request to 0x%x\n", __builtin_return_address(0));
}

int main(int argc, char **argv){

  puts("Hello, what can I help you with? : ");
  vuln();
  return 0;
}
