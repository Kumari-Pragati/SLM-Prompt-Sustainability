import unittest
from mbpp_916_code import find_triplet_array

class TestFindTripletArray(unittest.TestCase):

    def test_typical_input(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 6
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 3))

    def test_edge_case_sum_equal_to_sum_of_three_smallest_elements(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 6
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 3))

    def test_edge_case_sum_equal_to_sum_of_three_largest_elements(self):
        A = [5, 4, 3, 2, 1]
        arr_size = len(A)
        sum = 10
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 5))

    def test_edge_case_sum_equal_to_sum_of_two_smallest_and_one_largest_elements(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 6
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 5))

    def test_edge_case_sum_equal_to_sum_of_two_largest_and_one_smallest_elements(self):
        A = [5, 4, 3, 2, 1]
        arr_size = len(A)
        sum = 10
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 5, 4))

    def test_edge_case_sum_equal_to_sum_of_three_middle_elements(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 7
        self.assertEqual(find_triplet_array(A, arr_size, sum), (2, 3, 4))

    def test_edge_case_sum_equal_to_sum_of_two_middle_elements_and_one_smallest_element(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 7
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 4))

    def test_edge_case_sum_equal_to_sum_of_two_middle_elements_and_one_largest_element(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 7
        self.assertEqual(find_triplet_array(A, arr_size, sum), (2, 3, 5))

    def test_edge_case_sum_equal_to_sum_of_one_smallest_element_and_two_largest_elements(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 7
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 4, 5))

    def test_edge_case_sum_equal_to_sum_of_one_largest_element_and_two_smallest_elements(self):
        A = [1, 2, 3, 4, 5]
        arr_size = len(A)
        sum = 7
        self.assertEqual(find_triplet_array(A, arr_size, sum), (1, 2, 5))

    def test_invalid_input_array_size_zero(self):
        A = []
        arr_size = len(A)
        sum = 6
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_invalid_input_array_size_one(self):
        A = [1]
        arr_size = len(A)
        sum = 6
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_invalid_input_array_size_two(self):
        A = [1, 2]
        arr_size = len(A)
        sum = 6
        self.assertFalse(find_triplet_array(A, arr_size, sum))

    def test_invalid_input_array_size_three(self):
        A = [1, 2, 3]
        arr_size = len(A)
        sum = 6
        self.assertFalse(find_triplet_array(A, arr_size, sum))
