# prob-cryptosystem

An implementation of a probabilistic cryptosystem.
written for Python 3.6 by Z. Henderson

CREDITS:

Algorithms and math from
- "Probabilistic encryption and how to play mental poker keeping
  secret all partial information" (1982) by Goldwasser and Micali
- Wikipedia

LICENSE:

To be frank, I don't understand how to correctly license this.
Just don't go calling this your work and we're cool.

If you do know how I should license this, @ me on Twitter:
@zzhenders

DESCRIPTION:

*** please note, this was done purely to learn how encryption works
*** and to practice Python. I cannot guarentee that it is actually
*** secure, so please do not use it to encrypt anything sensitive!

1) Run prob-keygen.py to generate private & public keys.

2) The contents of the text file 'message' will be encrypted.
  Change the text within it if you so desire, but note that long
  text will create an increasingly long ciphertext and a more
  time-costly en/decryption process.

3) Run prob-encryption.py in the same folder as 'message' and the
  'publicKey' text file. This will generate 'ciphertext'.
  
4) Run prob-decryption.py in the same folder as 'ciphertext' and
  the 'privateKey' text file. This will generate 'plaintext'.

