import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):

    def test_simple_cases(self):
        self.assertEqual(neg_nos([1, -2, 3]), -2)
        self.assertEqual(neg_nos([-5, 4, -3]), -5)

    def test_edge_conditions(self):
        self.assertIsNone(neg_nos([]))
        self.assertIsNone(neg_nos([1, 2, 3]))
        self.assertEqual(neg_nos([0]), 0)

    def test_complex_cases(self):
        self.assertEqual(neg_nos([-1, -2, -3, 4]), -1)
        self.assertEqual(neg_nos([-1, 0, 1]), -1)
        self.assertIsNone(neg_nos([0, 0, 0]))
