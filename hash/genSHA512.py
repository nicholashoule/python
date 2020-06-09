'''
Generate the printable form of a sha512 password hash as produced by crypt (C)

https://en.wikipedia.org/wiki/Passwd
https://en.wikipedia.org/wiki/Crypt_(C)
$<id>$<salt>$<hash>

Example:
$6$qoE2letU$wWPRl.PVczjzeMVgjiA8LLy2nOyZb...
'''
import sys
import crypt
import getpass

# Purpose
# Important: This script is only compatible with crypt (C) on Linux.
print('''
Generate a sha512 password hash as produced by crypt (C)
''')

# Crypt, as defined by POSIX, doesn't mandate a specific encryption algorithm
# hence OSX crypt() isn't compatible with this script.
if 'linux' not in sys.platform.lower():
    print('This script is only compatible with crypt (C) on Linux.')
    sys.exit(1)

try:
    print('Please enter a password to encrypt.')
    t1Pass, t2Pass = getpass.getpass(), getpass.getpass('Enter password again: ')

    while t1Pass != t2Pass:
        print('Passwords do not match. Please try and enter your password again.')
        t1Pass, t2Pass = getpass.getpass(), getpass.getpass('Enter password again: ')

    tPass = t2Pass

except Exception as error:
    print('ERROR: ', error)
else:
    # Print salted sha512 hash to console
    print(crypt.crypt(tPass, crypt.mksalt(crypt.METHOD_SHA512)))
