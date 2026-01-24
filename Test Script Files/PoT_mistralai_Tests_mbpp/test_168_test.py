import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(frequency([1, 2, 3, 2, 1], 2), 3)
        self.assertEqual(frequency(['a', 'b', 'a', 'c', 'a'], 'a'), 3)

    def test_edge_case_empty_list(self):
        self.assertEqual(frequency([], 1), 0)

    def test_edge_case_single_element(self):
        self.assertEqual(frequency([1], 1), 1)
        self.assertEqual(frequency(['a'], 'a'), 1)

    def test_edge_case_single_element_not_found(self):
        self.assertEqual(frequency([1], 2), 0)
        self.assertEqual(frequency(['a'], 'b'), 0)

    def test_corner_case_none_type(self):
        self.assertRaises(TypeError, frequency, None, 1)
