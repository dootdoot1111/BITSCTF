# Listen Close (Not really.)

This challenge requires us to analyze audio files in a altogether different way. It gives us an audio file and a password proteced zip file. For this challenge we'll be using an audio analysis software called [Audacity](https://www.audacityteam.org/download/).

Open audacity and import the wav file in it.

Next, we view the 'Spectrogram' of the audio file. It is a visual representation of the audio file under some frequencies vs time. To do this click on the small arrow beside the file name in audacity and select Spectrogram.

![SpectrogramSelect](https://github.com/dootdoot1111/BITSCTF/raw/main/Misc/Listen%20Close%20(Not%20really.)/Screenshot%202021-01-12%20at%201.23.24%20PM.png)

After the screen turns somewhat colourful, stretch the waveform, a bit until the text, becomes clear and readable.(Which is a bit tough, you'll need to focus, it hurts your eye tho).

If you struggle with getting a clear image, try using other spectrogram tools, like [Sonic Visualiser](https://sonicvisualiser.org/download.html), or online tools.

This is what you get with Sonic Visualiser(recommended coz its clearer) :

![SonicSS](https://github.com/dootdoot1111/BITSCTF/raw/main/Misc/Listen%20Close%20(Not%20really.)/Screenshot%202021-01-12%20at%201.31.03%20PM.png)

Text :

###### CONGRATULATIONS
###### H3R3 1S Y0UR PA55W0RD:
######                       s1i2l3k4v5w6f7i8t9v0
###### PS : Shift 'em by the sum of the numbers. Gaius commands you.

Googling Gaius we find Caesar, again. This is an obvious hint to Caesar shift cipher. The numbers appearing before the password are 3, 3, 1, 5, 5 which add up to 17. [Shift](https://www.dcode.fr/caesar-cipher) the password by 17, to get the password for the zip file. 

Unzip the zip file, read the text file to get your Flag!
