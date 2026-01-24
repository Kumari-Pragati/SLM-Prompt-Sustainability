import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_list([]), 0)
        self.assertEqual(count_list([1, 2, 3]), 3)
        self.assertEqual(count_list([0, 0, 0]), 3)
        self.assertEqual(count_list([1, 0, 1, 0, 1]), 4)

    def test_edge_case(self):
        self.assertEqual(count_list([None]), 1)
        self.assertEqual(count_list([1, None, 2]), 3)
        self.assertEqual(count_list([None, None, None]), 3)

    def test_boundary_case(self):
        self.assertEqual(count_list([-100]), 1)
        self.assertEqual(count_list([100]), 1)
        self.assertEqual(count_list([-100, -1, 0, 1, 100]), 5)
