import unittest
from mbpp_627_code import find_First_Missing

class TestFindFirstMissing(unittest.TestCase):
    def test_typical_case(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_First_Missing(array, 0, 9), 10)

    def test_edge_case_start_greater_than_end(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_First_Missing(array, 10, 0), 1)

    def test_edge_case_start_equal_to_end(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_First_Missing(array, 0, 0), 1)

    def test_edge_case_start_equal_to_array_start(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_First_Missing(array, 0, 9), 1)

    def test_edge_case_start_equal_to_array_end(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_First_Missing(array, 9, 9), 10)

    def test_edge_case_array_empty(self):
        array = []
        self.assertEqual(find_First_Missing(array, 0, 0), 1)

    def test_edge_case_array_single_element(self):
        array = [0]
        self.assertEqual(find_First_Missing(array, 0, 0), 1)

    def test_edge_case_array_two_elements(self):
        array = [0, 1]
        self.assertEqual(find_First_Missing(array, 0, 1), 2)

    def test_edge_case_array_three_elements(self):
        array = [0, 1, 2]
        self.assertEqual(find_First_Missing(array, 0, 2), 3)

    def test_edge_case_array_four_elements(self):
        array = [0, 1, 2, 3]
        self.assertEqual(find_First_Missing(array, 0, 3), 4)

    def test_edge_case_array_five_elements(self):
        array = [0, 1, 2, 3, 4]
        self.assertEqual(find_First_Missing(array, 0, 4), 5)

    def test_edge_case_array_six_elements(self):
        array = [0, 1, 2, 3, 4, 5]
        self.assertEqual(find_First_Missing(array, 0, 5), 6)

    def test_edge_case_array_seven_elements(self):
        array = [0, 1, 2, 3, 4, 5, 6]
        self.assertEqual(find_First_Missing(array, 0, 6), 7)

    def test_edge_case_array_eight_elements(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        self.assertEqual(find_First_Missing(array, 0, 7), 8)

    def test_edge_case_array_nine_elements(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.assertEqual(find_First_Missing(array, 0, 8), 9)

    def test_edge_case_array_ten_elements(self):
        array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_First_Missing(array, 0, 9), 10)
