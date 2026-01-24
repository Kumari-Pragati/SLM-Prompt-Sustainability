import unittest
from mbpp_621_code import increment_numerics

class TestIncrementNumerics(unittest.TestCase):
    def test_typical_use_case(self):
        test_list = ['1', '2', '3', 'a', 'b', 'c']
        expected_result = ['2', '3', '4', 'a', 'b', 'c']
        self.assertEqual(increment_numerics(test_list, 1), expected_result)

    def test_edge_case_zero(self):
        test_list = ['1', '2', '3', 'a', 'b', 'c']
        expected_result = ['1', '2', '3', 'a', 'b', 'c']
        self.assertEqual(increment_numerics(test_list, 0), test_list)

    def test_edge_case_negative(self):
        test_list = ['1', '2', '3', 'a', 'b', 'c']
        expected_result = ['0', '1', '2', 'a', 'b', 'c']
        self.assertEqual(increment_numerics(test_list, -1), expected_result)

    def test_invalid_input_non_integer(self):
        test_list = ['1', '2', '3', 'a', 'b', 'c']
        with self.assertRaises(TypeError):
            increment_numerics(test_list, 'K')
