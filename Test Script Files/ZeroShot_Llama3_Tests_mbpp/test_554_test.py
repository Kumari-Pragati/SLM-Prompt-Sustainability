import unittest
from mbpp_554_code import Split

class TestSplitFunction(unittest.TestCase):

    def test_split_function(self):
        self.assertEqual(Split([1, 2, 3, 4, 5]), [1, 3, 5])
        self.assertEqual(Split([10, 20, 30, 40, 50]), [])
        self.assertEqual(Split([-1, -2, -3, -4, -5]), [-1, -3, -5])
        self.assertEqual(Split([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [1, 3, 5, 7, 9])
        self.assertEqual(Split([2, 4, 6, 8, 10]), [])

    def test_split_function_empty_list(self):
        self.assertEqual(Split([]), [])

    def test_split_function_single_element(self):
        self.assertEqual(Split([1]), [1])

    def test_split_function_all_even(self):
        self.assertEqual(Split([2, 4, 6, 8, 10]), [])
