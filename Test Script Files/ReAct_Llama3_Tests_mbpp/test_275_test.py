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
        m = 5
        self.assertEqual(get_Position(a, n, m), 3)

    def test_edge_case_max_at_start_zero(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_max_at_end_zero(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_max_at_middle_zero(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 5
        self.assertEqual(get_Position(a, n, m), 3)

    def test_edge_case_max_at_start_negative(self):
        a = [-10, -20, -30, -40, -50]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_max_at_end_negative(self):
        a = [-50, -40, -30, -20, -10]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 5)

    def test_edge_case_max_at_middle_negative(self):
        a = [-10, -20, -30, -40, -50]
        n = len(a)
        m = 5
        self.assertEqual(get_Position(a, n, m), 3)

    def test_edge_case_max_at_start_zero_negative(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_max_at_end_zero_negative(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_max_at_middle_zero_negative(self):
        a = [0, 0, 0, 0, 0]
        n = len(a)
        m = 5
        self.assertEqual(get_Position(a, n, m), 3)
