import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(get_Position([1, 2, 3, 4], 4, 2), 3)
        self.assertEqual(get_Position([5, 10, 15, 20], 4, 5), 1)

    def test_edge_case_1(self):
        self.assertEqual(get_Position([0], 1, 1), 1)
        self.assertEqual(get_Position([0], 0, 1), 0)

    def test_edge_case_2(self):
        self.assertEqual(get_Position([1, 2, 3], 3, 1), 3)
        self.assertEqual(get_Position([1, 2, 3], 0, 1), 0)

    def test_invalid_input_1(self):
        with self.assertRaises(TypeError):
            get_Position(1, 2, "m")

    def test_invalid_input_2(self):
        with self.assertRaises(ValueError):
            get_Position([1, 2, 3], -1, 2)
