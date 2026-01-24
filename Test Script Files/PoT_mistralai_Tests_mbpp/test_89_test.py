import unittest
from mbpp_89_code import closest_num

class TestClosestNum(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(closest_num(2), 1)
        self.assertEqual(closest_num(5), 4)
        self.assertEqual(closest_num(10), 9)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(closest_num(0), -1)
        self.assertEqual(closest_num(1), 0)
        self.assertEqual(closest_num(len(str(sys.maxsize))), sys.maxsize - 1)
