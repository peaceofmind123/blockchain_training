"""Breaks the caesar cipher using brute-force"""
import sys
from caesar import encrypt
def break_caesar(ciphertext):
    """
    Breaks the caesar cipher
    Params:
        ciphertext: The encrypted message
    Returns:
        plaintexts: An array of possible plaintexts
    """
    plaintexts = []
    for i in range(0,26):
        plaintexts.append(encrypt(ciphertext,i))
    return plaintexts


def main(text=None):
    if text is None:
        text = 'a quick brown fox jumps over the lazy dog'
    print(break_caesar(encrypt(text, 15)))
if __name__ == '__main__':
    try:
        main(sys.argv[1])
    except IndexError:
        main()