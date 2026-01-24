import unittest
from mbpp_105_code import count

class TestCountFunction(unittest.TestCase):

    def test_count_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_count_single_element_list(self):
        self.assertEqual(count([1]), 1)

    def test_count_multiple_elements_list(self):
        self.assertEqual(count([1, 2, 3]), 6)

    def test_count_negative_numbers(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_count_mixed_positive_and_negative_numbers(self):
        self.assertEqual(count([1, -2, 3, -4]), 0)

    def test_count_non_numeric_elements(self):
        with self.assertRaises(TypeError):
            count(['a', 'b', 'c'])

    def test_count_mixed_types(self):
        with self.assertRaises(TypeError):
            count([1, 'a', 2, 'b'])
