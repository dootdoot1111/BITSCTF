# Stop Twitching

Challenge text :

##### Ryan’s eye often starts twitching for no particular reason, but after he solves a problem, it usually goes away. This time he came across this problem:

##### 69 + 420 = 49154

##### It was perplexing but then he realised that all the 3 terms in the original equation were actually bitwise xor’ed with a binary number and this was the resulting equation. Furthermore, the binary number is deduced after a key is chosen. For example, if key = “asdfg”, then the binary number = “0000110011001000011000111”.

##### Can you help Ryan find the key that was used. Flag Format = BITSCTF{key}

The question itself is pretty straightforward. We just need to find a number which when xorr'ed to the three numbers will make the equation mathematically correct. This can be done fairly easily through bruteforce!!

The key can be then found from it, by first getting the binary representation of that number, splitting it into chunks of 5 and decoding the individual components to letters. the last step involves the use of 'Bacon' cipher.

I wrote a short [python script](https://github.com/dootdoot1111/BITSCTF/blob/main/Crypto/Stop%20Twitching/xorpls.py) for it, which i have attached. Run it to get the flag!

PS: The flag and the challenge name all reference to the 'Pog' emote often used on the livestreaming site [Twitch](https://www.twitch.tv).

PPS : The term Pog originates from an age old iconic blooper reel featuring [Ryan Gootecks, in his hilarious "POG" face](https://www.youtube.com/watch?v=g9TNY75jhcs&t=127).
