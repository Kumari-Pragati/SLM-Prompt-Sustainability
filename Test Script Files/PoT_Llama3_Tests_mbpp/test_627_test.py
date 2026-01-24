import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(find_First_Missing([0,1,2,3,4,5,6,7,8,9], 0, 9), 10)

    def test_edge_case_start_equal_end(self):
        self.assertEqual(find_First_Missing([0], 0, 0), 1)

    def test_edge_case_start_greater_end(self):
        self.assertEqual(find_First_Missing([5,6,7,8,9], 9, 5), 4)

    def test_edge_case_array_empty(self):
        self.assertEqual(find_First_Missing([], 0, 0), 1)

    def test_edge_case_array_single_element(self):
        self.assertEqual(find_First_Missing([0], 0, 0), 1)

    def test_edge_case_array_single_element_out_of_range(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 0, 1), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self):
        self.assertEqual(find_First_Missing([0], 1, 0), 1)

    def test_edge_case_array_single_element_out_of_range_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse_reverse(self