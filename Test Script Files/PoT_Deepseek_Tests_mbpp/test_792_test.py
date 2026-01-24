import unittest
from mbpp_792_code import count_list

class TestCountList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_list([1, 2, 3, 4, 5]), 5)

    def test_empty_list(self):
        self.assertEqual(count_list([]), 0)

    def test_single_element(self):
        self.assertEqual(count_list([1]), 1)

    def test_large_list(self):
        self.assertEqual(count_list(list(range(1, 1001))), 1000)

    def test_duplicate_elements(self):
        self.assertEqual(count_list([1, 2, 2, 3, 4, 4, 5]), 7)

    def test_negative_numbers(self):
        self.assertEqual(count_list([-1, -2, -3, -4, -5]), 5)

    def test_mixed_types(self):
        self.assertEqual(count_list([1, 'two', 3.0, True, None]), 5)
