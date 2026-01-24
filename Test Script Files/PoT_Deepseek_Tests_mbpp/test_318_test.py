import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(max_volume(5), 60)

    def test_edge_case_s_equals_1(self):
        self.assertEqual(max_volume(1), 0)

    def test_boundary_case_s_equals_2(self):
        self.assertEqual(max_volume(2), 2)

    def test_corner_case_s_equals_3(self):
        self.assertEqual(max_volume(3), 6)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            max_volume(-1)
