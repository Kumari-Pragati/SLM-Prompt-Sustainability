import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(No_of_Triangle(3, 1), 3)
        self.assertEqual(No_of_Triangle(5, 2), 10)
        self.assertEqual(No_of_Triangle(8, 3), 28)

    def test_edge_cases(self):
        self.assertEqual(No_of_Triangle(0, 0), -1)
        self.assertEqual(No_of_Triangle(1, 0), -1)
        self.assertEqual(No_of_Triangle(1, 1), 0)

    def test_boundary_cases(self):
        self.assertEqual(No_of_Triangle(1, 2), 1)
        self.assertEqual(No_of_Triangle(2, 1), 1)
        self.assertEqual(No_of_Triangle(2, 2), 3)
