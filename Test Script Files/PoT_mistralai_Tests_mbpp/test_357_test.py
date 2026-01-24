import unittest
from mbpp_357_code import find_max

class TestFindMax(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_max([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 9)
        self.assertEqual(find_max([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]]), -9)
        self.assertEqual(find_max([[0, 0, 0], [0, 0, 0], [0, 0, 0]]), 0)

    def test_edge_case_empty_list(self):
        self.assertIsNone(find_max([]))

    def test_edge_case_single_element(self):
        self.assertEqual(find_max([[1]]), 1)
        self.assertEqual(find_max([[-1]]), -1)

    def test_edge_case_single_integer(self):
        self.assertEqual(find_max([1]), 1)
        self.assertEqual(find_max([-1]), -1)
