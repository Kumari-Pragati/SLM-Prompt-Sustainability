import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):
    def test_only_zero_or_one(self):
        self.assertEqual(check('0'), 'Yes')
        self.assertEqual(check('1'), 'Yes')
        self.assertEqual(check('00000'), 'Yes')
        self.assertEqual(check('11111'), 'Yes')
        self.assertEqual(check('01010'), 'Yes')

    def test_only_zero(self):
        self.assertEqual(check(''), 'Yes')
        self.assertEqual(check('0000'), 'Yes')

    def test_only_one(self):
        self.assertEqual(check('1111'), 'Yes')
        self.assertEqual(check('1'), 'Yes')

    def test_mixed_zero_and_one(self):
        self.assertEqual(check('0101010101'), 'No')
        self.assertEqual(check('1010101010'), 'No')

    def test_other_characters(self):
        self.assertEqual(check('0123'), 'No')
        self.assertEqual(check('abc'), 'No')
        self.assertEqual(check('!@#'), 'No')
