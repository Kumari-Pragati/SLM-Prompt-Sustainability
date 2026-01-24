import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):
    def test_typical_input(self):
        self.assertEqual(count_list([1, 2, 3]), 9)

    def test_edge_cases(self):
        self.assertEqual(count_list([]), 0)
        self.assertEqual(count_list([0]), 1)
        self.assertEqual(count_list([1, 0]), 1)
        self.assertEqual(count_list([1, 2, 0]), 4)

    def test_boundary_cases(self):
        self.assertEqual(count_list([1000000]), 1000000000)
        self.assertEqual(count_list([-1000000]), 1000000000)
