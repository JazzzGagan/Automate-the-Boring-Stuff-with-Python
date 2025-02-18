#! /usr/bin/env python 3
#pw.py - An insecure password locker program.

PASSWORDS = {'facebook':'LKSJDLFJ3LKJ3434LJLDJFFACEBOOK',
             'laptop': 'SKDJFSJDFLAPTOP',
             'wifi': 'ASLKDJFLKS3393@339KLSDJWIFI',
             'mobile': 'KSJDLFJ2LKDF03J93J;MOBILE',
             'collegeemail': 'VOELLEGE23ICOLLEGE'}

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: py pw.py [account] - copy account passowrd')
    sys.exit()


account = sys.argv[1] # first command line for first argument

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Passowrd for ' + account + 'is copied to clipboard')
else:
    print('There is no account named ' + account )
    
