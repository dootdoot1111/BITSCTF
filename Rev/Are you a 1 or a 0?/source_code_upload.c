#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char **argv)
{
  volatile int security_check;
  printf("Enter Super Secret Password:");
  char password[1024];

  security_check = 0;
  gets(password);

  if (security_check != 0)
  {
    printf("FLAG\n");
  }
  else
  {
    printf("NOT FLAG\n");
  }
}

// NOTE: "FLAG" is not the flag for this challenge.
// ADDITIONAL NOTE: The flag that you receive from "self_destruct_initiator" will be missing "{" and "}", which you will have to add so that it conforms to the
// flag format of BITSCTF{...}