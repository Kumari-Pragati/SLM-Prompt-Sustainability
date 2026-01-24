import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):

    def test_simple_case(self):
        self.assertEqual(No_of_Triangle(3, 1), 3)
        self.assertEqual(No_of_Triangle(4, 2), 6)
        self.assertEqual(No_of_Triangle(5, 3), 10)

    def test_edge_case(self):
        self.assertEqual(No_of_Triangle(1, 1), -1)
        self.assertEqual(No_of_Triangle(0, 1), -1)
        self.assertEqual(No_of_Triangle(1, 0), -1)

    def test_boundary_case(self):
        self.assertEqual(No_of_Triangle(1, 2), 0)
        self.assertEqual(No_of_Triangle(2, 1), 1)
        self.assertEqual(No_of_Triangle(2, 2), 1)

    def test_complex_case(self):
        self.assertEqual(No_of_Triangle(6, 4), 15)
        self.assertEqual(No_of_Triangle(7, 5), 21)
        self.assertEqual(No_of_Triangle(8, 6), 28)
