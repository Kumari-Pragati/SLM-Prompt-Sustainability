import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(left_insertion([], 5), 0)

    def test_single_element_list(self):
        self.assertEqual(left_insertion([5], 5), 0)
        self.assertEqual(left_insertion([5], 10), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 6), 5)
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 0), 0)

    def test_duplicates_in_list(self):
        self.assertEqual(left_insertion([1, 2, 2, 3, 4, 5], 2), 1)
        self.assertEqual(left_insertion([1, 2, 2, 3, 4, 5], 3), 3)

    def test_edge_cases(self):
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 5), 4)
