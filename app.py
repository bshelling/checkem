#!/usr/bin/env python

from __future__ import print_function, unicode_literals
from PyInquirer import prompt, print_json
import hashlib
import os
import io


print("---------------------------")
print("")
print(" Checkem v1.0")
print(" Written By: Brandon Shelling | bshelling@gmail.com ")
print(" Application validates the itegrity of a downloaded file")
print("")
print("---------------------------")
print("")
questions = [
    {
        'type': 'input',
        'name': 'originHash',
        'message': 'Enter the original file\'s checksum:'
    },
    {
        'type': 'input',
        'name': 'fileName',
        'message': 'Enter the name of the file to validate:'
    }
]
answers = prompt(questions)


try:
    with open(os.getcwd()+'/'+answers['fileName'],'rb') as file:
        hash = file.read()
        file = hashlib.sha256(hash).hexdigest()

    origin = answers['originHash']
    if(origin == file):
        print("The file is valid")
    else:
        print("")
        print("This file is not valid the checksums do not match.\nPlease check with the original file owner and try again")
except Exception:
    print("")
    print("Something went wrong please try again.\nPlease be sure you entered a valid hash and filename.\nAlso you should execute this in the same directory where the file exists")
    print("")
   
