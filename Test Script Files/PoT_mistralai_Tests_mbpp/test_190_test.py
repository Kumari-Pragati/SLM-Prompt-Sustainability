import unittest
from mbpp_190_code import count_Intgral_Points

class TestCountIntgralPoints(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_Intgral_Points(1, 2, 3, 4), 6)

    def test_edge_case_zero(self):
        self.assertEqual(count_IntgralPoints(0, 0, 0, 0), 0)

    def test_edge_case_one(self):
        self.assertEqual(count_IntgralPoints(0, 0, 1, 1), 0)
        self.assertEqual(count_IntgralPoints(1, 1, 0, 0), 0)

    def test_edge_case_negative(self):
        self.assertEqual(count_IntgralPoints(-1, -2, 0, 0), 0)
        self.assertEqual(count_IntgralPoints(0, 0, -1, -2), 0)

    def test_boundary_case_min_max(self):
        self.assertEqual(count_IntgralPoints(sys.maxsize, sys.maxsize, sys.maxsize, sys.maxsize), sys.maxsize * sys.maxsize)
        self.assertEqual(count_IntgralPoints(sys.minsize, sys.minsize, sys.minsize, sys.minsize), 0)
