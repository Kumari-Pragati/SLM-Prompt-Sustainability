import unittest
from mbpp_14_code import find_Volume

class TestFindVolume(unittest.TestCase):

    def test_typical_inputs(self):
        self.assertEqual(find_Volume(10, 5, 3), 150)

    def test_edge_cases(self):
        self.assertEqual(find_Volume(0, 0, 0), 0)
        self.assertEqual(find_Volume(10, 0, 0), 0)
        self.assertEqual(find_Volume(0, 5, 0), 0)
        self.assertEqual(find_Volume(0, 0, 10), 0)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            find_Volume('a', 5, 3)
        with self.assertRaises(TypeError):
            find_Volume(10, 'b', 3)
        with self.assertRaises(TypeError):
            find_Volume(10, 5, 'c')
