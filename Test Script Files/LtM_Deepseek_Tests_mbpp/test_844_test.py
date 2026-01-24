import unittest
from mbpp_844_code import get_Number

class TestGetNumber(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(get_Number(5, 1), 1)
        self.assertEqual(get_Number(5, 3), 5)
        self.assertEqual(get_Number(10, 5), 9)

    def test_edge_conditions(self):
        self.assertEqual(get_Number(1, 1), 1)
        self.assertEqual(get_Number(2, 2), 2)
        self.assertEqual(get_Number(10, 10), 10)

    def test_boundary_conditions(self):
        self.assertEqual(get_Number(10, 1), 1)
        self.assertEqual(get_Number(10, 10), 10)

    def test_complex_cases(self):
        self.assertEqual(get_Number(15, 8), 13)
        self.assertEqual(get_Number(20, 15), 19)
