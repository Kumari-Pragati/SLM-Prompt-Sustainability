import unittest
from mbpp_393_code import max_length_list

class TestMaxLengthList(unittest.TestCase):
    def test_positive_list(self):
        self.assertEqual(max_length_list([1, 2, 3, 4, 5]), (5, [1, 2, 3, 4, 5]))

    def test_empty_list(self):
        self.assertEqual(max_length_list([]), (0, []))

    def test_single_element_list(self):
        self.assertEqual(max_length_list([1]), (1, [1]))

    def test_mixed_length_list(self):
        self.assertEqual(max_length_list([1, 2, 3, 'four', 5]), (3, ['four']))

    def test_negative_list(self):
        self.assertEqual(max_length_list([-1, -2, -3, -4, -5]), (5, [-1, -2, -3, -4, -5]))
