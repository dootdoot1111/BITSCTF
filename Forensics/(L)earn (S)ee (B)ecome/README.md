#  (L)earn (S)ee (B)ecome 

This is a yet another steganography challenge, forensics sucks, but steganography doesn't. (Atleast for me) This challenge gives us a PNG image of kittens, its cute, but I'm more of a dog person.

Anyways, using steghide won't work here, because steghide is compatible only to JPEG images, and not PNG. Googling for steganography tools for PNG images, we come across, [zsteg](https://github.com/zed-0xff/zsteg).

A quick look through the [user manual](https://github.com/zed-0xff/zsteg#usage) we can easily understand how to use the tool. Run the following on a terminal:

```
zsteg -a kittens.png
```

This might litter(no pun intended) your screen with garbage, but knowing the flag format, its easy to spot our flag!
