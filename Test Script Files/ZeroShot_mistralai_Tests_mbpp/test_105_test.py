import unittest
from mbpp_105_code import List

from 105_code import count

class TestCountFunction(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count([]), 0)

    def test_single_element_list(self):
        self.assertEqual(count([1]), 1)

    def test_multiple_elements_list(self):
        self.assertEqual(count([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(count([1, -2, 3, -4, 5]), 9)

    def test_list_with_floats(self):
        self.assertAlmostEqual(count([1.1, 2.2, 3.3]), 6.6)

    def test_list_with_strings(self):
        self.assertEqual(count(['1', '2', '3', '4', '5']), 15)

    def test_list_with_mixed_types(self):
        self.assertEqual(count([1, '2', 3, '4', 5]), 9)
