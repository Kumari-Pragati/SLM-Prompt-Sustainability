import unittest
from mbpp_258_code import count_odd

class TestCountOdd(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(count_odd([]), 0)

    def test_single_element(self):
        self.assertEqual(count_odd([1]), 1)

    def test_multiple_odd(self):
        self.assertEqual(count_odd([1, 3, 5, 7]), 4)

    def test_multiple_even(self):
        self.assertEqual(count_odd([2, 4, 6, 8]), 0)

    def test_mixed_elements(self):
        self.assertEqual(count_odd([1, 2, 3, 4, 5]), 3)

    def test_negative_numbers(self):
        self.assertEqual(count_odd([-1, -2, 3, 4, 5]), 3)

    def test_non_integer_elements(self):
        with self.assertRaises(TypeError):
            count_odd([1, 2, 'a', 4, 5])
