import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (1, 4))
        self.assertEqual(find_Points(3, 4, 1, 2), (1, 4))
        self.assertEqual(find_Points(1, 1, 2, 2), (-1, -1))

    def test_edge_and_boundary(self):
        self.assertEqual(find_Points(0, 0, 1, 1), (-1, 1))
        self.assertEqual(find_Points(1, 1, 0, 0), (0, 1))
        self.assertEqual(find_Points(0, 0, 0, 0), (-1, -1))
        self.assertEqual(find_Points(float('inf'), float('inf'), float('inf'), float('inf')), (-1, -1))
        self.assertEqual(find_Points(-float('inf'), -float('inf'), -float('inf'), -float('inf')), (-1, -1))

    def test_complex(self):
        self.assertEqual(find_Points(-1, 0, 1, 1), (-1, 1))
        self.assertEqual(find_Points(1, 1, -1, 0), (1, 0))
        self.assertEqual(find_Points(float('inf'), -float('inf'), -float('inf'), float('inf')), (-float('inf'), float('inf')))
        self.assertEqual(find_Points(-float('inf'), float('inf'), float('inf'), -float('inf')), (-float('inf'), float('inf')))
