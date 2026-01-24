import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(No_of_Triangle(5, 3), 3)
        self.assertEqual(No_of_Triangle(10, 5), 21)
        self.assertEqual(No_of_Triangle(15, 7), 55)

    def test_zero(self):
        self.assertEqual(No_of_Triangle(0, 0), 0)

    def test_negative_numbers(self):
        self.assertEqual(No_of_Triangle(-1, 1), -1)
        self.assertEqual(No_of_Triangle(0, -1), -1)
        self.assertEqual(No_of_Triangle(-1, -1), -1)

    def test_edge_conditions(self):
        self.assertEqual(No_of_Triangle(1, 1), 0)
        self.assertEqual(No_of_Triangle(2, 1), 1)
        self.assertEqual(No_of_Triangle(3, 2), 3)
