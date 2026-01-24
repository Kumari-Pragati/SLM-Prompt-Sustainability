import unittest
from mbpp_867_code import min_Num

class TestMinNum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(min_Num([]), 2)

    def test_single_odd_number(self):
        self.assertEqual(min_Num([1]), 1)

    def test_single_even_number(self):
        self.assertEqual(min_Num([2]), 2)

    def test_mixed_numbers(self):
        self.assertEqual(min_Num([1, 2, 3, 4, 5]), 1)

    def test_all_odd_numbers(self):
        self.assertEqual(min_Num([1, 3, 5, 7]), 1)

    def test_all_even_numbers(self):
        self.assertEqual(min_Num([2, 4, 6, 8]), 2)

    def test_edge_case_single_even_number(self):
        self.assertEqual(min_Num([0]), 2)

    def test_edge_case_single_odd_number(self):
        self.assertEqual(min_Num([1]), 1)

    def test_invalid_input_non_integer(self):
        with self.assertRaises(TypeError):
            min_Num("not_an_integer", 1)

    def test_invalid_input_negative_number(self):
        with self.assertRaises(ValueError):
            min_Num([-1, 0, 1], 3)
