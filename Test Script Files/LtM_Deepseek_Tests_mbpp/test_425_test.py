import unittest
from mbpp_425_code import count_element_in_list

class TestCountElementInList(unittest.TestCase):

    def test_simple_inputs(self):
        self.assertEqual(count_element_in_list([1, 2, 3], 2), 1)
        self.assertEqual(count_element_in_list(['a', 'b', 'c'], 'b'), 1)

    def test_edge_conditions(self):
        self.assertEqual(count_element_in_list([], 1), 0)
        self.assertEqual(count_element_in_list([1, 2, 3], 4), 0)

    def test_boundary_conditions(self):
        self.assertEqual(count_element_in_list([1, 2, 3], 1), 1)
        self.assertEqual(count_element_in_list(['a', 'b', 'c'], 'c'), 1)

    def test_complex_cases(self):
        self.assertEqual(count_element_in_list([1, 2, 3, 2], 2), 2)
        self.assertEqual(count_element_in_list(['a', 'b', 'c', 'b'], 'b'), 2)
