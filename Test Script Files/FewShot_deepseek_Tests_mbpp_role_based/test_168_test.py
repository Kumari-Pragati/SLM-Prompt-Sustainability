import unittest
from mbpp_168_code import frequency

class TestFrequency(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(frequency([1, 2, 3, 2, 4], 2), 2)

    def test_edge_case_empty_list(self):
        self.assertEqual(frequency([], 2), 0)

    def test_boundary_case_single_element(self):
        self.assertEqual(frequency([2], 2), 1)
        self.assertEqual(frequency([2], 3), 0)

    def test_boundary_case_all_same_elements(self):
        self.assertEqual(frequency([2, 2, 2, 2], 2), 4)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            frequency("not a list", 2)
