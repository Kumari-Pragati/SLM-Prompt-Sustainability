import unittest
from mbpp_471_code import find_remainder

class TestFindRemainder(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_remainder([1, 2, 3], 3, 5), 3)
        self.assertEqual(find_remainder([4, 5, 6], 3, 7), 6)

    def test_edge_and_boundary(self):
        self.assertEqual(find_remainder([], 0, 5), 1)
        self.assertEqual(find_remainder([0], 1, 5), 0)
        self.assertEqual(find_remainder([1, 2, 3, 4, 5], 5, 2), 1)
        self.assertEqual(find_remainder([6, 7, 8], 3, 3), 0)

    def test_complex(self):
        self.assertEqual(find_remainder([-1, 0, 1], 3, 5), 1)
        self.assertEqual(find_remainder([1000000001, 1000000002, 1000000003], 1000000007, 1000000007), 1)
