import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(max_volume(2), 2)

    def test_edge(self):
        self.assertEqual(max_volume(1), 0)
        self.assertEqual(max_volume(0), 0)

    def test_max_value(self):
        self.assertEqual(max_volume(3), 6)

    def test_max_value_edge(self):
        self.assertEqual(max_volume(4), 24)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_volume(None)

    def test_invalid_input_edge(self):
        with self.assertRaises(TypeError):
            max_volume("")
