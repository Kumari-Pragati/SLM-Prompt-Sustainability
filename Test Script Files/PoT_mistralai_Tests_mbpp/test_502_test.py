import unittest
from mbpp_502_code import find

class TestFind(unittest.TestCase):
    def test_typical_cases(self):
        self.assertEqual(find(10, 3), 1)
        self.assertEqual(find(20, 5), 0)
        self.assertEqual(find(30, 7), 3)

    def test_edge_and_boundary_cases(self):
        self.assertEqual(find(0, 3), 0)
        self.assertEqual(find(1, 1), 0)
        self.assertEqual(find(2, 2), 0)
        self.assertEqual(find(3, 0), TraceError)
        self.assertEqual(find(-10, 3), TraceError)
