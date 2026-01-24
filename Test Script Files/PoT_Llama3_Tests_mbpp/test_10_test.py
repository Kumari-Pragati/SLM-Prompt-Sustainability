import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_edge_case_n_zero(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 0), [])

    def test_edge_case_n_equal_to_list_length(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_edge_case_negative_n(self):
        with self.assertRaises(ValueError):
            small_nnum([1, 2, 3, 4, 5], -1)

    def test_edge_case_non_integer_n(self):
        with self.assertRaises(TypeError):
            small_nnum([1, 2, 3, 4, 5], 'a')

    def test_edge_case_non_list_input(self):
        with self.assertRaises(TypeError):
            small_nnum('abc', 3)

    def test_edge_case_non_integer_list_elements(self):
        with self.assertRaises(TypeError):
            small_nnum([1.5, 2.5, 3.5, 4.5, 5.5], 3)
