import unittest
from mbpp_436_code import neg_nos

class TestNegNos(unittest.TestCase):

    def test_simple_positive(self):
        self.assertIsNone(neg_nos([1, 2, 3]))

    def test_simple_negative(self):
        self.assertEqual(neg_nos([-1, -2, -3]), -1)

    def test_single_negative(self):
        self.assertEqual(neg_nos([0, -1]), -1)

    def test_empty_list(self):
        self.assertIsNone(neg_nos([]))

    def test_min_value(self):
        self.assertEqual(neg_nos([-50, -49, -48]), -50)

    def test_max_value(self):
        self.assertEqual(neg_nos([-999999999, -1, 0]), -999999999)

    def test_mixed_list(self):
        self.assertEqual(neg_nos([-1, 0, 1, -2]), -1)
