import unittest
from mbpp_275_code import get_Position

class TestGet_Position(unittest.TestCase):
    def test_typical_case(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case_max_at_start(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_max_at_end(self):
        a = [50, 40, 30, 20, 10]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case_max_at_middle(self):
        a = [10, 20, 30, 40, 50]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 3)

    def test_invalid_input_non_list(self):
        a = "not a list"
        n = len(a)
        m = 10
        with self.assertRaises(TypeError):
            get_Position(a, n, m)

    def test_invalid_input_non_integer(self):
        a = [10, 20, 30, 40, 50]
        n = "not an integer"
        m = 10
        with self.assertRaises(TypeError):
            get_Position(a, n, m)

    def test_invalid_input_non_positive_integer(self):
        a = [10, 20, 30, 40, 50]
        n = -1
        m = 10
        with self.assertRaises(ValueError):
            get_Position(a, n, m)
