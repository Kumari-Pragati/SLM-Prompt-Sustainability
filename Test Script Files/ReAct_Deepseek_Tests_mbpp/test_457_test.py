import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Min([3, 1, 2]), 1)

    def test_empty_list(self):
        self.assertIsNone(Find_Min([]))

    def test_single_element_list(self):
        self.assertEqual(Find_Min([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(Find_Min([-3, -1, -2]), -3)

    def test_duplicate_min_values(self):
        self.assertEqual(Find_Min([2, 1, 1]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(Find_Min([3, -1, 2]), -1)

    def test_large_numbers(self):
        self.assertEqual(Find_Min([1000000, 2000000, 3000000]), 1000000)
