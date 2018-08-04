# prob-encryption.py
#
#   WARNING! THIS IS POSSIBLY *NOT* SECURE.
#   DO NOT USE TO ENCRYPT SENSITIVE INFO.
#
#   Probabilistically encrypts a given file. 
#
#   written by Z. Henderson

from secrets import randbelow
from mathtools import *

def cipher(binary, x, n):
    """This function will generate a list of ciphertext integers."""

    nlen = len(hex(n)) - 2
    cipherlist = []
    
    for bit in binary:
        y = coprime(n)              # generates random coprime
        
        if bit == '0':
            temp = hex(pow(y, 2, n))
            cipherlist.append(temp[2:])
        else:
            temp = hex(pow(x*y*y, 1, n))
            cipherlist.append(temp[2:])

    for i in range(len(cipherlist)):
        while len(cipherlist[i]) < nlen:
            temp = cipherlist.pop(i)
            cipherlist.insert(i, '0'+temp)
    text = "".join(cipherlist)
    return text

def main():

    print("This program will encrypt a file you specify.")
    print("It will only work on simple text files")
    print("(e.g. plaintext.txt, plaintext)\n")
    print("Note that long messages will take a long time to encrypt!\n")

    pubKeyFile = open("publicKey",'r')
    pubKey = []
    for line in pubKeyFile:
        pubKey.append(int(line, 16))
    pubKeyFile.close()

    infile = open("message", 'r')
    plain = infile.read()
    infile.close()

    hexaList = []                           # this segment translates plaintext to a number
    for i in plain:
        temp = hex(ord(i))
        temp = temp[2:]
        if len(temp) < 2:
            temp = '0' + temp
        hexaList.append(temp)
    hexa = "".join(hexaList)
    binary = bin(int(hexa, 16))
    binary = binary[2:]                     # now we have the plaintext as a string of bits!

    ciphertext = cipher(binary,pubKey[0],pubKey[1])
    outfile = open('ciphertext', 'w')
    print(ciphertext, file = outfile)
    outfile.close()

    print("\nSuccess!\n\nCiphertext file generated in this directory.")
    
main()
