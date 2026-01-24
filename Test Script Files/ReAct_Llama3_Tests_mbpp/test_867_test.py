import unittest
from mbpp_867_code import min_Num

class TestMin_Num(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5], 5), 2)

    def test_odd_count_multiple(self):
        self.assertEqual(min_Num([1, 3, 5, 7, 9], 5), 1)

    def test_odd_count_single(self):
        self.assertEqual(min_Num([1], 1), 1)

    def test_even_count_multiple(self):
        self.assertEqual(min_Num([2, 4, 6, 8, 10], 5), 2)

    def test_even_count_single(self):
        self.assertEqual(min_Num([2], 1), 2)

    def test_empty_array(self):
        self.assertEqual(min_Num([], 0), 2)

    def test_array_with_one_element(self):
        self.assertEqual(min_Num([5], 1), 2)

    def test_array_with_no_elements(self):
        self.assertEqual(min_Num([], 0), 2)
