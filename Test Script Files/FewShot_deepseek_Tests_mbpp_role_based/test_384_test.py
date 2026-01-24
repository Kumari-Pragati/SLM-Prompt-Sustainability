import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):
    def test_typical_use_case(self):
        arr = [1, 2, 3, 4, 5, 1, 1]
        self.assertEqual(frequency_Of_Smallest(len(arr), arr), 3)

    def test_edge_case_single_element(self):
        arr = [1]
        self.assertEqual(frequency_Of_Smallest(len(arr), arr), 1)

    def test_boundary_case_all_same_elements(self):
        arr = [1, 1, 1, 1, 1]
        self.assertEqual(frequency_Of_Smallest(len(arr), arr), 5)

    def test_boundary_case_all_different_elements(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(frequency_Of_Smallest(len(arr), arr), 1)

    def test_invalid_input_empty_array(self):
        arr = []
        with self.assertRaises(ValueError):
            frequency_Of_Smallest(len(arr), arr)
