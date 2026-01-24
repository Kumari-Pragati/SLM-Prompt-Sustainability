import unittest
from mbpp_354_code import tn_ap

class TestTnAp(unittest.TestCase):

    def test_tn_ap(self):
        self.assertEqual(tn_ap(1, 5, 2), 9)
        self.assertEqual(tn_ap(2, 3, 1), 5)
        self.assertEqual(tn_ap(5, 2, 3), 11)
        self.assertEqual(tn_ap(10, 1, 5), 15)
        self.assertEqual(tn_ap(0, 5, 2), 2)

    def test_tn_ap_edge_cases(self):
        self.assertEqual(tn_ap(0, 0, 0), 0)
        self.assertEqual(tn_ap(1, 0, 0), 1)
        self.assertEqual(tn_ap(0, 1, 0), 0)
        self.assertEqual(tn_ap(0, 0, 1), 0)
