import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Find_Min([3, 1, 2]), 1)

    def test_single_element(self):
        self.assertEqual(Find_Min([5]), 5)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            Find_Min([])

    def test_negative_numbers(self):
        self.assertEqual(Find_Min([-3, -1, -2]), -3)

    def test_duplicate_min(self):
        self.assertEqual(Find_Min([2, 1, 1]), 1)

    def test_mixed_numbers(self):
        self.assertEqual(Find_Min([3, -1, 2]), -1)

    def test_large_numbers(self):
        self.assertEqual(Find_Min([1000000, 2000000, 3000000]), 1000000)
