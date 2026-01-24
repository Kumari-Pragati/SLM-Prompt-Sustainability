import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [10, 20, 30, 40, 50]
        m = 5
        n = 10
        self.assertEqual(div_of_nums(nums, m, n), [10, 20, 30, 40, 50])

    def test_edge_condition(self):
        nums = [0]
        m = 0
        n = 0
        self.assertEqual(div_of_nums(nums, m, n), [0])

    def test_boundary_condition(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 1
        n = 10
        self.assertEqual(div_of_nums(nums, m, n), [10])

    def test_invalid_input(self):
        nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        m = 'a'
        n = 10
        with self.assertRaises(TypeError):
            div_of_nums(nums, m, n)
