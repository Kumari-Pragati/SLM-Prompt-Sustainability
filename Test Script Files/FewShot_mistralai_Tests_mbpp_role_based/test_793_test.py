import unittest
from mbpp_793_code import last

class TestLast(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(last([], 5, 0), -1)

    def test_single_element(self):
        self.assertEqual(last([5], 5, 0), 0)

    def test_middle_element(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 3, 4), 2)

    def test_first_element(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 1, 4), 0)

    def test_last_element(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 5, 4), 4)

    def test_element_not_found(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 6, 4), -1)

    def test_negative_index(self):
        self.assertEqual(last([1, 2, 3, 4, 5], 3, -1), -1)

    def test_negative_number(self):
        self.assertEqual(last([1, 2, 3, 4, 5], -1, 4), -1)
