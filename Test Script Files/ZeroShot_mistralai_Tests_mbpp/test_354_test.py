import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):

    def test_tn_ap_with_positive_values(self):
        self.assertEqual(tn_ap(1, 5, 2), 11)
        self.assertEqual(tn_ap(3, 7, 4), 43)
        self.assertEqual(tn_ap(10, 15, 5), 105)

    def test_tn_ap_with_zero_value_for_n(self):
        self.assertEqual(tn_ap(2, 0, 3), 2)

    def test_tn_ap_with_negative_values(self):
        self.assertRaises(ValueError, tn_ap, -1, 5, 2)
        self.assertRaises(ValueError, tn_ap, 1, -5, 2)
        self.assertRaises(ValueError, tn_ap, 1, 5, -2)
