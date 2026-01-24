import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 3
        expected = [1, 2, 3]
        self.assertEqual(small_nnum(list1, n), expected)

    def test_edge_case_n_zero(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 0
        expected = []
        self.assertEqual(small_nnum(list1, n), expected)

    def test_edge_case_n_equal_to_list_length(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 10
        expected = list1
        self.assertEqual(small_nnum(list1, n), expected)

    def test_invalid_input_non_integer_n(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 'three'
        with self.assertRaises(TypeError):
            small_nnum(list1, n)

    def test_invalid_input_non_list_input(self):
        list1 = 'not a list'
        n = 3
        with self.assertRaises(TypeError):
            small_nnum(list1, n)
