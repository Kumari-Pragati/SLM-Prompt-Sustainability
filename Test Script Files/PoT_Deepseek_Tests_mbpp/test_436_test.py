import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(neg_nos([1, -2, 3]), -2)
        self.assertEqual(neg_nos([-5, -10, -15]), -5)

    def test_edge_cases(self):
        self.assertIsNone(neg_nos([1, 2, 3]))
        self.assertIsNone(neg_nos([]))

    def test_corner_cases(self):
        self.assertIsNone(neg_nos([0]))
        self.assertEqual(neg_nos([-1]), -1)
