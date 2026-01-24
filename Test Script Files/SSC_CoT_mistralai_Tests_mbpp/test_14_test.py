import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(find_Volume(3, 4, 5), 60.0)
        self.assertEqual(find_Volume(2, 2, 2), 8.0)
        self.assertEqual(find_Volume(1, 1, 1), 1.0)

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(find_Volume(0, 4, 5), 0.0)
        self.assertEqual(find_Volume(3, 0, 5), 0.0)
        self.assertEqual(find_Volume(3, 4, 0), 0.0)
        self.assertEqual(find_Volume(-3, 4, 5), 0.0)
        self.assertEqual(find_Volume(3, -4, 5), 0.0)
        self.assertEqual(find_Volume(3, 4, -5), 0.0)

    def test_negative_volume(self):
        self.assertAlmostEqual(find_Volume(-3, 4, 5), 0.0)
        self.assertAlmostEqual(find_Volume(3, -4, 5), 0.0)
        self.assertAlmostEqual(find_Volume(3, 4, -5), 0.0)
