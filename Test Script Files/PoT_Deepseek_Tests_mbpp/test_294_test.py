import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_single_element(self):
        self.assertEqual(max_val([1]), 1)

    def test_negative_numbers(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_val([-1, 0, 1]), 1)

    def test_float_numbers(self):
        self.assertEqual(max_val([1.1, 1.2, 1.3]), 1.3)

    def test_mixed_types(self):
        self.assertEqual(max_val([1, '2', 3]), 3)

    def test_empty_list(self):
        with self.assertRaises(ValueError):
            max_val([])

    def test_non_integer_elements(self):
        self.assertEqual(max_val(['1', '2', '3']), '3')

    def test_none_elements(self):
        with self.assertRaises(TypeError):
            max_val([None])
