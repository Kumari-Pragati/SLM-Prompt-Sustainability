import unittest
from mbpp_137_code import zero_count

class TestZeroCount(unittest.TestCase):

    def test_zero_count(self):
        self.assertEqual(zero_count(array('i', [1, 2, 3, 4, 5])), 0.0)
        self.assertEqual(zero_count(array('i', [0, 0, 0, 0, 0])), 1.0)
        self.assertEqual(zero_count(array('i', [1, 0, 1, 0, 1])), 0.4)
        self.assertEqual(zero_count(array('i', [0, 1, 2, 3, 4])), 0.0)
        self.assertEqual(zero_count(array('i', [0, 0, 1, 2, 3])), 0.3333333333333333)

    def test_zero_count_empty(self):
        self.assertEqual(zero_count(array('i', [])), 0.0)

    def test_zero_count_single(self):
        self.assertEqual(zero_count(array('i', [0])), 1.0)
