import unittest
from mbpp_588_code import big_diff

class TestBigDiff(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(big_diff([10, 2, 7, 2]), 8)

    def test_edge_case_single_element(self):
        self.assertEqual(big_diff([5]), 0)

    def test_boundary_case_max_min(self):
        self.assertEqual(big_diff([100, 0]), 100)

    def test_boundary_case_max_max(self):
        self.assertEqual(big_diff([100, 100]), 0)

    def test_boundary_case_min_min(self):
        self.assertEqual(big_diff([-100, -100]), 0)

    def test_boundary_case_min_max(self):
        self.assertEqual(big_diff([-100, 100]), 200)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            big_diff("10, 2, 7, 2")
