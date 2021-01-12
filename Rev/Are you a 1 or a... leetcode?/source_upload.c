#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>
#include <string.h>

int main(int argc, char **argv)
{
    volatile int security_check;
    char buffer[1024];

    if (argc == 1)
    {
        printf("Enter password as command line argument next time.\nIntializing Shut Down Sequence...\n");
        exit(1);
    }

    security_check = 0;
    strcpy(buffer, argv[1]);

    if (security_check == 0x1337C0D3)
    {
        printf("FLAG\n");
    }
    else
    {
        printf("Nice try, but not quite.\nTry again, you got 0x%08x\n", security_check);
    }
}

// NOTE: "FLAG" is not the flag for this challenge.
// ADDITIONAL NOTE: The flag that you receive from "self_destruct_initiator" will be missing "{" and "}", which you will have to add so that it conforms to the
// flag format of BITSCTF{...}. Make sure you know the difference between 0 and O.
