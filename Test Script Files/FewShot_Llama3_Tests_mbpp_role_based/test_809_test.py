import unittest
from mbpp_809_code import check_smaller

class TestCheckSmaller(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertTrue(check_smaller((1, 2, 3), (0, 1, 2)))

    def test_edge_case_equal(self):
        self.assertFalse(check_smaller((1, 1, 1), (1, 1, 1)))

    def test_edge_case_all_greater(self):
        self.assertTrue(check_smaller((2, 3, 4), (1, 2, 3)))

    def test_edge_case_all_less(self):
        self.assertFalse(check_smaller((1, 0, -1), (2, 3, 4)))

    def test_invalid_input_type(self):
        with self.assertRaises(TypeError):
            check_smaller("test", (1, 2, 3))

    def test_invalid_input_length(self):
        with self.assertRaises(ValueError):
            check_smaller((1, 2), (1, 2, 3))
