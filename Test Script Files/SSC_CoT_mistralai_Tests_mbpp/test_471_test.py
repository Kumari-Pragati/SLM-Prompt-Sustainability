import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 5), 3)
        self.assertEqual(find_remainder([4, 5, 6], 3, 7), 4)

    def test_edge_cases(self):
        self.assertEqual(find_remainder([], 0, 2), 1)
        self.assertEqual(find_remainder([1], 1, 2), 1)
        self.assertEqual(find_remainder([1, 2], 2, 1), 0)

    def test_boundary_conditions(self):
        self.assertEqual(find_remainder([0, 1, 2], 3, 5), 0)
        self.assertEqual(find_remainder([1000000000, 2, 3], 3, 5), 2)

    def test_negative_inputs(self):
        self.assertRaises(ValueError, find_remainder, [], 0, -1)
        self.assertRaises(ValueError, find_remainder, [1], 1, -1)
        self.assertRaises(ValueError, find_remainder, [1, 2], 2, -1)
