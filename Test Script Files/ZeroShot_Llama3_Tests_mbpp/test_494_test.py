import unittest
from mbpp_494_code import binary_to_integer

class TestBinaryToInteger(unittest.TestCase):
    def test_binary_to_integer(self):
        self.assertEqual(binary_to_integer((1,0,1)), '5')
        self.assertEqual(binary_to_integer((1,1,0,1)), '11')
        self.assertEqual(binary_to_integer((0,1,0,1)), '5')
        self.assertEqual(binary_to_integer((1,1,1,1)), '15')
        self.assertEqual(binary_to_integer((0,0,0,0)), '0')
        self.assertEqual(binary_to_integer((1,0,0,0)), '1')
        self.assertEqual(binary_to_integer((1,1,1,0)), '10')
        self.assertEqual(binary_to_integer((1,0,1,1)), '9')
        self.assertEqual(binary_to_integer((0,1,1,1)), '11')
        self.assertEqual(binary_to_integer((1,1,0,0)), '4')
