import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(max_volume(1), 0)
        self.assertEqual(max_volume(2), 0)
        self.assertEqual(max_volume(3), 0)

    def test_edge_conditions(self):
        self.assertEqual(max_volume(0), 0)
        self.assertEqual(max_volume(10), 270)
        self.assertEqual(max_volume(11), 363)
        self.assertEqual(max_volume(12), 432)

    def test_complex_cases(self):
        self.assertEqual(max_volume(13), 455)
        self.assertEqual(max_volume(14), 480)
        self.assertEqual(max_volume(15), 500)
