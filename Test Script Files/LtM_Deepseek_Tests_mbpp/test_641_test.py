import unittest
from mbpp_641_code import is_nonagonal

class TestIsNonagonal(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(is_nonagonal(1), 1)
        self.assertEqual(is_nonagonal(2), 10)
        self.assertEqual(is_nonagonal(3), 22)

    def test_edge_conditions(self):
        self.assertEqual(is_nonagonal(0), 0)
        self.assertEqual(is_nonagonal(-1), -1)

    def test_boundary_conditions(self):
        self.assertEqual(is_nonagonal(100), 3415)
        self.assertEqual(is_nonagonal(1000), 384655)

    def test_complex_cases(self):
        self.assertEqual(is_nonagonal(10000), 70497550)
