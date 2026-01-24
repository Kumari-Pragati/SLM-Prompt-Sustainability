import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):
    def test_normal_inputs(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)
        self.assertEqual(catalan_number(5), 42)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(catalan_number(-1), None)
        self.assertEqual(catalan_number(0.5), None)
        self.assertEqual(catalan_number(6), 91)
        self.assertEqual(catalan_number(7), 364)
        self.assertEqual(catalan_number(8), 1490)
        self.assertEqual(catalan_number(9), 5478)
        self.assertEqual(catalan_number(10), 21164)
