import unittest
from mbpp_476_code import big_sum

class TestBigSum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(big_sum([1, 2, 3, 4, 5]), 1 + 5)

    def test_edge_case_min_max(self):
        self.assertEqual(big_sum([-100, -50, -1, 0, 1, 50, 100]), 100 + (-100))

    def test_edge_case_single_element(self):
        self.assertEqual(big_sum([1]), 1 + (-sys.maxsize if sys.platform == 'win32' else -sys.maxsize - 1))

    def test_edge_case_empty(self):
        self.assertEqual(big_sum([]), sys.maxsize if sys.platform == 'win32' else -sys.maxsize - 1)
