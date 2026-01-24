import unittest
from mbpp_105_code import count

class TestCountFunction(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 15)

    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count([5]), 5)

    def test_negative_numbers(self):
        self.assertEqual(count([-1, -2, -3]), -6)

    def test_mixed_numbers(self):
        self.assertEqual(count([1, -2, 3, -4, 5]), 3)

    def test_non_numeric_input(self):
        with self.assertRaises(TypeError):
            count(['a', 'b', 'c'])

    def test_non_list_input(self):
        with self.assertRaises(TypeError):
            count(123)
