import unittest
from mbpp_116_code import tuple_to_int

class TestTupleToInt(unittest.TestCase):

    def test_empty_tuple(self):
        self.assertEqual(tuple_to_int(()), 0)

    def test_single_element_tuple(self):
        for num in range(-10, 10):
            self.assertEqual(tuple_to_int((num,)), num)

    def test_multiple_elements_tuple(self):
        for num1, num2 in zip(range(-10, 10), range(-10, 10)):
            self.assertEqual(tuple_to_int((num1, num2)), num1 * 10 + num2)

    def test_large_tuple(self):
        large_tuple = tuple(range(1000))
        self.assertLess(abs(tuple_to_int(large_tuple) - sum(large_tuple)), 1e6)

    def test_negative_numbers_in_tuple(self):
        for nums in [(-1, 2), (-1, -2), (-1, 0), (0, -1), (-10, -20)]:
            self.assertEqual(tuple_to_int(nums), sum(nums))

    def test_zero_in_tuple(self):
        for nums in [(0,), (0, 1), (1, 0), (0, 0)]:
            self.assertEqual(tuple_to_int(nums), sum(nums))

    def test_mixed_signs_in_tuple(self):
        for nums in [(1, -2, 3), (-1, 2, -3), (1, -2, 0), (0, 1, -2)]:
            self.assertEqual(tuple_to_int(nums), sum(nums))

    def test_tuple_with_non_integer_elements(self):
        with self.assertRaises(TypeError):
            tuple_to_int((1.0, 2))

    def test_tuple_with_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            tuple_to_int(('a', 2))
