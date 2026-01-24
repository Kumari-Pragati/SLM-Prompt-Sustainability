import unittest
from mbpp_793_code import last

class TestLastFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(last([], 10, 0), -1)

    def test_single_element(self):
        self.assertEqual(last([10], 10, 0), 0)
        self.assertEqual(last([10], 5, 0), -1)

    def test_multiple_elements(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 3, 4), 3)
        self.assertEqual(last([1, 2, 3, 4, 5], 6, 4), -1)
        self.assertEqual(last([1, 2, 3, 4, 5], 1, 0), -1)

    def test_duplicates(self):
        self.assertEqual(last([1, 1, 2, 3, 4, 4, 5], 4, 6), 4)
        self.assertEqual(last([1, 1, 2, 3, 4, 4, 5], 6, 6), 5)

    def test_negative_numbers(self):
        self.assertEqual(last([-1, -2, -3, -4, -5], -3, 4), 3)
        self.assertEqual(last([-1, -2, -3, -4, -5], -6, 4), -1)

    def test_large_numbers(self):
        self.assertEqual(last([1000000001, 1000000002, 1000000003, 1000000004, 1000000005], 1000000005, 4), 4)
        self.assertEqual(last([1000000001, 1000000002, 1000000003, 1000000004, 1000000005], 1000000006, 4), -1)
