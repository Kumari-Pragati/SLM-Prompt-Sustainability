import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)

    def test_edge_case_empty_lists(self):
        self.assertEqual(count_same_pair([], []), 0)

    def test_boundary_case_single_element(self):
        self.assertEqual(count_same_pair([1], [1]), 1)
        self.assertEqual(count_same_pair([1], [2]), 0)

    def test_boundary_case_multiple_same_elements(self):
        self.assertEqual(count_same_pair([1, 1, 1], [1, 1, 1]), 3)
        self.assertEqual(count_same_pair([1, 2, 3], [1, 2, 3]), 3)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_same_pair([1, 2, 3], [1, '2', 3])
