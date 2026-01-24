import unittest
from mbpp_410_code import min_val

class TestMinVal(unittest.TestCase):

    def test_min_val(self):
        self.assertEqual(min_val([1, 2, 3, 4, 5]), 1)
        self.assertEqual(min_val([-1, -2, -3, -4, -5]), -5)
        self.assertEqual(min_val([1, 2, 3, 4, 5, 'a']), 1)
        self.assertEqual(min_val([-1, -2, -3, -4, -5, 'a']), -5)
        self.assertEqual(min_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 1)
        self.assertEqual(min_val([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10]), -10)
        self.assertEqual(min_val([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a']), 1)
        self.assertEqual(min_val([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10, 'a']), -10)
