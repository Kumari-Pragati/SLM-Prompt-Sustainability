import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):

    def test_simple_list(self):
        self.assertEqual(count_list([1, 2, 3]), 3)
        self.assertEqual(count_list([0, 0, 0]), 3)
        self.assertEqual(count_list([-1, 0, 1]), 3)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count_list([42]), 1)

    def test_large_list(self):
        large_list = [i for i in range(1000)]
        self.assertEqual(count_list(large_list), 1000)

    def test_list_with_duplicates(self):
        self.assertEqual(count_list([1, 1, 2, 2, 3, 3]), 6)
