import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(big_diff([1, 2, 3, 4, 5]), 4)
        self.assertEqual(big_diff([-1, -2, -3, -4, -5]), 6)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(big_diff([0, 0]), 0)
        self.assertEqual(big_diff([-10000, -9999, -9998]), 19998)
        self.assertEqual(big_diff([9999, 10000]), 10000)
        self.assertEqual(big_diff([-10000, 10000]), 20000)
        self.assertEqual(big_diff([10000, -10000]), 20000)

    def test_empty_list(self):
        self.assertEqual(big_diff([]), 0)

    def test_single_element(self):
        self.assertEqual(big_diff([1]), 0)
        self.assertEqual(big_diff([-1]), 0)
