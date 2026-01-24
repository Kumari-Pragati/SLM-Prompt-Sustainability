import unittest
from mbpp_503_code import add_consecutive_nums

class TestAddConsecutiveNums(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(add_consecutive_nums([1, 2, 3, 4, 5]), [1, 1, 1, 1])

    def test_single_element(self):
        self.assertEqual(add_consecutive_nums([1]), [])

    def test_empty_list(self):
        self.assertEqual(add_consecutive_nums([]), [])

    def test_negative_numbers(self):
        self.assertEqual(add_consecutive_nums([-1, 0, 1]), [1, 1])

    def test_large_numbers(self):
        self.assertEqual(add_consecutive_nums([1000, 2000, 3000]), [1000, 1000])

    def test_zero_and_large_numbers(self):
        self.assertEqual(add_consecutive_nums([0, 1000, 2000]), [1000, 1000])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            add_consecutive_nums("1, 2, 3")

        with self.assertRaises(TypeError):
            add_consecutive_nums(123)

        with self.assertRaises(TypeError):
            add_consecutive_nums([1, "2", 3])

        with self.assertRaises(TypeError):
            add_consecutive_nums([1, None, 3])
