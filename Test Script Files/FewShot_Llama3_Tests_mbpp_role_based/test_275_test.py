import unittest
from mbpp_275_code import get_Position

class TestGet_Position(unittest.TestCase):
    def test_typical_use_case(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        m = 2
        self.assertEqual(get_Position(a, n, m), 3)

    def test_edge_case_max_value_at_start(self):
        a = [5, 4, 3, 2, 1]
        n = len(a)
        m = 2
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_max_value_at_end(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        m = 2
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case_max_value_at_middle(self):
        a = [1, 2, 3, 4, 5]
        n = len(a)
        m = 2
        self.assertEqual(get_Position(a, n, m), 3)

    def test_edge_case_max_value_at_start_with_zero(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 2
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_max_value_at_end_with_zero(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 2
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case_max_value_at_middle_with_zero(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 2
        self.assertEqual(get_Position(a, n, m), 3)
