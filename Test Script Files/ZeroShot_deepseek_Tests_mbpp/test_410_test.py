import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_min_val_with_integers(self):
        self.assertEqual(min_val([5, 3, 9, 1]), 1)
        self.assertEqual(min_val([-5, -3, -9, -1]), -9)
        self.assertEqual(min_val([0, 0, 0]), 0)

    def test_min_val_with_floats(self):
        self.assertEqual(min_val([5.5, 3.3, 9.9, 1.1]), 1.1)
        self.assertEqual(min_val([-5.5, -3.3, -9.9, -1.1]), -9.9)
        self.assertEqual(min_val([0.0, 0.0, 0.0]), 0.0)

    def test_min_val_with_mixed_types(self):
        self.assertEqual(min_val([5, 3, '9', 1]), 1)
        self.assertEqual(min_val([-5, -3, '-9', -1]), -9)
        self.assertEqual(min_val([0, 0, '0']), 0)

    def test_min_val_with_empty_list(self):
        self.assertIsNone(min_val([]))

    def test_min_val_with_non_integer_values(self):
        self.assertIsNone(min_val(['a', 'b', 'c']))
