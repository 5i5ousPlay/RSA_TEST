"""
IMPORTANT: Program uses pycryptodome library.
Use "pip install pycryptodome" or alternatively
"pip install -r requirements.txt" in your python
virtual environment.

This is Group 4's Demo Program for RSA Algorithm

"""

import math
from Crypto.Util import number

def char_to_ascii(char):
    """
    Converts characters to ascii values
    """
    if(type(char) is str):
       return [ord(x) for x in char]
    else:
        return ord(char)

def ascii_to_char(ascii):
    """
    Converts ascii characters to characters
    """
    if(type(ascii) is list):
       return [chr(x) for x in ascii]
    else:
        return chr(ascii)

def rsa_keygeneration_10bit(message):
    """
    RSA Encryption normally uses primes that are
    around 1024-2048 bits long. However, for the sake
    of demonstration (and to avoid overflow errors),
    this program uses 10-bit primes.
    """
    p = number.getPrime(10)
    q = number.getPrime(10)
    n = p*q
    e = 2

    """
    NOTE:
    Original RSA paper uses the Euler Totient Function below:
    
    ETF = (p-1)*(q-1)
    
    However computing for d (mod ETF) occasionally 
    gives a number that is too big. Thus, for the sake of functionality 
    this program uses the Carmichael Totient Function. This will still 
    provide the correct encryption and decryption of data. Most real life
    implementations of RSA use either. 
    """
    CTF = math.lcm((p-1),(q-1))

    # finds integer 'e' such that 1<e<CTF
    while (e < CTF):
        if (math.gcd(e,CTF)==1):
            break
        else:
            e = e + 1


    # finds d*e = 1(mod CTF)
    d = pow(e, -1, CTF)

    to_convert = message
    print("Original Message: ", to_convert)

    # converts message into a list of numerical ascii values that can be encrypted using RSA
    in_ascii = char_to_ascii(to_convert)
    print("In ascii: ", in_ascii)

    # Encryption
    encrypted_data = []
    for x in in_ascii:
        c = pow(x,e,n)
        encrypted_data.append(c)
    print("Encrypted Data: ", encrypted_data)

    # shows the ascii conversion of encrypted data
    # made to be unreadable
    encrypted_ascii = ascii_to_char(encrypted_data)
    encrypted_ascii = ''.join(encrypted_ascii)
    print("Encrypted Ascii: ", encrypted_ascii)

    # Decryption
    decrypted_data = []
    for x in encrypted_data:
        m = pow(x,d,n)
        decrypted_data.append(m)
    print("Decrypted Data: ", decrypted_data)

    # shows the decrypted data's numerical values
    # should be the same values as the original converted ascii letters
    # converts back to ascii and prints the original message that was encrypted
    decrypted_ascii = ascii_to_char(decrypted_data)
    decrypted_ascii = ''.join(decrypted_ascii)
    print("Decrypted Message:" , decrypted_ascii)

if __name__ == '__main__':
    while True:
        print("\n----BASIC-RSA-ALGORITHM-DEMONSTRATION----")
        print("Please input your message for encryption\nOr input 'EXIT' to stop the program")
        message = input('Input:')
        if message == 'EXIT':
            break
        else:
            rsa_keygeneration_10bit(message)