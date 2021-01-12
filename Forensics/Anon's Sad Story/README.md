# Anon's Sad Story

The challenge provides us a with a pdf file containing a sad story from an anonymous poster in a funny 4chan style. And, yes I hate GIMP too.

The flag can be found very easily by just searching "BITSCTF" in the pdf file. We use grep command for this purpose. 'grep' is a CLI command on bash that can search through a bigger file for a string or a pattern of string.

You can read more about how to use it [here](https://phoenixnap.com/kb/grep-command-linux-unix-examples).

Fire up the terminal and run :

```
grep -a "BITSCTF" Anon_uses_Linux.pdf
```
Ez flag!
