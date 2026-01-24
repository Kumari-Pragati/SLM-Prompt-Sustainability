import unittest
from mbpp_234_code import volume_cube

class TestVolumeCube(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(volume_cube(2), 8)
        self.assertEqual(volume_cube(5), 125)
        self.assertEqual(volume_cube(10), 1000)

    def test_edge_cases(self):
        self.assertEqual(volume_cube(0), 0)
        self.assertEqual(volume_cube(-1), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            volume_cube('a')
        with self.assertRaises(TypeError):
            volume_cube(None)

    def test_special_cases(self):
        self.assertEqual(volume_cube(-10), 1000)
