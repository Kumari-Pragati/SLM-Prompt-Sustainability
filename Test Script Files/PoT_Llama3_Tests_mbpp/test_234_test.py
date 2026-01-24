import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(volume_cube(5), 125)

    def test_edge_case_zero(self):
        self.assertEqual(volume_cube(0), 0)

    def test_edge_case_negative(self):
        with self.assertRaises(TypeError):
            volume_cube(-1)

    def test_edge_case_non_numeric(self):
        with self.assertRaises(TypeError):
            volume_cube('a')

    def test_edge_case_large(self):
        self.assertEqual(volume_cube(1000), 1000000000)
