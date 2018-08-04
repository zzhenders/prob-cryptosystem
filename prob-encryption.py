# p-encryption.py
#
#   WARNING! THIS IS PROBABLY *NOT* SECURE. DO NOT USE FOR ACTUAL ENCRYPTION.
#
#   Probabilistically encrypts a given file in a compressed format. 
#
#   written by Z. Henderson
#
#   based on Probabilistic Encryption and How to Play Mental Poker Keeping
#   Secret All Partial Information" by Goldwasser and Micali

from secrets import randbelow
from mathtools import *

def cipher(binary, x, n):
    """This function will generate a list of ciphertext integers."""

    cipherlist = []
    for i in range(len(binary)):
        y = coprime(n)              # generates random coprime
        nlen = len(hex(n)) - 2
        
        if binary[i] == 0:
            cipherlist.append(hex(pow(y, 2, n)))
        else:
            cipherlist.append(hex(pow(x*y*y, 1, n)))
    #cipherlist.reverse()
    
    text = list2hex(cipherlist, nlen)
    return text

def list2hex(listofhex, k):
    hexa = "".join(listofhex)
    listofhex = hexa.split('0x')
    listofhex.remove('')
    listofhex.insert(0,'20')                 # padding to ensure no loss of data
    listofhex.append('20')                   # padding again to ensure no loss of data
    for i in range(len(listofhex)):
        while len(listofhex[i]) < k:
            temp = listofhex.pop(i)
            listofhex.insert(i,'0'+temp)     
    hexa = "".join(listofhex)
    return hexa

def main():

    print("This program will encrypt a file you specify.")
    print("It will only work on simple text files")
    print("(e.g. plaintext.txt, plaintext)\n")
    print("Note that long messages will take a long time to encrypt!\n")

    mname = "message" #input("Please enter the filename\nof the file you want to encrypt: ")

    pubKeyFile = open("publicKey",'r')
    pubKey = []
    for line in pubKeyFile:
        pubKey.append(int(line, 16))
    pubKeyFile.close()

    infile = open(mname, 'r')
    plain = infile.read()
    infile.close()

    hexaList = []
    for i in plain:
        hexaList.append(hex(ord(i)))
    hexa = list2hex(hexaList,2)

    decimal = int(hexa, 16)
    binary = bin(decimal)
    binary = binary[2:]                     # now we have the plaintext as a string of bits!

    ciphertext = cipher(binary,pubKey[0],pubKey[1])
    outfile = open('ciphertext', 'w')
    print(ciphertext, file = outfile)
    outfile.close()
#    if bits < 16:
        #perform encryption on whole string
#        1==1
#    else:
#        for i in range(bits-16):
#            print(binary[i:i+17])
    #ciphertext = pow(decimal, pubKey[0], pubKey[1])
    #cipherhex = hex(ciphertext)
    
    
main()
