import unittest
from mbpp_294_code import max_val

class TestMaxVal(unittest.TestCase):

    def test_max_val_typical_case(self):
        self.assertEqual(max_val([1, 2, 3, 4, 5]), 5)

    def test_max_val_with_negative_numbers(self):
        self.assertEqual(max_val([-1, -2, -3, -4, -5]), -1)

    def test_max_val_with_mixed_numbers(self):
        self.assertEqual(max_val([-1, 2, -3, 4, -5]), 4)

    def test_max_val_with_non_integer_values(self):
        self.assertEqual(max_val([1, 2, 3, 4, '5']), 4)

    def test_max_val_with_empty_list(self):
        with self.assertRaises(ValueError):
            max_val([])

    def test_max_val_with_non_list_input(self):
        with self.assertRaises(TypeError):
            max_val("not a list")
