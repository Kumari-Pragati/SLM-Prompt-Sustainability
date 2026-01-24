import unittest
from mbpp_760_code import unique_Element

class TestUniqueElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(unique_Element([1, 2, 3, 4, 5], 5), 'YES')

    def test_edge_case_empty_array(self):
        self.assertEqual(unique_Element([], 0), 'YES')

    def test_edge_case_single_element(self):
        self.assertEqual(unique_Element([1], 1), 'YES')

    def test_boundary_case_maximum_values(self):
        self.assertEqual(unique_Element([1000000000]*10000, 10000), 'YES')

    def test_complex_case_duplicate_elements(self):
        self.assertEqual(unique_Element([1, 2, 2, 3, 4, 5], 6), 'NO')

    def test_complex_case_mixed_elements(self):
        self.assertEqual(unique_Element([1, 2, 3, 4, 5, 5], 6), 'NO')
