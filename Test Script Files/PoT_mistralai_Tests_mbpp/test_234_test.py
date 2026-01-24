import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(volume_cube(3), 27)

    def test_edge_case_zero(self):
        self.assertEqual(volume_cube(0), 0)

    def test_edge_case_one(self):
        self.assertEqual(volume_cube(1), 1)

    def test_edge_case_negative(self):
        self.assertEqual(volume_cube(-1), None)
