import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertTrue(same_Length(123, 123))
        self.assertTrue(same_Length(12345, 12345))

    def test_edge_conditions(self):
        self.assertTrue(same_Length(0, 0))
        self.assertFalse(same_Length(1, 0))
        self.assertFalse(same_Length(0, 1))

    def test_boundary_conditions(self):
        self.assertTrue(same_Length(10**9, 10**9))
        self.assertFalse(same_Length(10**9 + 1, 10**9))
        self.assertFalse(same_Length(10**9, 10**9 + 1))

    def test_more_complex_cases(self):
        self.assertTrue(same_Length(123456789, 987654321))
        self.assertFalse(same_Length(1234567890, 987654321))
        self.assertFalse(same_Length(123456789, 9876543210))
