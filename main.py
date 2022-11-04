# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import math
from Crypto.Util import number
from decimal import Decimal

#poached from clarence
def char_to_ascii(char):
    """
    Converts characters to ascii values
    """
    if(type(char) is str):
       return [ord(x) for x in char]
    else:
        return ord(char)

#poached from g4g
def gcd(a, h):
    temp = 0
    while(1):
        temp = a % h
        if (temp == 0):
            return h
        a = h
        h = temp

def rsa_keygeneration_1024bit(message):
    p = number.getPrime(512)
    q = number.getPrime(512)
    n = p*q #public key
    e = 2 #public key
    CTF = math.lcm((p-1),(q-1))

    while (e < CTF):
        if (gcd(e,CTF)==1):
            break
        else:
            e += 1

    # x*y == 1 (mod p)
    # d*e = 1(mod CTF)
    d = pow(e, -1, CTF)

    to_convert = message
    print("OG Message: ", to_convert)

    in_ascii = char_to_ascii(to_convert)
    print("In ascii: ", in_ascii)

    #Encryption
    encrypted_data = []
    for x in in_ascii:
        z = pow(x,e)
        z = math.fmod(z,n)
        encrypted_data.append(z)
    print(encrypted_data)

    #Decryption
    decrypted_data = []

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    message = input()
    rsa_keygeneration_1024bit(message)
    #converted = char_to_ascii(message)
    #print(converted)

