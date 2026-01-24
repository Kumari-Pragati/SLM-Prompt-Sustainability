import unittest
from mbpp_743_code import rotate_right

class TestRotateRight(unittest.TestCase):
    def test_typical_use_case(self):
        list1 = [1, 2, 3, 4, 5]
        m = 2
        n = 1
        expected_result = [4, 5, 1, 2, 3]
        self.assertEqual(rotate_right(list1, m, n), expected_result)

    def test_edge_case_m_zero(self):
        list1 = [1, 2, 3, 4, 5]
        m = 0
        n = 1
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(rotate_right(list1, m, n), expected_result)

    def test_edge_case_n_zero(self):
        list1 = [1, 2, 3, 4, 5]
        m = 2
        n = 0
        expected_result = [3, 4, 5, 1, 2]
        self.assertEqual(rotate_right(list1, m, n), expected_result)

    def test_edge_case_m_equal_to_length(self):
        list1 = [1, 2, 3, 4, 5]
        m = 5
        n = 1
        expected_result = [5, 1, 2, 3, 4]
        self.assertEqual(rotate_right(list1, m, n), expected_result)

    def test_edge_case_n_equal_to_length(self):
        list1 = [1, 2, 3, 4, 5]
        m = 1
        n = 5
        expected_result = [4, 5, 1, 2, 3]
        self.assertEqual(rotate_right(list1, m, n), expected_result)

    def test_invalid_input_type_m(self):
        list1 = [1, 2, 3, 4, 5]
        m = 'a'
        n = 1
        with self.assertRaises(TypeError):
            rotate_right(list1, m, n)

    def test_invalid_input_type_n(self):
        list1 = [1, 2, 3, 4, 5]
        m = 1
        n = 'b'
        with self.assertRaises(TypeError):
            rotate_right(list1, m, n)
