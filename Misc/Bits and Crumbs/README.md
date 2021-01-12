# Bits and Crumbs

This challenge is pretty straightforward. It gives us a zip file, with concatenated folders, all having images in them. A bit annoying tbh. Anyways, one way is to use an image editor (like GIMP), and add all 4 images in the zip file to a bigger image, and scan the QR code formed in the middle to get the flag.

But, since I've already made my hate for GIMP clear earlier, there exists a shorter way to it too. 

For some reason, all four images look different when opened than their thumbnails. We extract the thumbnail, which can be done by using exiftool :

``` 
exiftool -b -thumbnailImage 1.jpg > thumbnail.jpg
```
I've done this for 1.jpg, so make sure you are in the correct folder when running the above command. This can be done on any of the four images, we got from the zip file.

Open the thumbnail image and scan the correct QR code. Make sure you scan the QR code in the middle. But check the other QR's out too. They're cool. I mean what could go wrong, Right?
