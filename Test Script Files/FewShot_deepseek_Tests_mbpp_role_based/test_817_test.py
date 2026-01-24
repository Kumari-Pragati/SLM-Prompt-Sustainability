import unittest
from mbpp_817_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        m = 2
        n = 3
        expected_output = [2, 3, 4, 6, 8]
        self.assertEqual(div_of_nums(nums, m, n), expected_output)

    def test_edge_case_with_single_number(self):
        nums = [1]
        m = 2
        n = 3
        expected_output = []
        self.assertEqual(div_of_nums(nums, m, n), expected_output)

    def test_boundary_case_with_large_numbers(self):
        nums = list(range(1, 10001))
        m = 2
        n = 3
        self.assertTrue(div_of_nums(nums, m, n))

    def test_error_handling_with_invalid_input(self):
        nums = [1, 2, 3, 4, 5]
        m = 'a'
        n = 3
        with self.assertRaises(TypeError):
            div_of_nums(nums, m, n)
