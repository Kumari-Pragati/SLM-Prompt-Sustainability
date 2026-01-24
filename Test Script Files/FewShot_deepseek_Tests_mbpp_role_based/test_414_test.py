import unittest
from mbpp_414_code import overlapping

class TestOverlapping(unittest.TestCase):
    def test_typical_case(self):
        list1 = [1, 2, 3, 4]
        list2 = [3, 4, 5, 6]
        self.assertEqual(overlapping(list1, list2), 1)

    def test_no_overlap(self):
        list1 = [1, 2, 3, 4]
        list2 = [5, 6, 7, 8]
        self.assertEqual(overlapping(list1, list2), 0)

    def test_empty_lists(self):
        list1 = []
        list2 = []
        self.assertEqual(overlapping(list1, list2), 0)

    def test_one_empty_list(self):
        list1 = [1, 2, 3, 4]
        list2 = []
        self.assertEqual(overlapping(list1, list2), 0)

    def test_duplicate_elements(self):
        list1 = [1, 2, 2, 4]
        list2 = [2, 3, 4, 5]
        self.assertEqual(overlapping(list1, list2), 1)

    def test_negative_numbers(self):
        list1 = [-1, -2, -3, -4]
        list2 = [-3, -4, -5, -6]
        self.assertEqual(overlapping(list1, list2), 1)

    def test_large_numbers(self):
        list1 = [1000, 2000, 3000, 4000]
        list2 = [3000, 4000, 5000, 6000]
        self.assertEqual(overlapping(list1, list2), 1)
