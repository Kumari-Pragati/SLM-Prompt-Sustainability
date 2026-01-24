import unittest
from mbpp_883_code import div_of_nums

class TestDivOfNums(unittest.TestCase):
    def test_divisible_by_both(self):
        self.assertListEqual(div_of_nums([10, 15, 20], 2, 5), [10, 20])

    def test_divisible_by_one(self):
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 2, 1), [2])
        self.assertListEqual(div_of_nums([1, 2, 3, 4, 5], 1, 2), [2])

    def test_empty_list(self):
        self.assertListEqual(div_of_nums([], 2, 5), [])

    def test_negative_numbers(self):
        self.assertListEqual(div_of_nums([-10, -5, -3], 2, 3), [-10])

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            div_of_nums(1, 2, "not_a_number")

    def test_invalid_input_2(self):
        with self.assertRaises(TypeError):
            div_of_nums([1, 2, 3], "not_a_number", 2)
