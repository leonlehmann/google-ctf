hex = '84h, 93h, 81h, 0BCh, 93h, 0B0h, 0A8h, 98h, 97h, 0A6h,0B4h, 94h, 0B0h, 0A8h, 0B5h, 83h, 0BDh, 98h, 85h, 0A2h,0B3h,0B3h, 0A2h, 0B5h, 98h, 0B3h, 0AFh, 0F3h, 0A9h,98h, 0F6h, 98h, 0ACh, 0F8h, 0BAh'
xor_byte = int(0xC7)

flag = ""

for x in hex.split(','):
    flag += chr(int(x[:-1],16)^xor_byte)

print flag
