import unittest
from mbpp_575_code import count_no

class TestCountNo(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_no(2, 2, 1, 10), 6)

    def test_edge_case(self):
        self.assertEqual(count_no(1, 1, 1, 1), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_no("2", 2, 1, 10)
        with self.assertRaises(TypeError):
            count_no(2, "2", 1, 10)
        with self.assertRaises(TypeError):
            count_no(2, 2, "1", 10)
        with self.assertRaises(TypeError):
            count_no(2, 2, 1, "10")

    def test_N_greater_than_count(self):
        self.assertEqual(count_no(2, 3, 1, 10), 10)

    def test_N_equal_to_zero(self):
        self.assertEqual(count_no(2, 0, 1, 10), 1)
