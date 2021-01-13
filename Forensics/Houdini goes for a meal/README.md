# Houdini goes for a meal

This was probably the toughest forensics challenge provided. This challenge requires a very good knowledge about the JPEG file format. You can read more about the JPEG file format over [here](https://docs.fileformat.com/image/jpeg/), but I'll explain a bit too.

To the computers, file extensions do not help with interpreting what file format a given file is. File extensions are for us to see. A machine however, reads what is called the 'header' data of a file. Header data are the starting bytes of file that helps us understand what file format to use while interpreting a file. These bytes are same for all files with the same format. 

For example, all ZIP files have the same file headers(or signatures) :

```
50 4B 03 04 	  	         PK..
```

These 'magic numbers' help a machine understand what file format a file has. Coming back to JPEG files. All JPEG files possess the following header:

![jpegfileformat](https://github.com/dootdoot1111/BITSCTF/raw/main/Forensics/Houdini%20goes%20for%20a%20meal/jpgfileformat.jpg)

You can understand and compare this to the file given to us that it is malformed and is missing some bytes from the header.

We add '49 46' at offset 8 to our file and change the extension to '.jpg', and lo behold, a cool jpeg image! To add these Hexadecimal bytes, you can use nay hex editors [online](https://hexed.it/) or just install one.

Now the last step demands us to revisit steganography, with steghide. Use steghide on this image with password, well, it couldn't be more obvious, "STEGOHIDEO". Yeah, That ez. Run :

```
steghide extract -sf Houdini_goes_for_a_meal.jpg
```

Enter the password to get the Flag.txt file!
