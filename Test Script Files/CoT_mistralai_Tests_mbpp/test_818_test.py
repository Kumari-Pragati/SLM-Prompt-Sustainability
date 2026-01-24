import unittest
from mbpp_818_code import lower_ctr

class TestLowerCtr(unittest.TestCase):
    def test_empty_string(self):
        self.assertEqual(lower_ctr(''), 0)

    def test_single_letter(self):
        for char in 'abcdefghijklmnopqrstuvwxyz':
            self.assertEqual(lower_ctr(char), 1)

    def test_multiple_letters(self):
        self.assertEqual(lower_ctr('hello'), 5)
        self.assertEqual(lower_ctr('Hello'), 1)
        self.assertEqual(lower_ctr('123abc'), 3)
        self.assertEqual(lower_ctr('abc123'), 3)

    def test_mixed_case(self):
        self.assertEqual(lower_ctr('mIXeDcAsE'), 7)

    def test_no_letters(self):
        self.assertEqual(lower_ctr('1234567890'), 0)
        self.assertEqual(lower_ctr('!@#$%^&*()_+-=[]{}|;:'\'<>,.?/'), 0)
        self.assertEqual(lower_ctr('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 0)
        self.assertEqual(lower_ctr('ABC123'), 0)
        self.assertEqual(lower_ctr('123ABC'), 0)
