This challenge provides us with a binary and asks us to reverse engineer it go get the source code. Not exactly, but yeah, kinda. On running the binary we see :

```
>>> ./noah

please enter username and password
format is ./filename <username> <password>
```

We need to find the username and password. Cool! h4xx0r mode on.

To find the username and the password, just use grep. [grep](https://phoenixnap.com/kb/grep-command-linux-unix-examples) is a CLI tool which can search for a string or its pattern in a bigger file. 

We search for username and password and find :

```
>>>strings loose_strings | grep "username"


***************** The username is <REDACTED_USER> and the password is <REDACTED_PASS> *****************
please enter username and password
format is ./filename <username> <password>
incorrect username or password
```

The strings command used above returns all the human readable strings in a binary file.

Since the format to run the binary is given, we run :

```
>>> ./loose_strings <REDACTED_USER> <REDACTED_PASS>
```

To get our flag!!
