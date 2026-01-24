import unittest
from mbpp_583_code import catalan_number

class TestCatalanNumber(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(catalan_number(0), 1)
        self.assertEqual(catalan_number(1), 1)
        self.assertEqual(catalan_number(2), 2)
        self.assertEqual(catalan_number(3), 5)
        self.assertEqual(catalan_number(4), 14)

    def test_edge_cases(self):
        self.assertEqual(catalan_number(-1), 1)  # Negative number should be treated as 0
        self.assertEqual(catalan_number(10), 16796)  # Larger number should be handled correctly

    def test_boundary_cases(self):
        self.assertEqual(catalan_number(0), 1)  # Boundary case: 0
        self.assertEqual(catalan_number(1), 1)  # Boundary case: 1

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            catalan_number("5")  # Invalid input type
