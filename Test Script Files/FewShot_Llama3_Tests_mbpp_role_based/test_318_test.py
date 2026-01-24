import unittest
from mbpp_318_code import max_volume

class TestMaxVolume(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(max_volume(3), 6)

    def test_edge_case_s_1(self):
        self.assertEqual(max_volume(1), 0)

    def test_edge_case_s_2(self):
        self.assertEqual(max_volume(2), 1)

    def test_edge_case_s_3(self):
        self.assertEqual(max_volume(3), 6)

    def test_edge_case_s_4(self):
        self.assertEqual(max_volume(4), 24)

    def test_edge_case_s_5(self):
        self.assertEqual(max_volume(5), 60)

    def test_invalid_input_s_0(self):
        with self.assertRaises(ValueError):
            max_volume(0)
