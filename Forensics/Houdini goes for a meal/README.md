# Houdini goes for a meal

This was probably the toughest forensics challenge provided. This challenge requires a very good knowledge about the JPEG file format. You can read more about the JPEG file format over [here](https://docs.fileformat.com/image/jpeg/), but I'll explain a bit too.

To the computers, file extensions do not help with interpreting what file format a given file is. File extensions are for us to see. A machine however, reads what is called the 'header' data of a file. Header data are the starting bytes of file that helps us understand what file format to use while interpreting a file. These bytes are same for all files with the same format. 

For example, all ZIP files have the same file headers(or signatures) :

```
50 4B 03 04 	  	         PK..
```

These 'magic numbers' help a machine understand what file format a file has. Coming back to JPEG files. All JPEG files possess the following header:

![jpegfileformat]()
