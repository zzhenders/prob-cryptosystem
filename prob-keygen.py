# prob-keygen.py 
#
#   WARNING! THIS IS POSSIBLY *NOT* SECURE.
#   DO NOT USE TO ENCRYPT SENSITIVE INFO.
#
#   An implementation of a public/private keypair generation. 
#
#   written by Z. Henderson

from math import gcd, sqrt
from secrets import randbelow
from time import sleep
from mathtools import *

def largeOddGen(num):
    """This function returns a odd integer with num +/- 3 digits."""

    large = ''
    num = num + randbelow(8) - 4        # num +/- 3
    for i in range(num):
        large = large + '9'

    large = int(large)                  #this is num number of 9s

    token = True
    odd = 1
    while token:
        odd = randbelow(large)

        if odd <= large//10:            # checks number of digits
            token = True
        elif odd%2 == 0:                # checks if odd
            token = True
        else:
            return odd                  # returns an odd integer of appropriate size

def largePrimeGen(numdigits):
    """This function generates an integer that is almost certainly a prime,
    with the specified number of digits. Skips some numbers regardless of
    their primality in an attempt to account for side-channel attacks."""

    prime = 0
    for i in range(randbelow(10) + 1):  # flush random pool
        prime = largeOddGen(numdigits)  # generates large odd int

    notprime = True
    while notprime:
        prime = prime + 2
        
        if randbelow(2) == 0:
            notprime = True             # sometimes skip numbers regardless if prime
        else:
            notprime = not isPrime(prime)

    return prime

def main():

    print("""Moving the mouse or pressing keys while this calculates
will increase the randomness of the result.

Please also be patient, this will take a moment.""")

    #try:
    sleep(2)                            # provides the user with sufficient time to respond
    numdigits = 200                     # how long primes should be, in decimal digits
            
    p1 = largePrimeGen(numdigits)       ## FINDING 1st PRIME ##
    p2 = largePrimeGen(numdigits)       ## FINDING 2nd PRIME ##
    n = p1*p2

    x = genNonresidue(p1,p2)            ## FINDING X: QUADRATIC NONRESIDUE ##
    y = coprime(n)

    msg = 'Hello'                       ## Testing crypto to ensure everything
    hexa = []                           ## works properly, that numbers aren't
    for c in msg:                       ## extremely unlucky. This has a very
        temp = hex(ord(c))              ## low chance of failing.
        temp = temp[2:]
        if len(temp) < 2:
            temp = '0' + temp
        hexa.append(temp)
    num = "".join(hexa)
    num = bin(int(num,16))
    num = num[2:]
    cyp = []
    
    for bit in num:
        if bit == '0':
            cyp.append(hex(pow(y, 2, n)))
        else:
            cyp.append(hex(pow(x*y*y, 1, n)))

    res = []
    for hexnum in cyp:
        res.append([pow(int(hexnum,16)%p1, (p1-1)//2, p1), pow(int(hexnum,16)%p2, (p2-1)//2, p2)])

    plain = []
    for tu in res:
        if tu[0] == 1:
            if tu[1] == 1:
                plain.append('0')
            else:
                plain.append('1')
        else:
            plain.append('1')

    plain = "".join(plain)
    hexa = hex(int(plain,2))
    hexa = hexa[2:]
    chars = []
    for i in range(len(hexa)//2):
        temp = hexa[2*i:2*i+2]
        chars.append(chr(int(temp,16)))
    plain = "".join(chars)
    print(plain)

    if msg != plain:
        return "Sorry, unlucky numbers chosen. Please try again!"
    
    ## This section is for RSA implementation ##
#    lambdaN = ctf(p1,p2)                      # Charmichael totient function
#
#    e = coprime(lambdaN)                      # encryption exponent
#
#    d = eEuclidean(e,lambdaN)                 # decryption exponent
#
#    m = 12345                                 # run a test to ensure everything works
#    c = pow(m,e,n)
#    p = pow(c,d,n)
#    if m != p:
#        return "Sorry, please try again!"     # if we stumbled on an unlucky number
#    else:
#        privatekey = "{0}\n{1}".format(hex(d), hex(n))
#        publickey = "{0}\n{1}".format(hex(e), hex(n))

    else:
        privatekey = "{0}\n{1}".format(hex(p1), hex(p2))
        publickey  = "{0}\n{1}".format(hex(x), hex(n))
        privateOutFile = open("privateKey", "w")
        publicOutFile = open("publicKey", "w")

        print(privatekey, file = privateOutFile)
        print(publickey, file = publicOutFile)
        privateOutFile.close()
        publicOutFile.close()
        print("\nSuccess!\n\nPrivate and public key generated in this directory.")

main()
