import unittest
from mbpp_686_code import defaultdict
from 686_code import freq_element

class TestFreqElement(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(freq_element((1, 1, 2, 3, 1)), "{'1': 2, '2': 1, '3': 1}")
        self.assertEqual(freq_element((3, 3, 3, 3, 3)), "{'3': 4}")

    def test_edge_cases(self):
        self.assertEqual(freq_element(()), "{}")
        self.assertEqual(freq_element((1,)), "{'1': 1}")
        self.assertEqual(freq_element((1, 1, 1, 1, 1)), "{'1': 4}")

    def test_boundary_cases(self):
        self.assertEqual(freq_element((-1, 0, 1)), "{'0': 1, '-1': 1, '1': 1}")
        self.assertEqual(freq_element((2147483647,)), "{'2147483647': 1}")

    def test_invalid_input(self):
        self.assertRaises(TypeError, freq_element, (1.0, 2))
        self.assertRaises(TypeError, freq_element, (object()))
