import unittest
from mbpp_292_code import find

class TestFind(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find(10, 3), 3)
        self.assertEqual(find(21, 7), 3)
        self.assertEqual(find(100, 25), 4)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find(0, 3), 0)
        self.assertEqual(find(3, 0), ValueError)
        self.assertEqual(find(1, 1), 1)
        self.assertEqual(find(2, 1), 2)
        self.assertEqual(find(1000000000, 1), 1000000000)
