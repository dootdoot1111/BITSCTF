# Baking with a Machine

Challenge text :

**A robot was trying to bake a cake using acetic acid along with a special ingredient called "SODA", during which it misplaced it's flag in the process. Can you find it?**

The question references to the idea that all machines/robots read data in binary(1/0), and looking at the text file given, we can see the resemblance, of 'o' to 0 and the '!' to 1.
Good old find and replace gives the binary text.

We then convert the Binary text to ASCII or readable text, through one of the [online solvers](https://binarytotext.net/).

Now the final string does look a bit like our flag, but isn't. Going through the challenge text, we understand that the 'special ingredient' SODA, is actually the encryption key used to Vigenere encrypt our flag. 
Decrypt the text with 'SODA' as the key to get the flag!
