import unittest
from mbpp_555_code import difference

class TestDifference(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(difference(5), 120)
        self.assertEqual(difference(10), 455)
        self.assertEqual(difference(20), 1716)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(difference(0), 0)
        self.assertEqual(difference(1), 0)
        self.assertEqual(difference(2), 2)
        self.assertEqual(difference(3), 6)
        self.assertEqual(difference(4294967295), 2147483647024)
