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

def ascii_to_char(ascii):
    """
    Converts ascii characters to characters
    """
    if(type(ascii) is list):
       return [chr(x) for x in ascii]
    else:
        return chr(ascii)

#poached from g4g
#def gcd(a, h):
    #temp = 0
    #while(1):
        #temp = a % h
        #if (temp == 0):
            #return h
        #a = h
        #h = temp

def rsa_keygeneration_6bit(message):
    p = number.getPrime(6)
    q = number.getPrime(6)
    n = p*q #public key
    e = 2 #public key
    CTF = math.lcm((p-1),(q-1))

    while (e < CTF):
        if (math.gcd(e,CTF)==1):
            break
        else:
            e = e + 1

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
        c = pow(x,e,n)
        encrypted_data.append(c)
    print("Encrypted Data: ", encrypted_data)
    encrypted_ascii = ascii_to_char(encrypted_data)
    encrypted_ascii = ''.join(encrypted_ascii)
    print("Encrypted Ascii: ", encrypted_ascii)

    #Decryption
    decrypted_data = []
    for x in encrypted_data:
        m = pow(x,d,n)
        decrypted_data.append(m)
    print("Decrypted Data: ", decrypted_data)

    decrypted_ascii = ascii_to_char(decrypted_data)
    decrypted_ascii = ''.join(decrypted_ascii)
    print("Decrypted Message:" , decrypted_ascii)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    message = input()
    rsa_keygeneration_6bit(message)
    #converted = char_to_ascii(message)
    #print(converted)

