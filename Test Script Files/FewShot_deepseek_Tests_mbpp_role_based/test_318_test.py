import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_volume(5), 60)

    def test_boundary_condition(self):
        self.assertEqual(max_volume(1), 0)

    def test_edge_condition(self):
        self.assertEqual(max_volume(2), 2)

    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            max_volume(-1)
