from string import ascii_lowercase

a = 69
b = 420
c = 49154

for x in range(0, c):
    if((a ^ x) + (b ^ x) == (c ^ x)):
        bin_key = bin(x)[2:]

    else:
        continue


intArr = []
for x in range(1, len(ascii_lowercase)):
    intArr.append(bin(x)[2:].zfill(5))

bacon_dict = dict(zip(intArr, ascii_lowercase))

print("BITSCTF{", end='')

for x in range(0, len(bin_key), 5):
    print(bacon_dict[bin_key[x:x + 5]], end='')

print("}")
