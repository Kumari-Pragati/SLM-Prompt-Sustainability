import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_list([1, 2, 3]), 9)
        self.assertEqual(count_list([4, 5, 6]), 36)

    def test_edge_input(self):
        self.assertEqual(count_list([]), 0)
        self.assertEqual(count_list([0]), 1)

    def test_boundary_input(self):
        max_int = (2 ** 31) - 1
        self.assertEqual(count_list([max_int] * 100), 10000)

    def test_negative_input(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)

    def test_mixed_input(self):
        self.assertEqual(count_list([1, -2, 3, 0, 5]), 25)
