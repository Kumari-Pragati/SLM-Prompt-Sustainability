import unittest
from mbpp_50_code import min_length_list

class TestMinLengthList(unittest.TestCase):

    def test_min_length_list(self):
        self.assertEqual(min_length_list([1, 2, 3, 4, 5]), (1, [1]))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), (1, [1]))
        self.assertEqual(min_length_list(['a', 'b', 'c', 'd', 'e']), (1, ['a']))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]), (1, [1]))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]), (1, [1]))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]), (1, [1]))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]), (1, [1]))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]), (1, [1]))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]), (1, [1]))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]), (1, [1]))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]), (1, [1]))
        self.assertEqual(min_length_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50]), (1, [1]))

    def test_min_length_list_empty(self):
        self.assertEqual(min_length_list([]), (0, []))

    def test_min_length_list_single_element(self):
        self.assertEqual(min_length_list([1]), (1, [1]))

    def test_min_length_list_single_element_list(self):
        self.assertEqual