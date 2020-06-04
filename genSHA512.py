'''
Generate the printable form of a sha512 password hash as produced by crypt (C)

https://en.wikipedia.org/wiki/Passwd
https://en.wikipedia.org/wiki/Crypt_(C)
$<id>$<salt>$<hash>

Example:
$6$qoE2letU$wWPRl.PVczjzeMVgjiA8LLy2nOyZb...
'''
import crypt
import getpass

# Program's Purpose
# Multi-line comment in Python
print('''Generate a sha512 password hash as produced by crypt (C)
Please enter a password to encrypt.
''')

try:
    t1Pass, t2Pass = getpass.getpass(), getpass.getpass('Enter password again: ')

    while t1Pass !=  t2Pass:
      print('Passwords do not match. Please try and enter your password again.')
      t1Pass, t2Pass = getpass.getpass(), getpass.getpass('Enter password again: ')

    tPass = t2Pass

except Exception as error:
    print('ERROR: ', error)
else:
    # Print salted sha512 hash to console
    print(crypt.crypt(tPass, crypt.mksalt(crypt.METHOD_SHA512)))
    
