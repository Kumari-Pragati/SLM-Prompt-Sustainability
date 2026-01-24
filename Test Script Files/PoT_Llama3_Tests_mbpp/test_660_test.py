import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_Points(1, 3, 2, 4), (-1, 4))

    def test_edge_case_l1_l2_equal(self):
        self.assertEqual(find_Points(1, 1, 2, 2), (-1, 2))

    def test_edge_case_r1_r2_equal(self):
        self.assertEqual(find_Points(1, 3, 1, 1), (1, 1))

    def test_edge_case_l1_l2_r1_r2_equal(self):
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, 1))

    def test_edge_case_l1_greater_than_r1(self):
        self.assertEqual(find_Points(3, 1, 2, 4), (2, 4))

    def test_edge_case_l2_greater_than_r2(self):
        self.assertEqual(find_Points(1, 3, 4, 2), (1, 3))

    def test_edge_case_l1_greater_than_l2_and_r1_greater_than_r2(self):
        self.assertEqual(find_Points(3, 1, 2, 4), (2, 4))

    def test_edge_case_l1_greater_than_l2_and_r1_equal_to_r2(self):
        self.assertEqual(find_Points(3, 1, 2, 2), (2, 2))

    def test_edge_case_l1_greater_than_l2_and_r1_greater_than_r2(self):
        self.assertEqual(find_Points(3, 1, 2, 4), (2, 4))

    def test_edge_case_l1_greater_than_l2_and_r1_equal_to_r2(self):
        self.assertEqual(find_Points(3, 1, 2, 2), (2, 2))

    def test_edge_case_l1_greater_than_l2_and_r1_greater_than_r2(self):
        self.assertEqual(find_Points(3, 1, 2, 4), (2, 4))

    def test_edge_case_l1_greater_than_l2_and_r1_equal_to_r2(self):
        self.assertEqual(find_Points(3, 1, 2, 2), (2, 2))
