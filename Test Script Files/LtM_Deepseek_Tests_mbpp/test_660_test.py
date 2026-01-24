import unittest
from mbpp_660_code import find_Points

class TestFindPoints(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(find_Points(1, 2, 1, 2), (-1, -1))
        self.assertEqual(find_Points(3, 4, 3, 4), (-1, -1))

    def test_edge_conditions(self):
        self.assertEqual(find_Points(1, 2, 2, 3), (1, 3))
        self.assertEqual(find_Points(3, 4, 4, 5), (3, 5))
        self.assertEqual(find_Points(1, 1, 1, 1), (-1, -1))

    def test_complex_cases(self):
        self.assertEqual(find_Points(1, 2, 3, 4), (-1, -1))
        self.assertEqual(find_Points(4, 3, 2, 1), (-1, -1))
        self.assertEqual(find_Points(1, 2, 2, 1), (-1, -1))
        self.assertEqual(find_Points(2, 1, 1, 2), (-1, -1))
