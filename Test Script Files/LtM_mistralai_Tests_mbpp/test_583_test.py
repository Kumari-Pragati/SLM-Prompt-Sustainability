import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):
    def test_simple_input(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(catalan_number(-1), None)
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2**32), None)

    def test_complex_cases(self):
        self.assertEqual(catalan_number(5), 22)
        self.assertEqual(catalan_number(6), 62)
        self.assertEqual(catalan_number(7), 203)
        self.assertEqual(catalan_number(8), 668)
        self.assertEqual(catalan_number(9), 2205)
