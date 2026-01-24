import unittest
from mbpp_236_code import No_of_Triangle

class TestNoOfTriangle(unittest.TestCase):

    def test_valid_input(self):
        self.assertEqual(No_of_Triangle(5, 2), 4)
        self.assertEqual(No_of_Triangle(10, 3), 14)
        self.assertEqual(No_of_Triangle(15, 4), 26)

    def test_invalid_input(self):
        self.assertEqual(No_of_Triangle(3, 4), -1)
        self.assertEqual(No_of_Triangle(7, 8), -1)
        self.assertEqual(No_of_Triangle(11, 12), -1)

    def test_edge_cases(self):
        self.assertEqual(No_of_Triangle(1, 1), 0)
        self.assertEqual(No_of_Triangle(2, 1), 1)
        self.assertEqual(No_of_Triangle(3, 1), 2)
