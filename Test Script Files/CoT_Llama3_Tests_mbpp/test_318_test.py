import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):

    def test_typical_input(self):
        self.assertEqual(max_volume(3), 6)

    def test_edge_case(self):
        self.assertEqual(max_volume(1), 0)

    def test_edge_case2(self):
        self.assertEqual(max_volume(2), 0)

    def test_edge_case3(self):
        self.assertEqual(max_volume(3), 6)

    def test_edge_case4(self):
        self.assertEqual(max_volume(4), 24)

    def test_edge_case5(self):
        self.assertEqual(max_volume(5), 60)

    def test_edge_case6(self):
        self.assertEqual(max_volume(6), 120)

    def test_edge_case7(self):
        self.assertEqual(max_volume(7), 210)

    def test_edge_case8(self):
        self.assertEqual(max_volume(8), 336)

    def test_edge_case9(self):
        self.assertEqual(max_volume(9), 504)

    def test_edge_case10(self):
        self.assertEqual(max_volume(10), 720)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            max_volume("a")
