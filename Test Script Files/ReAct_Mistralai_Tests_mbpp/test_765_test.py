import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):

    def test_positive_integer(self):
        self.assertGreaterEqual(is_polite(1), 2)
        self.assertGreaterEqual(is_polite(10), 11)
        self.assertGreaterEqual(is_polite(100), 101)

    def test_zero(self):
        self.assertGreaterEqual(is_polite(0), 1)

    def test_negative_integer(self):
        self.assertGreaterEqual(is_polite(-1), 0)
        self.assertGreaterEqual(is_polite(-10), -9)
        self.assertGreaterEqual(is_polite(-100), -99)

    def test_float(self):
        self.assertGreaterEqual(is_polite(1.5), 3)
        self.assertGreaterEqual(is_polite(-1.5), 0)

    def test_edge_cases(self):
        self.assertGreaterEqual(is_polite(math.e), math.e + 1)
        self.assertGreaterEqual(is_polite(math.pi), math.ceil(math.pi) + 1)
