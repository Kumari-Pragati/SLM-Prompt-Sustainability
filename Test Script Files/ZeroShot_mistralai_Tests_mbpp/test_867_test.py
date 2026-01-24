import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):

    def test_min_num_empty_list(self):
        self.assertEqual(min_Num([], 0), 2)

    def test_min_num_single_odd_element(self):
        self.assertEqual(min_Num([1], 1), 1)

    def test_min_num_single_even_element(self):
        self.assertEqual(min_Num([2], 1), 2)

    def test_min_num_multiple_odd_elements(self):
        self.assertEqual(min_Num([1, 3, 5], 3), 1)

    def test_min_num_multiple_even_elements(self):
        self.assertEqual(min_Num([2, 4, 6], 3), 2)

    def test_min_num_mixed_elements(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 1)
