import unittest
from mbpp_349_code import check

class TestCheckFunction(unittest.TestCase):

    def test_check_with_binary_string(self):
        self.assertEqual(check('0101'), 'Yes')
        self.assertEqual(check('1010'), 'Yes')
        self.assertEqual(check('0000'), 'Yes')
        self.assertEqual(check('1111'), 'Yes')

    def test_check_with_non_binary_string(self):
        self.assertEqual(check('0123'), 'No')
        self.assertEqual(check('101A'), 'No')
        self.assertEqual(check('ABCD'), 'No')
        self.assertEqual(check('1234'), 'No')

    def test_check_with_empty_string(self):
        self.assertEqual(check(''), 'Yes')

    def test_check_with_single_digit_string(self):
        self.assertEqual(check('0'), 'Yes')
        self.assertEqual(check('1'), 'Yes')
