import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_list([1, 2, 3]), 9)
        self.assertEqual(count_list([0, 0, 0]), 1)
        self.assertEqual(count_list([4, 5, 6]), 36)

    def test_edge_case_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(count_list([0]), 1)
        self.assertEqual(count_list([1]), 1)
        self.assertEqual(count_list([-1]), 1)
