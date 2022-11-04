# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
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

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    message = input()
    converted = char_to_ascii(message)
    print(converted)

