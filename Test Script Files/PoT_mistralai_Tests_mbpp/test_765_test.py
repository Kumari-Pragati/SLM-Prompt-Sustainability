import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(is_polite(1), 3)
        self.assertEqual(is_polite(2), 4)
        self.assertEqual(is_polite(10), 12)
        self.assertEqual(is_polite(100), 102)
        self.assertEqual(is_polite(1000), 1002)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(is_polite(0), 1)
        self.assertEqual(is_polite(10 ** 100), 10 ** 100 + 1)
        self.assertEqual(is_polite(-1), None)
        self.assertEqual(is_polite(math.nan), None)
        self.assertEqual(is_polite(math.inf), None)
