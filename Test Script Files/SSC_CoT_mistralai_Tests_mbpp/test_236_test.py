import unittest
from mbpp_236_code import No_of_Triangle

class TestNo_of_Triangle(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(No_of_Triangle(5, 3), 6)
        self.assertEqual(No_of_Triangle(10, 5), 21)

    def test_edge_cases(self):
        self.assertEqual(No_of_Triangle(0, 0), -1)
        self.assertEqual(No_of_Triangle(1, 1), 0)
        self.assertEqual(No_of_Triangle(2, 2), 1)
        self.assertEqual(No_of_Triangle(3, 3), 3)

    def test_boundary_cases(self):
        self.assertEqual(No_of_Triangle(4, 1), 6)
        self.assertEqual(No_of_Triangle(5, 2), 10)
        self.assertEqual(No_of_Triangle(6, 3), 15)
        self.assertEqual(No_of_Triangle(7, 4), 21)

    def test_invalid_inputs(self):
        self.assertEqual(No_of_Triangle(-1, 1), -1)
        self.assertEqual(No_of_Triangle(1, -1), -1)
        self.assertEqual(No_of_Triangle(0, 0), -1)
        self.assertEqual(No_of_Triangle(1, 0), -1)
