import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):

    def test_no_of_triangle_valid_input(self):
        self.assertEqual(No_of_Triangle(5, 3), 6)
        self.assertEqual(No_of_Triangle(10, 5), 21)
        self.assertEqual(No_of_Triangle(20, 10), 70)

    def test_no_of_triangle_invalid_input(self):
        self.assertEqual(No_of_Triangle(2, 3), -1)
        self.assertEqual(No_of_Triangle(1, 1), -1)
        self.assertEqual(No_of_Triangle(0, 0), -1)
