import unittest
from mbpp_659_code import Repeat

class TestRepeat(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(Repeat([1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]), [2, 4, 5])

    def test_empty_list(self):
        self.assertEqual(Repeat([]), [])

    def test_list_with_single_element(self):
        self.assertEqual(Repeat([1]), [])

    def test_all_repeated_elements(self):
        self.assertEqual(Repeat([1, 1, 1, 1]), [1])

    def test_no_repeated_elements(self):
        self.assertEqual(Repeat([1, 2, 3, 4]), [])

    def test_negative_numbers(self):
        self.assertEqual(Repeat([-1, -1, -2, -2]), [-1, -2])

    def test_mixed_numbers(self):
        self.assertEqual(Repeat([1, -1, 2, -2, 2, -2]), [2, -2])

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            Repeat(['a', 'b', 'b'])

    def test_none_elements(self):
        with self.assertRaises(TypeError):
            Repeat([None, None, None])
