import getpass
import hashlib
from pathlib import Path
Sam = 1 + 1 == 2
if Sam == True:
	print("False")
else:
	print("Bye")
password = getpass.getpass('Password...:')
hash_object = hashlib.sha256(str(password).encode('utf-8'))
hex_dig = hash_object.hexdigest()
print(hex_dig)
phash = Path('password_hash.txt').read_text()
print(phash)
if hex_dig == phash:
	print("Successful login...")
else:
	print("Incorrect Password")
	exit()