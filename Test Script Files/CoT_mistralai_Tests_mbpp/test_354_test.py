import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(tn_ap(1, 3, 2), 7)
        self.assertEqual(tn_ap(5, 4, 3), 23)
        self.assertEqual(tn_ap(10, 6, 5), 71)

    def test_zero_and_negative_numbers(self):
        self.assertEqual(tn_ap(0, 3, 2), 2)
        self.assertEqual(tn_ap(-1, 3, 2), -5)
        self.assertEqual(tn_ap(0, 0, 1), 0)

    def test_invalid_inputs(self):
        self.assertRaises(TypeError, tn_ap, 'a', 3, 2)
        self.assertRaises(TypeError, tn_ap, 1, 'n', 2)
        self.assertRaises(TypeError, tn_ap, 1, 3, 'd')
        self.assertRaises(ValueError, tn_ap, -1, 0, 2)
        self.assertRaises(ValueError, tn_ap, 1, -1, 2)
        self.assertRaises(ValueError, tn_ap, 1, 0, 0)
