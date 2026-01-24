import unittest
from mbpp_232_code import larg_nnum

class TestLargNnum(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 3
        expected_result = [9, 8, 7]
        self.assertEqual(larg_nnum(list1, n), expected_result)

    def test_edge_case_n_equal_to_list_length(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 10
        expected_result = list1
        self.assertEqual(larg_nnum(list1, n), expected_result)

    def test_edge_case_n_greater_than_list_length(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 15
        expected_result = list1
        self.assertEqual(larg_nnum(list1, n), expected_result)

    def test_invalid_input_non_integer_n(self):
        list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        n = 'a'
        with self.assertRaises(TypeError):
            larg_nnum(list1, n)

    def test_invalid_input_non_list_list1(self):
        list1 = 'abc'
        n = 3
        with self.assertRaises(TypeError):
            larg_nnum(list1, n)
