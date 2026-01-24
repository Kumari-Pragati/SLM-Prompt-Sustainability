import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):
    def test_simple_valid_inputs(self):
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(2), 5)
        self.assertEqual(is_nonagonal(3), 14)
        self.assertEqual(is_nonagonal(4), 28)
        self.assertEqual(is_nonagonal(5), 49)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(is_nonagonal(0), 0)
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(-1), None)
        self.assertEqual(is_nonagonal(0.5), None)

    def test_invalid_inputs(self):
        self.assertEqual(is_nonagonal(None), None)
        self.assertEqual(is_nonagonal('a'), None)
        self.assertEqual(is_nonagonal(-10), None)
