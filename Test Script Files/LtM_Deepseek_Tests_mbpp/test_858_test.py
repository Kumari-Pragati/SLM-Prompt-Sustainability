import unittest
from mbpp_858_code import count_list

class TestCountList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(count_list([1, 2, 3]), 9)

    def test_empty_input(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_input(self):
        self.assertEqual(count_list([1]), 1)

    def test_large_input(self):
        self.assertEqual(count_list(list(range(1000))), 1000000)

    def test_negative_input(self):
        self.assertEqual(count_list([-1, -2, -3]), 9)

    def test_mixed_input(self):
        self.assertEqual(count_list([1, 'a', None]), 9)
