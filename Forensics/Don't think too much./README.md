#  Don't think too much. 

We'll do what the challenge title says and just not think too much. This time the challenge provides us with three files. A password protected zip file, a text file with a 'master' password and an image of a random dude.

Well the image is not that of a random dude but is that of the great Julius Caesar. To solve with challenge you require a tool most commonly used for [steganography](https://en.wikipedia.org/wiki/Steganography) problems in CTF's called steghide.

[Steghide](https://github.com/StefanoDeVuono/steghide) is used to hide data in LSB of jpeg images. It can also be password protected, which it is, for our challenge.

First we use the 'master' password in the text file provided, which is, well, as it happens to be, 69. (Nice) Extract the hidden text file from the image useing steghide as follows:

```
steghide extract -sf Random_guy.jpg
```

Enter the password '69' next and you'll be able to extract a text file named 'embedded.txt'. Open the text file, to get the password for your zip file.

Unzip with the found password, check out not bod.txt, to get your flag! (Remember to add the flag format BITSCTF{...} )
