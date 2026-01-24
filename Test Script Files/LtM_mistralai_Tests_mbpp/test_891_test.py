import unittest
from mbpp_891_code import same_Length

class TestSameLength(unittest.TestCase):
    def test_simple(self):
        self.assertTrue(same_Length(123, 456))
        self.assertTrue(same_Length(999, 999))
        self.assertFalse(same_Length(123, 457))
        self.assertFalse(same_Length(0, 123))
        self.assertFalse(same_Length(123, 0))

    def test_edge_cases(self):
        self.assertTrue(same_Length(9, 90))
        self.assertTrue(same_Length(90, 9))
        self.assertFalse(same_Length(9, 10))
        self.assertFalse(same_Length(10, 9))
        self.assertTrue(same_Length(0, 0))

    def test_complex(self):
        self.assertTrue(same_Length(123456789, 987654321))
        self.assertFalse(same_Length(123456789, 1234567890))
        self.assertFalse(same_Length(1234567890, 123456789))
