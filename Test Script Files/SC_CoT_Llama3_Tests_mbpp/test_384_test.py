import unittest
from mbpp_384_code import frequency_Of_Smallest

class TestFrequencyOfSmallest(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 2, 1]), 2)

    def test_edge_case_single_element(self):
        self.assertEqual(frequency_Of_Smallest(1, [1]), 1)

    def test_edge_case_all_same(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 1, 1, 1]), 5)

    def test_edge_case_all_unique(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 4, 5]), 1)

    def test_edge_case_min_at_start(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 1, 2, 3, 4]), 2)

    def test_edge_case_min_at_end(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 3, 4, 1]), 2)

    def test_edge_case_min_in_middle(self):
        self.assertEqual(frequency_Of_Smallest(5, [1, 2, 1, 3, 4]), 2)

    def test_invalid_input_empty_list(self):
        with self.assertRaises(IndexError):
            frequency_Of_Smallest(5, [])

    def test_invalid_input_single_element_list(self):
        with self.assertRaises(IndexError):
            frequency_Of_Smallest(0, [1])

    def test_invalid_input_list_with_non_integer(self):
        with self.assertRaises(TypeError):
            frequency_Of_Smallest(5, ['a', 'b', 'c', 'd', 'e'])
