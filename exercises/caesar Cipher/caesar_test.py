import unittest
from caesar import encrypt, decrypt

class TestCaesar(unittest.TestCase):
    def test_encrypt_works(self):
        plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
        ciphertext = 'DEFGHIJKLMNOPQRSTUVWXYZABC'.lower()
        
        ciphertext_o = encrypt(plaintext, 3)
        self.assertEqual(ciphertext, ciphertext_o)
    
    def test_decrypt_works(self):
        plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
        ciphertext = 'DEFGHIJKLMNOPQRSTUVWXYZABC'.lower()
        
        plaintext_o = decrypt(ciphertext, 3)
        self.assertEqual(plaintext, plaintext_o)
    
    def test_both_work_together(self):
        plaintext = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.lower()
        for i in range(1, 100):
            c_o = encrypt(plaintext, i)
            p_o = decrypt(c_o, i)
            self.assertEqual(plaintext, p_o)
        

if __name__ == '__main__':
    unittest.main()
