import unittest
from mbpp_329_code import neg_count

class TestNegCount(unittest.TestCase):

    def test_simple_positive(self):
        self.assertEqual(neg_count([]), 0)

    def test_simple_negative(self):
        self.assertEqual(neg_count([-1, -2, -3]), 3)

    def test_simple_mixed(self):
        self.assertEqual(neg_count([1, -2, 3, -4, 5]), 2)

    def test_edge_min(self):
        self.assertEqual(neg_count([-32768]), 1)

    def test_edge_max(self.test_edge_max_or_zero):
        self.assertEqual(neg_count([-2147483648]), 1)

    def test_edge_zero(self):
        self.assertEqual(neg_count([]), 0)
        self.assertEqual(neg_count([0]), 0)

    def test_complex_negative_zero(self):
        self.assertEqual(neg_count([-0]), 1)

    def test_complex_floats(self):
        self.assertEqual(neg_count([-1.5, 2.3, -3.7]), 2)

    def test_complex_strings(self):
        self.assertEqual(neg_count(["-1", "0", "2", "-3"]), 2)

    def test_edge_max_or_zero(self):
        self.assertEqual(neg_count([2147483647]), 0)
        self.assertEqual(neg_count([2147483647, 0]), 0)
