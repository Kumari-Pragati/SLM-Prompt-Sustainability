import unittest
from mbpp_309_code import maximum

class TestMaximum(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(maximum(5, 10), 10)

    def test_boundary_condition(self):
        self.assertEqual(maximum(0, 0), 0)

    def test_edge_condition(self):
        self.assertEqual(maximum(-10, -5), -5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            maximum("5", 10)
