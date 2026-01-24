import unittest
from mbpp_686_code import defaultdict
from 686_code import freq_element

class TestFreqElement(unittest.TestCase):

    def test_simple(self):
        self.assertEqual(freq_element((1, 1, 2, 2, 3)), '{"1": 2, "2": 2, "3": 1}')
        self.assertEqual(freq_element((2, 2, 2, 3, 3)), '{"2": 3, "3": 2}')
        self.assertEqual(freq_element((4, 4, 4, 4, 4)), '{"4": 5}')

    def test_edge_cases(self):
        self.assertEqual(freq_element(()), '{}')
        self.assertEqual(freq_element((1,)), '{"1": 1}')
        self.assertEqual(freq_element((1, 1, 1, 2)), '{"1": 3, "2": 1}')
        self.assertEqual(freq_element((1, 1, 1, 1, 2)), '{"1": 4, "2": 1}')
