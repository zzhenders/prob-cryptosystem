# rsa-decryption.py
#
#   WARNING! THIS IS PROBABLY *NOT* SECURE. DO NOT USE FOR ACTUAL ENCRYPTION.
#
#   Decrypts an encrypted file using RSA. 
#
#   written by Z. Henderson
#
#   based on "Probabilistic Encryption and How to Play Mental Poker Keeping
#   Secret All Partial Information" by Goldwasser and Micali

def decipher(ciphertext, p, q):

    nlen = len(hex(p*q)) - 2

    ciphertext = ciphertext[:-1]
    clen = len(ciphertext)

    clist = []
    for i in range(clen//nlen):
        clist.append(ciphertext[i*nlen:(i*nlen)+nlen])

    residue = []

    for hexnum in clist:
        residue.append[pow(hexnum%p, (p-1)//2, p), pow(hexnum%q, (q-1)//2, q)]

    binary = ""
    for tup in residue:
        if tup[0] == 1:
            if tup[1] == 1:
                binary.append('0')
            else:
                binary.append('1')
        else:
            binary.append('1')

    
    #[pow(c0%p1, (p1-1)//2, p1), pow(c0%p2, (p2-1)//2, p2)]
    
def list2hex(listofhex, k):
    hexa = "".join(listofhex)
    listofhex = hexa.split('0x')
    listofhex = listofhex[1:-1]             #removing padding
    for i in range(len(listofhex)):
        while len(listofhex[i]) < k:
            temp = listofhex.pop(i)
            listofhex.insert(i,'0'+temp)     
    hexa = "".join(listofhex)
    return hexa

def main():

    print("This program will decrypt a file you specify.")
    print("It will only work on simple text files")
    print("(e.g. ciphertext.txt, ciphertext)\n")
    print("Note that long messages will take a long time to decrypt!\n")

    cname = "ciphertext" #input("Please enter the filename\nof the file you want to encrypt: ")

    priKeyFile = open("publicKey",'r')
    priKey = []
    for line in priKeyFile:
        priKey.append(int(line, 16))
    priKeyFile.close()

    infile = open(cname, 'r')
    ciphertext = infile.read()
    infile.close()

    plaintext = decipher(ciphertext, priKey[0], priKey[1])


    
main()
