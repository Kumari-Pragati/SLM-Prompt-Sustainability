import unittest
from mbpp_901_code import smallest_multiple

class TestSmallestMultiple(unittest.TestCase):

    def test_normal_inputs(self):
        self.assertEqual(smallest_multiple(2), 6)
        self.assertEqual(smallest_multiple(3), 6)
        self.assertEqual(smallest_multiple(4), 12)
        self.assertEqual(smallest_multiple(5), 10)
        self.assertEqual(smallest_multiple(6), 12)
        self.assertEqual(smallest_multiple(7), 14)
        self.assertEqual(smallest_multiple(8), 16)
        self.assertEqual(smallest_multiple(9), 18)
        self.assertEqual(smallest_multiple(10), 20)
        self.assertEqual(smallest_multiple(12), 24)
        self.assertEqual(smallest_multiple(15), 30)

    def test_edge_cases(self):
        self.assertEqual(smallest_multiple(1), 2)
        self.assertEqual(smallest_multiple(0), 0)
        self.assertEqual(smallest_multiple(200), 800)
        self.assertEqual(smallest_multiple(2000), 8000)

    def test_boundary_cases(self):
        self.assertEqual(smallest_multiple(11), 22)
        self.assertEqual(smallest_multiple(12), 24)
        self.assertEqual(smallest_multiple(13), 26)
        self.assertEqual(smallest_multiple(14), 24)
        self.assertEqual(smallest_multiple(15), 30)
        self.assertEqual(smallest_multiple(16), 32)
        self.assertEqual(smallest_multiple(17), 34)
        self.assertEqual(smallest_multiple(18), 36)
        self.assertEqual(smallest_multiple(19), 38)
        self.assertEqual(smallest_multiple(20), 40)
