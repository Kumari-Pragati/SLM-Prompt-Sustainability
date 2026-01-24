import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(No_of_Triangle(10, 3), 6)

    def test_invalid_input1(self):
        self.assertEqual(No_of_Triangle(5, 10), -1)

    def test_invalid_input2(self):
        self.assertEqual(No_of_Triangle(10, 15), -1)

    def test_zero_input(self):
        self.assertEqual(No_of_Triangle(0, 0), 0)

    def test_negative_input(self):
        with self.assertRaises(TypeError):
            No_of_Triangle(-1, 1)

    def test_non_integer_input(self):
        with self.assertRaises(TypeError):
            No_of_Triangle('a', 1)
