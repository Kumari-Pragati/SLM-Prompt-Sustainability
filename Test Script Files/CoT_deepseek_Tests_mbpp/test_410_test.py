import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(min_val([5, 3, 9, 1]), 1)

    def test_with_floats(self):
        self.assertEqual(min_val([5.5, 3.3, 9.9, 1.1]), 1.1)

    def test_with_mixed_types(self):
        self.assertEqual(min_val([5, '3', 9, 1]), 1)

    def test_with_negative_numbers(self):
        self.assertEqual(min_val([-5, -3, -9, -1]), -9)

    def test_with_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_with_single_element(self):
        self.assertEqual(min_val([5]), 5)

    def test_with_none_in_list(self):
        with self.assertRaises(TypeError):
            min_val([5, None, 9, 1])
