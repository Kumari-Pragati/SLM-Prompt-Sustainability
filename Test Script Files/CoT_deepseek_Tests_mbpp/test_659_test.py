import unittest
from mbpp_659_code import Repeat

class TestRepeatFunction(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Repeat([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]), [2, 4, 5])

    def test_empty_list(self):
        self.assertEqual(Repeat([]), [])

    def test_single_element_list(self):
        self.assertEqual(Repeat([1]), [])

    def test_all_repeated_elements(self):
        self.assertEqual(Repeat([1, 1, 1, 1]), [1])

    def test_no_repeated_elements(self):
        self.assertEqual(Repeat([1, 2, 3, 4]), [])

    def test_negative_numbers(self):
        self.assertEqual(Repeat([-1, -1, -2, -2]), [-1, -2])

    def test_mixed_numbers(self):
        self.assertEqual(Repeat([1, 'a', 'a', 2, 2]), ['a', 2])

    def test_repeated_string(self):
        self.assertEqual(Repeat(['a', 'a', 'b', 'b']), ['a', 'b'])

    def test_large_input(self):
        self.assertEqual(Repeat(list(range(1, 1001)) + [1000]), [1000])
