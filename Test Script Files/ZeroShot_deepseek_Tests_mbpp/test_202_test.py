import unittest
from mbpp_202_code import remove_even

class TestRemoveEven(unittest.TestCase):

    def test_remove_even(self):
        self.assertEqual(remove_even('abcdefg'), 'bdf')
        self.assertEqual(remove_even('1234567890'), '13579')
        self.assertEqual(remove_even(''), '')
        self.assertEqual(remove_even('a'), '')
        self.assertEqual(remove_even('1'), '1')
        self.assertEqual(remove_even('abc123'), 'b13')
