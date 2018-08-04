# rsa-keygen.py 
#
#   WARNING! THIS IS POSSIBLY *NOT* SECURE.
#   DO NOT USE TO ENCRYPT SENSITIVE INFO.
#
#   An implementation of a public/private keypair generation using RSA. 
#
#   written by Z. Henderson for Python 3.6
#
#   based on RSA as learned from Wikipedia & the cryptosystem described in
#   "Probabilistic Encryption and How to Play Mental Poker Keeping Secret
#   All Partial Information" by Goldwasser and Micali

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
            
    ## FINDING 1st PRIME ##
    p1 = largePrimeGen(numdigits)

    ## FINDING 2nd PRIME ##
    p2 = largePrimeGen(numdigits)

    n = p1*p2

    ## FINDING Y: QUADRATIC NONRESIDUE ##
    x = genNonresidue(p1,p2)
    y = coprime(n)

    c0 = pow(y, 2, n)
    c1 = pow(x*y*y, 1, n)

    print(c0,c1)
    plain = []
    pt = [[pow(c0%p1, (p1-1)//2, p1), pow(c0%p2, (p2-1)//2, p2)],[pow(c1%p1, (p1-1)//2, p1), pow(c1%p2, (p2-1)//2, p2)]]
    for tu in pt:
        if tu[0] == 1:
            if tu[1] == 1:
                plain.append(0)
            else:
                plain.append(1)
        else:
            plain.append(1)
            
    print(plain)
    
    ## This section is for RSA ##
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


    privatekey = "{0}\n{1}".format(hex(p1), hex(p2))
    publickey  = "{0}\n{1}".format(hex(y), hex(n))
    privateOutFile = open("privateKey", "w")
    publicOutFile = open("publicKey", "w")
    print(privatekey, file = privateOutFile)
    print(publickey, file = publicOutFile)
    privateOutFile.close()
    publicOutFile.close()

    print("\nSuccess!\n\nPrivate and public key generated in this directory.")

main()
