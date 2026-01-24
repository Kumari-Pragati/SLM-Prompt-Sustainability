import unittest
from mbpp_134_code import check_last

class TestCheckLast(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 1), "ODD")

    def test_even_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4, 6], 5, 1), "EVEN")

    def test_odd_sum(self):
        self.assertEqual(check_last([1, 2, 3, 4, 7], 5, 1), "ODD")

    def test_boundary_case(self):
        self.assertEqual(check_last([], 0, 1), "EVEN")

    def test_single_element_array(self):
        self.assertEqual(check_last([5], 1, 1), "ODD")

    def test_large_array(self):
        self.assertEqual(check_last(list(range(1, 10001)), 10000, 1), "ODD")

    def test_p_not_equal_to_1(self):
        self.assertEqual(check_last([1, 2, 3, 4, 5], 5, 0), "EVEN")

    def test_invalid_p(self):
        with self.assertRaises(TypeError):
            check_last([1, 2, 3, 4, 5], 5, 'a')

    def test_invalid_n(self):
        with self.assertRaises(TypeError):
            check_last([1, 2, 3, 4, 5], 'a', 1)

    def test_invalid_arr(self):
        with self.assertRaises(TypeError):
            check_last('a', 1, 1)
