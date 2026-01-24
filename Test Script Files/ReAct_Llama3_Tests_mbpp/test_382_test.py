import unittest
from mbpp_382_code import find_rotation_count

class TestFindRotationCount(unittest.TestCase):
    def test_typical_case(self):
        A = [1, 2, 3, 4, 5]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_left_rotation(self):
        A = [5, 1, 2, 3, 4]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_right_rotation(self):
        A = [1, 2, 3, 4, 5]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_middle_rotation(self):
        A = [5, 4, 3, 2, 1]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_no_rotation(self):
        A = [1, 2, 3, 4, 5]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_single_element(self):
        A = [1]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_empty_array(self):
        A = []
        self.assertEqual(find_rotation_count(A), -1)

    def test_edge_case_single_element_rotation(self):
        A = [5]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_rotation_at_start(self):
        A = [5, 1, 2, 3, 4]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_rotation_at_end(self):
        A = [1, 2, 3, 4, 5]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_rotation_at_middle(self):
        A = [5, 4, 3, 2, 1]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_rotation_at_start_and_end(self):
        A = [5, 1, 2, 3, 4]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_rotation_at_start_and_middle(self):
        A = [5, 4, 3, 2, 1]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_rotation_at_end_and_middle(self):
        A = [1, 2, 3, 4, 5]
        self.assertEqual(find_rotation_count(A), 0)

    def test_edge_case_rotation_at_start_and_middle_and_end(self):
        A = [5, 4, 3, 2, 1]
        self.assertEqual(find_rotation_count(A), 0)
