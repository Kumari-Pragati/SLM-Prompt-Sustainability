import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):

    def test_count_list(self):
        self.assertEqual(count_list([1, 2, 3]), 9)
        self.assertEqual(count_list([1, 2, 3, 4]), 16)
        self.assertEqual(count_list([1, 2, 3, 4, 5]), 25)
        self.assertEqual(count_list([]), 0)
        self.assertEqual(count_list([1]), 1)
        self.assertEqual(count_list([1, 2]), 4)

    def test_count_list_negative(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)
        self.assertEqual(count_list([-1, -2, -3, -4]), 16)
        self.assertEqual(count_list([-1, -2, -3, -4, -5]), 25)
        self.assertEqual(count_list([-1]), 1)
        self.assertEqual(count_list([-1, -2]), 4)

    def test_count_list_mixed(self):
        self.assertEqual(count_list([1, -2, 3, -4]), 16)
        self.assertEqual(count_list([1, -2, 3, -4, 5]), 25)
        self.assertEqual(count_list([1, -2, 3, -4, 5, -6]), 25)
