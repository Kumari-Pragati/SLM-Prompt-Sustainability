import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Find_Min([1, 2, 3, 4, 5]), 1)

    def test_empty_list(self):
        self.assertIsNone(Find_Min([]))

    def test_single_element_list(self):
        self.assertEqual(Find_Min([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(Find_Min([-1, -2, -3]), -3)

    def test_multiple_min_values(self):
        self.assertEqual(Find_Min([-1, 0, -1]), -1)
