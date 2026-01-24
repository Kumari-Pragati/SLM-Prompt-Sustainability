import unittest
from mbpp_801_code import test_three_equal

class TestThreeEqual(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(test_three_equal(1, 2, 3), 0)
        self.assertEqual(test_three_equal(1, 1, 1), 0)
        self.assertEqual(test_three_equal(2, 2, 3), 0)

    def test_edge_cases(self):
        self.assertEqual(test_three_equal(1, 2, 4), 1)
        self.assertEqual(test_three_equal(1, 1, 4), 1)
        self.assertEqual(test_three_equal(2, 3, 4), 1)
        self.assertEqual(test_three_equal(1, 2, 1), 1)
        self.assertEqual(test_three_equal(1, 1, 2), 1)
        self.assertEqual(test_three_equal(2, 1, 1), 1)

    def test_empty_inputs(self):
        self.assertEqual(test_three_equal(0, 0, 0), 3)
        self.assertEqual(test_three_equal(None, None, None), 3)
        self.assertEqual(test_three_equal('', '', ''), 3)
