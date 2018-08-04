# mathtools.py
#   Contains functions used by multiple parts of the encryption system

from secrets import randbelow
from math import gcd, sqrt

def coprime(integer):
    """This function generates a random number 2 <= n < integer-2
    such that n and integer are coprime."""

    n = randbelow(integer-2)
    
    while True:
        if n < 2:
            n = randbelow(integer-2)
        elif gcd(integer, n) != 1:
            n = randbelow(integer-2)
        elif n%2 == 0:
            n = n - 1
        else:
            return n

def isPrime(n):                     # checks for a prime
    """This implementation of the Fermat primality test outputs True
    if the integer is a prime, and False otherwise. Runs the test
    80 times or until the test is failed."""

    # variables use the typical notation for the Fermat primality test
    # a**(n-1) mod n = 1

    a = coprime(n)
    
    for i in range(80):
        if pow(a, n-1, n) != 1:
            return False
        elif pow(a, n-1, n) == 1:
            1 + 1                   #do nothing, here mainly to allow check for errors
        else:
            return "error"

    return True

def ctf(p,q):
    """Carmichael's totient function, assuming p and q are both prime.
    Which is to say, using Euler's totient function."""
    
    # lambda(n) = lcm(lambda(p), lambda(q)) = lcm(p − 1, q − 1)
    # works because in lambda(p**n), p is prime and n is 1,
    # which allows us to use the Euler totient:
    # phi(p**n), where p is prime and n is >= 1, equals (p**(n-1))(p-1) 
    # lcm(a,b) = a*b/gcd(a,b)
    # thank you, Wikipedia

    #lcm = ((p-1)/(gcd(p-1, q-1)))*(q-1)
    denominator = gcd(p-1, q-1)
    
    intermediate = (p-1) // denominator
    result = intermediate * (q-1)
    return result

def eEuclidean(a,b):
    """Performs the extended Euclidean algorithm to find the
    multiplicative inverse of a mod b."""
    
    r0, r1, r2  = a, b, 0
    s0, s1, s2  = 1, 0, 0
    t0, t1, t2  = 0, 1, 0
    q2          = 0

    while True:
        q2 = r0//r1
        r2 = r0%r1
        s2 = s0 - (q2 * s1)
        t2 = t0 - (q2 * t1)

        if r2 == 0:
            return s1%b
        else:
            r0, s0, t0 = r1, s1, t1
            r1, s1, t1 = r2, s2, t2

def jacobi(numerator, denominator):
    """Uses the Jacobi symbol to determine quadratic
    residuosity of numerator mod(denominator).
    
             { 0 if inputs are not coprime
    result = { 1 if numerator is a quadratic residue
             {-1 if numerator is not a quadratic residue.
    """

    q, p, swap, sign = numerator, denominator, 0, 1
    
    while True:
            
        q = q%p                         # 1: Reduce q

        while q%2 == 0:                 # 2: Extract any even 'numerator'
                                    
            if (p%8 == 1 or p%8 == 7):      # using properties of the Jacobi Symbol,
                sign = sign                 # leaves sign of result
            elif (p%8 == 3 or p%8 == 5):    # or
                sign = sign*(-1)            # flips the sign of the result

            q = q//2
                    
        if q == 1:                      # 3: if num = 1, result = 1
            return 1*sign
        elif gcd(q,p) != 1:                 # otherwise, if q & p *not* coprime odd integers
            return 0                        # result = 0
            
        else:                           # 4: flip symbol using rule 6                
            sign = sign * int(pow(-1, ((p-1)//2)*((q-1)//2)))
            swap = q
            q = p
            p = swap
                
def genNonresidue(p1, p2):
    """Generates x, a quadratic nonresidue of p1 and of p2."""

    x, a, b, = coprime(p1*p2), 0, 0
    
    while True:
        #xp1,xp2 = x%p1, x%p2
        #a = pow(x, (p1-1)//2, p1)
        #b = pow(x, (p2-1)//2, p2)
        a = jacobi(x,p1)
        b = jacobi(x,p2)

        if x < 2:
            1==1
        elif a == -1:                         # if x is a nonresidue of p1
            if b == -1:                     # if x is a nonresidue of p2
                return x
        x = coprime(p1*p2)
