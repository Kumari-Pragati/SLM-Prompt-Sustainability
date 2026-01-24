import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_typical_cases(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))
        self.assertEqual(find_Points(5, 6, 2, 3), (2, 6))
        self.assertEqual(find_Points(0, 0, 10, 10), (0, 10))

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find_Points(0, 0, 0, 0), (-1, -1))
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))
        self.assertEqual(find_Points(1, 2, 1, 2), (1, 2))
        self.assertEqual(find_Points(1, 2, 2, 1), (1, 2))
        self.assertEqual(find_Points(float('inf'), float('inf'), float('inf'), float('inf')), (float('inf'), float('inf')))
        self.assertEqual(find_Points(float('-inf'), float('-inf'), float('-inf'), float('-inf')), (float('-inf'), float('-inf')))
