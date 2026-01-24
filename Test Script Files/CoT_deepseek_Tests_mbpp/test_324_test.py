import unittest
from mbpp_324_code import sum_of_alternates

class TestSumOfAlternates(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(sum_of_alternates((1, 2, 3, 4, 5)), ((9), (14)))

    def test_single_element(self):
        self.assertEqual(sum_of_alternates((1,)), ((1), (0)))

    def test_empty_tuple(self):
        self.assertEqual(sum_of_alternates(()), ((0), (0)))

    def test_negative_numbers(self):
        self.assertEqual(sum_of_alternates((-1, -2, -3, -4, -5)), ((-9), (-14)))

    def test_mixed_numbers(self):
        self.assertEqual(sum_of_alternates((1, -2, 3, -4, 5)), ((3), (7)))

    def test_float_numbers(self):
        self.assertEqual(sum_of_alternates((1.5, 2.5, 3.5, 4.5)), ((9.5), (14.5)))

    def test_string_elements(self):
        with self.assertRaises(TypeError):
            sum_of_alternates(('a', 'b', 'c', 'd'))

    def test_list_elements(self):
        with self.assertRaises(TypeError):
            sum_of_alternates([1, 2, 3, 4])

    def test_none_elements(self):
        with self.assertRaises(TypeError):
            sum_of_alternates((None, None, None))
