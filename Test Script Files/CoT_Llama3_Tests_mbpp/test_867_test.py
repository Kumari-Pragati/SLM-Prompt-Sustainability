import unittest
from mbpp_867_code import min_Num

class TestMin_Num(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 2)

    def test_odd_count_multiple_of_2(self):
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 1)

    def test_odd_count_single(self):
        self.assertEqual(min_Num([1], 1), 1)

    def test_even_count(self):
        self.assertEqual(min_Num([2, 4, 6, 8], 4), 2)

    def test_empty_array(self):
        self.assertEqual(min_Num([], 0), 2)

    def test_single_element_array(self):
        self.assertEqual(min_Num([2], 1), 2)

    def test_array_with_single_odd(self):
        self.assertEqual(min_Num([2, 1, 4, 6], 4), 2)

    def test_array_with_multiple_odd(self):
        self.assertEqual(min_Num([1, 3, 5, 7, 9, 2, 4, 6], 8), 1)
