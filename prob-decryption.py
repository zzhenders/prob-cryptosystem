# prob-decryption.py
#
#   WARNING! THIS IS POSSIBLY *NOT* SECURE.
#   DO NOT USE TO ENCRYPT SENSITIVE INFO.
#
#   Decrypts an encrypted file. 
#
#   written by Z. Henderson

def decipher(ciphertext, p, q):

    if ord(ciphertext[-1]) == 10:
        ciphertext = ciphertext[:-1]    # removes end-of-text newline character if present

    nlen, clen = len(hex(p*q)) - 2, len(ciphertext)
    clist = []
    for i in range(clen//nlen):         # breaks large hex number into blocks
        clist.append(ciphertext[i*nlen:((i+1)*nlen)])

    residue = []                        # calculates residuosity of each number block mod p,q
    for hexnum in clist:
        residue.append([pow(int(hexnum,16)%p, (p-1)//2, p), pow(int(hexnum,16)%q, (q-1)//2, q)])
   
    binary = []                         # if the number is a quadratic nonresidue mod n
    for tup in residue:                 # return 0, otherwise return 1
        if tup[0] == 1:
            if tup[1] == 1:
                binary.append('0')
            else:
                binary.append('1')
        else:
            binary.append('1')

    binary = "".join(binary)            # translates binary to hexadecimal
    hexa = hex(int(binary, 2))
    hexa = hexa[2:]

    chars = []                          # for each 2-digit hex, finds unicode char 
    for i in range(len(hexa)//2):       # and assembles them into a string
        temp = hexa[2*i:2*i+2]
        chars.append(chr(int(temp,16)))
    plain = "".join(chars)
    return plain
    
def main():

    print("This program will decrypt a file you specify.")
    print("It will only work on simple text files")
    print("(e.g. ciphertext.txt, ciphertext)\n")
    print("Note that long messages will take a long time to decrypt!\n")

    cname = "ciphertext" #input("Please enter the filename\nof the file you want to encrypt: ")

    infile = open(cname, 'r')
    ciphertext = infile.read()
    infile.close()

    priKeyFile = open("privateKey",'r')
    priKey = []
    for line in priKeyFile:
        priKey.append(int(line, 16))
    priKeyFile.close()

    plaintext = decipher(ciphertext, priKey[0], priKey[1])
    outfile = open('plaintext', 'w')
    print(plaintext, file = outfile)
    outfile.close()

    print("\nSuccess!\n\nPlaintext file generated in this directory.")
    
main()
