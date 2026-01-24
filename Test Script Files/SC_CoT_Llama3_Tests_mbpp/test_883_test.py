import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_typical_input(self):
        nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        m = 2
        n = 3
        expected_output = [30, 60, 90, 100]
        self.assertEqual(div_of_nums(nums, m, n), expected_output)

    def test_edge_case_m_equal_n(self):
        nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        m = 3
        n = 3
        expected_output = [30, 60, 90, 100]
        self.assertEqual(div_of_nums(nums, m, n), expected_output)

    def test_edge_case_m_divides_n(self):
        nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        m = 2
        n = 2
        expected_output = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        self.assertEqual(div_of_nums(nums, m, n), expected_output)

    def test_edge_case_m_and_n_divide_same(self):
        nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        m = 4
        n = 4
        expected_output = [40, 80, 100]
        self.assertEqual(div_of_nums(nums, m, n), expected_output)

    def test_invalid_input_type_m(self):
        nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        m = 'a'
        n = 3
        with self.assertRaises(TypeError):
            div_of_nums(nums, m, n)

    def test_invalid_input_type_n(self):
        nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
        m = 2
        n = 'b'
        with self.assertRaises(TypeError):
            div_of_nums(nums, m, n)
