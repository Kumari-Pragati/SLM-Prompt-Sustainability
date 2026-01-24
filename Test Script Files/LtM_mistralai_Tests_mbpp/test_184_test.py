import unittest
from mbpp_184_code import greater_specificnum

class TestGreaterSpecificNum(unittest.TestCase):

    def test_simple(self):
        self.assertTrue(greater_specificnum([1, 2, 3], 1))
        self.assertTrue(greater_specificnum([5, 4, 3], 5))
        self.assertFalse(greater_specificnum([1, 2, 3], 4))

    def test_edge_cases(self):
        self.assertTrue(greater_specificnum([0, 0], 1))
        self.assertFalse(greater_specificnum([1000000000], 1000000001))
        self.assertTrue(greater_specificnum([], any))

    def test_complex(self):
        self.assertTrue(greater_specificnum([-1, 0, 1], 0))
        self.assertFalse(greater_specificnum([1, 2, 3], -1))
        self.assertTrue(greater_specificnum([float('inf')], float('inf')))
