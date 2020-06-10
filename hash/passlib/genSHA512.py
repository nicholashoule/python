'''
Cross-platform:
Generate the printable form of a sha512 password hash as produced by Linux crypt (C)

https://en.wikipedia.org/wiki/Passwd
https://en.wikipedia.org/wiki/Crypt_(C)
https://foss.heptapod.net/python-libs/passlib
$<id>$<salt>$<hash>

Example:
$6$qoE2letU$wWPRl.PVczjzeMVgjiA8LLy2nOyZb...
'''
# Standard library imports
import getpass
import random
import string
import argparse

# Third-party library imports
from passlib.hash import sha512_crypt

# argparse, argument parser
# .. _argparse: https://docs.python.org/3/library/argparse.html
parser = argparse.ArgumentParser(
    description='''Cross-platform: Generate a sha512 password hash as produced by Linux crypt (C)'''
)
parser.add_argument('-r', '--rounds', type=int, default=5000,
                    help='specify the rounds')
args = parser.parse_args()

# Purpose
# Important: This script is only compatible with crypt (C) on Linux.
print(parser.description)


# verify() - Verify the password hash
def verify(tpass, thash):
    # To-Do:
    # sha512_crypt.verify(tpass, thash)
    return sha512_crypt.verify(tpass, thash)


# Attempt to hash/verify the user's password
try:
    tsalt = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(16)])
    t1Pass, t2Pass = getpass.getpass(), getpass.getpass('Enter password again: ')

    while t1Pass != t2Pass:
        print('Passwords do not match. Please try and enter your password again.')
        t1Pass, t2Pass = getpass.getpass(), getpass.getpass('Enter password again: ')

    tpass = t2Pass
    thash = sha512_crypt.using(salt=tsalt, rounds=args.rounds).hash(tpass)

except Exception as error:
    print('ERROR: ', error)
else:
    # Verify and print the hash
    if verify(tpass, thash):
        print(thash)
    else:
        print("[Tainted]: Couldn't verify the sha512 hash.")
