import sys
"""Encryption and decryption facility using the caesar cipher"""

def encrypt(plaintext, shift):
    """
    Encryption method using the caesar cipher
    Params:
        plaintext: The string to be encrypted
        shift: a number by which the alphabet will be shifted
    Returns:
        ciphertext: the encrypted string
    """
    key = []
    
    for char in plaintext.lower():
        if ord(char) not in range(ord('a'), ord('z')+1):
            key.append(char)
            continue
        char_val = ord(char)
        if shift >=0:
            char_val+= (shift % 26)
        else:
            char_val-= (-shift % 26)
        if char_val > ord('z'):
            char_val -= 26
        elif char_val < ord('a'):
            char_val += 26
        char_key = chr(char_val)
        key.append(char_key)
    
    return ''.join(key)

def decrypt(ciphertext, shift):
    """
    Decryption method using the caesar cipher
    Params:
        ciphertext: The text to be decrypted
        shift: the shift used to obtain the ciphertext from the plaintext
    Returns:
        plaintext: The decrypted text 
    """
    return encrypt(ciphertext, -shift)

def main(plaintext, shift):
    print(encrypt(plaintext, shift))

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])