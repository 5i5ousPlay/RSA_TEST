# RSA_TEST
RSA_Demo_Program
* Group 4 Demonstration Program for RSA Algorithm
* Program uses pycryptodome library. Use `pip install pycryptodome` in python virtual environment to install library. Or alternatively use `pip install -r requirements.txt`.
## Things to Note / About the Program

The program works by first getting two random 1024-bit primes for the `p` and `q` values needed for the RSA Algorithm using the `pycryptodome` library's `number.getPrime()` function. It is important to note that practical applications of the RSA Algorithm usually use primes that are approximately 1024-2048 bits long, with some other applications going up to 4096-bit primes. The general idea is that the larger the prime, the more difficult it is to decrypt. The downside however is that this also takes longer to compute the larger the prime is. 

The program then computes for `n = p*q` and then initially sets the value `e = 2`. The former is to get the modulus for the public and private keys, while the latter is set to 2 to set up the program to find a value such that `1 < e < Carmichael Totient Function[CTF]` and `gcd(e, CTF) == 1`. Another important thing to note is that although the original RSA Algorithm paper uses `Euler's Totient Function[ETF]: (p-1)*(q-1)`, computing for `d mod ETF` occasionally produces a number that is too big, hence why practical applications will use either ETF or `Carmichael Totient Function: lcm((p-1),(q-1))` which also works. For the sake of demonstration and avoiding overflow errors caused by this, the program uses CTF instead.

Upon computing for CTF, the program looks for `e` such that `1 < e < Carmichael Totient Function[CTF]` and `gcd(e, CTF) == 1`. The program then computes for `d = e^-1 mod CTF`
