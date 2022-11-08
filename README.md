# RSA_TEST
## Group 4 RSA_Demo_Program
* Group 4 Demonstration Program for RSA Algorithm
* IMPORTANT: Program uses pycryptodome library. Use `pip install pycryptodome` in python virtual environment to install library. Or alternatively use `pip install -r requirements.txt`.
## Things to Note / About the Program

### Key Generation
The program works by first getting two random 1024-bit primes for the `p` and `q` values needed for the RSA Algorithm using the `pycryptodome` library's `number.getPrime()` function. It is important to note that practical applications of the RSA Algorithm usually use primes that are approximately 1024-2048 bits long, with some other applications going up to 4096-bit primes. The general idea is that the larger the prime, the more difficult it is to decrypt. The downside however is that this also takes longer to compute the larger the prime is. 

The program then computes for `n = p*q` and then initially sets the value `e = 2`. The former is to get the modulus for the public and private keys, while the latter is set to 2 to set up the program to find a value such that `1 < e < Carmichael Totient Function[CTF]` and `gcd(e, CTF) == 1`. Another important thing to note is that although the original RSA Algorithm paper uses `Euler's Totient Function[ETF]: (p-1)*(q-1)`, computing for `d (mod ETF)` occasionally produces a number that is too big, hence why practical applications will use either ETF or `Carmichael Totient Function: lcm((p-1),(q-1))` which also works. For the sake of demonstration and avoiding overflow errors that may be caused by this, the program uses CTF instead.

Upon computing for CTF, the program looks for `e` such that `1 < e < Carmichael Totient Function[CTF]` and `gcd(e, CTF) == 1`. The program then computes for `d = e^-1 (mod CTF)` through `d = pow(e, -1, CTF)`. Note that `lcm()`, `gcd()`, and `pow()` functions used in the program are imported from python's `math` library for the sake of brevity and for the lattermost in order to also avoid overflow errors caused by the exponentiation of really large numbers.

### Encryption
Having completed these preliminary tasks for key generation, the program will then proceed to start encrypting the message. The program first converts the letters of the user inputted string into a list of numerical ascii values using the helper function `char_to_ascii`. To show this step the program prints both the original message and the subsequent ascii conversion.
```
Input:Hello
Original Message:  Hello
In ascii:  [72, 101, 108, 108, 111]
```
Following this, the program will then start encrypting each value in the `In ascii: []` list using the formula `c = m^e (mod n)` where `c` is the resulting encrypted character, `m` is the ascii representation of the original character. The program then proceeds to show this step by printing the resulting encrypted list of values.
```
Encrypted Data:  [373248, 1030301, 1259712, 1259712, 1367631]
```
#### Small Tangent || Encrypted to Ascii
Originally, the program would then convert the encrypted values in this list back to ascii without decrypting as a way to show that the encrypted message would now be unreadable if converted back to text. However, this ran into the problem where the number that would get passed to the helper function `ascii_to_char()` was too big to have an equivalent ascii representation. Hence, this code has been commented out from the program. However, if you wish to see just for the sake of it, you can choose to uncomment the section of code,
```
# encrypted_ascii = ascii_to_char(encrypted_data)
# encrypted_ascii = ''.join(encrypted_ascii)
# print("Encrypted Ascii: ", encrypted_ascii)
```
and change the values passed to `p` and `q` from 1024-bit primes to 10-bit primes like so.
```
p = number.getPrime(10)
q = number.getPrime(10)
```
### Decryption
To decrypt the data, the program will then proceed to decrypt each value in the `Encrypted Data: []` list using the formula `c^d = m (mod n)`. To compute for `m` the program manipulates this formula via the symmetric property whereby `m = c^d (mod n)`. To show this step the program prints the list of decrypted values which should be equal to and ordered the same way as the values in the `In ascii: []` list earlier. 
```
In ascii:  [72, 101, 108, 108, 111]
Decrypted Data:  [72, 101, 108, 108, 111]
```
The final step is simply the reverse of the initial step whereby the values within the `Decrypted Data: []` list are passed to the helper function `ascii_to_char()` which converts the list back into a string. The program then proceeds to print the decrypted string which should be the same as the `Original Message: `
```
Original Message:  Hello
Decrypted Message: Hello
```
The full terminal output should look something like this.
```
Original Message:  Hello
In ascii:  [72, 101, 108, 108, 111]
Encrypted Data:  [373248, 1030301, 1259712, 1259712, 1367631]
Decrypted Data:  [72, 101, 108, 108, 111]
Decrypted Message: Hello
```
### Exiting the Program
To exit the program simply input `EXIT`. 
## Members
* Conanan
* Geraldo
* Monterozo
* Tarrazona
* Tomazar 
