from string import ascii_lowercase  #just imported the lowercase alphabets(abcdefghijk...), which means a variable named ascii_lowercase was created having value 'abcdefghjikl....z'

a = 69                                                                           #nice
b = 420
c = 49154

for x in range(0, c):
    if((a ^ x) + (b ^ x) == (c ^ x)):        # just the given expression, but in variables
        bin_key = bin(x)[2:]                 # python outputs numbers converted to binary as '0b10101010', so to ignore the 0b, we used the [2:]

    else:
        continue


intArr = []
for x in range(1, len(ascii_lowercase)):
    intArr.append(bin(x)[2:].zfill(5))        # just created an array having binary numbers from 1 to 26

bacon_dict = dict(zip(intArr, ascii_lowercase))     # bacon cipher encodes all alphabets as binary numbers of the position of the alphabet. With a having position 0 to z having position 25

print("BITSCTF{", end='')       # just ensuring the flag format. The end='; stuff just ensured we dont print a newline

for x in range(0, len(bin_key), 5):
    print(bacon_dict[bin_key[x:x + 5]], end='')     # reads the binary form of the decimal key, 5 bits at a time, looks for the corresponding alphabet and prints it

print("}")              # flag format. can't score with it, can't score without it.
