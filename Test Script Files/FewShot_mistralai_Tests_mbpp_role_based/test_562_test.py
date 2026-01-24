import unittest
from mbpp_562_code import Find_Max_Length

class TestFindMaxLength(unittest.TestCase):
    def test_positive_list(self):
        self.assertEqual(Find_Max_Length([1, 2, 3, 4, 5]), 1)
        self.assertEqual(Find_Max_Length(['abc', 'def', 'ghi']), 3)

    def test_empty_list(self):
        self.assertEqual(Find_Max_Length([]), 0)

    def test_single_element_list(self):
        self.assertEqual(Find_Max_Length(['a']), 1)

    def test_negative_list(self):
        self.assertEqual(Find_Max_Length([-1, -2, -3]), 3)

    def test_mixed_list(self):
        self.assertEqual(Find_Max_Length([1, 'a', 3, 'b']), 2)

    def test_list_with_zero(self):
        self.assertEqual(Find_Max_Length([0, 1, 2, 0]), 2)
