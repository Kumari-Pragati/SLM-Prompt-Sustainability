import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(max_volume(2), 2)
        self.assertEqual(max_volume(3), 6)
        self.assertEqual(max_volume(4), 24)

    def test_edge_input(self):
        self.assertEqual(max_volume(1), 1)
        self.assertEqual(max_volume(0), 0)

    def test_boundary_input(self):
        self.assertEqual(max_volume(5), 40)
        self.assertEqual(max_volume(10), 945)

    def test_complex_input(self):
        self.assertEqual(max_volume(17), 1560)
        self.assertEqual(max_volume(28), 49504)
