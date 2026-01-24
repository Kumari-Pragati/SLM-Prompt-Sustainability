import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):

    def test_neg_nos(self):
        self.assertEqual(neg_nos([1, -2, 3, -4]), -2)
        self.assertEqual(neg_nos([1, 2, 3, -4]), -4)
        self.assertEqual(neg_nos([1, 2, 3, 4]), None)
        self.assertEqual(neg_nos([]), None)
        self.assertEqual(neg_nos([-1, -2, -3, -4]), -1)
