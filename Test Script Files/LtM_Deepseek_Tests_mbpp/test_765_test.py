import unittest
from mbpp_765_code import is_polite

class TestIsPolite(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(is_polite(1), 3)
        self.assertEqual(is_polite(2), 5)
        self.assertEqual(is_polite(3), 7)

    def test_edge_conditions(self):
        self.assertEqual(is_polite(0), 2)
        self.assertEqual(is_polite(100), 102)
        self.assertEqual(is_polite(1000), 1003)

    def test_boundary_conditions(self):
        self.assertEqual(is_polite(math.pow(2, 31) - 1), math.pow(2, 31))
        self.assertEqual(is_polite(math.pow(2, 31)), math.pow(2, 32))

    def test_complex_cases(self):
        self.assertEqual(is_polite(math.pow(2, 63) - 1), math.pow(2, 63))
        self.assertEqual(is_polite(math.pow(2, 63)), math.pow(2, 64))
