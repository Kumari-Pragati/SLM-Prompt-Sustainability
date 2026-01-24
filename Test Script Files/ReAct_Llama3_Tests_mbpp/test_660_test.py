import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(find_Points(1, 3, 2, 4), (-2, 4))

    def test_edge_case_l1_l2_equal(self):
        self.assertEqual(find_Points(1, 1, 2, 4), (-1, 4))

    def test_edge_case_r1_r2_equal(self):
        self.assertEqual(find_Points(1, 3, 4, 4), (1, -1))

    def test_edge_case_l1_l2_r1_r2_equal(self):
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))

    def test_edge_case_l1_l2_r1_r2_not_equal(self):
        self.assertEqual(find_Points(1, 3, 2, 4), (-2, 4))

    def test_edge_case_l1_l2_not_equal_r1_r2_equal(self):
        self.assertEqual(find_Points(1, 2, 2, 2), (-1, 2))

    def test_edge_case_l1_l2_r1_r2_not_equal(self):
        self.assertEqual(find_Points(1, 3, 2, 4), (-2, 4))
