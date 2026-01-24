import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 4), 0)
        self.assertEqual(find_remainder([10, 20, 30], 3, 100), 0)

    def test_edge_conditions(self):
        self.assertEqual(find_remainder([], 0, 5), 0)
        self.assertEqual(find_remainder([1], 1, 1), 0)
        self.assertEqual(find_remainder([1, 2, 3, 4, 5], 5, 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 0), 0)
        self.assertEqual(find_remainder([1, 2, 3], 3, -1), -1)

    def test_complex_cases(self):
        self.assertEqual(find_remainder([1, 2, 3, 4, 5], 5, 2), 1)
        self.assertEqual(find_remainder([10, 20, 30, 40, 50], 5, 100), 0)
