import unittest
from mbpp_755_code import second_smallest

class TestSecondSmallest(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(second_smallest([1, 2, 3, 4, 5]), 2)
        self.assertEqual(second_smallest([-1, 0, 1, 2, 3]), 0)
        self.assertEqual(second_smallest([5, 3, 2, 1]), 3)

    def test_edge_case_single_item(self):
        self.assertIsNone(second_smallest([1]))

    def test_edge_case_two_identical_items(self):
        self.assertIsNone(second_smallest([1, 1]))

    def test_edge_case_unsorted_list(self):
        self.assertEqual(second_smallest([5, 3, 2, 1]), 3)
        self.assertEqual(second_smallest([3, 5, 2, 1]), 2)

    def test_corner_case_empty_list(self):
        self.assertIsNone(second_smallest([]))
