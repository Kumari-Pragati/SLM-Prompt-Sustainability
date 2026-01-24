import unittest
from mbpp_419_code import round_and_sum

class TestRoundAndSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(round_and_sum([]), 0)

    def test_single_element_list(self):
        self.assertEqual(round_and_sum([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(round_and_sum([1, 2, 3]), 6)

    def test_list_with_negative_numbers(self):
        self.assertEqual(round_and_sum([-1, -2, -3]), -6)

    def test_list_with_decimal_numbers(self):
        self.assertEqual(round_and_sum([1.5, 2.5, 3.5]), 7.5)

    def test_list_with_mixed_types(self):
        with self.assertRaises(TypeError):
            round_and_sum([1, 'a', 3.5])

    def test_list_with_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            round_and_sum([1, 'a', 3.5, [4, 5]])

    def test_list_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            round_and_sum([1.5, 'a', 3.5])
