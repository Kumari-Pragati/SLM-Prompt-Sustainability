import unittest
from mbpp_236_code import No_of_Triangle

class TestNoOfTriangle(unittest.TestCase):

    # Test for simple / typical inputs
    def test_typical_inputs(self):
        self.assertEqual(No_of_Triangle(5, 2), 6)
        self.assertEqual(No_of_Triangle(10, 3), 14)

    # Test for edge and boundary conditions
    def test_edge_conditions(self):
        self.assertEqual(No_of_Triangle(1, 1), -1)
        self.assertEqual(No_of_Triangle(0, 0), -1)
        self.assertEqual(No_of_Triangle(100, 50), 19950)

    # Test for more complex or corner cases
    def test_corner_cases(self):
        self.assertEqual(No_of_Triangle(10, 10), 1)
        self.assertEqual(No_of_Triangle(20, 10), 14)
