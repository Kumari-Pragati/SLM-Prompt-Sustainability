import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):

    def test_binary_to_integer(self):
        self.assertEqual(binary_to_integer((1, 0, 1, 1)), '7')
        self.assertEqual(binary_to_integer((1, 0, 0, 0)), '8')
        self.assertEqual(binary_to_integer((1, 1, 1, 1)), '15')
        self.assertEqual(binary_to_integer((0, 0, 0, 0)), '0')
        self.assertEqual(binary_to_integer((1, 1, 0, 1)), '12')
