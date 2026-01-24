import unittest
from mbpp_615_code import average_tuple

class TestAverageTuple(unittest.TestCase):
    def test_typical_use_case(self):
        nums = [[1, 2, 3], [4, 5, 6]]
        self.assertEqual(average_tuple(nums), [2.5, 5.5])

    def test_empty_input(self):
        nums = []
        with self.assertRaises(ZeroDivisionError):
            average_tuple(nums)

    def test_single_element_input(self):
        nums = [[1, 2, 3]]
        self.assertEqual(average_tuple(nums), [2.0])

    def test_multiple_element_input(self):
        nums = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        self.assertEqual(average_tuple(nums), [2.0, 5.0, 8.0])

    def test_non_numeric_input(self):
        nums = [['a', 'b', 'c'], ['d', 'e', 'f']]
        with self.assertRaises(TypeError):
            average_tuple(nums)
