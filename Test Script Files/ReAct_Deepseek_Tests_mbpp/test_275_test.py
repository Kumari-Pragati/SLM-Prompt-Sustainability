import unittest
from mbpp_275_code import get_Position

class TestGetPosition(unittest.TestCase):

    def test_typical_case(self):
        a = [10, 20, 30, 40]
        n = len(a)
        m = 5
        self.assertEqual(get_Position(a, n, m), 2)

    def test_edge_case_with_single_element(self):
        a = [10]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_with_multiple_elements_divisible_by_m(self):
        a = [10, 20, 30, 40]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_with_multiple_elements_not_divisible_by_m(self):
        a = [11, 22, 33, 44]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 4)

    def test_edge_case_with_all_elements_equal_to_m(self):
        a = [10, 20, 30, 40]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 1)

    def test_edge_case_with_all_elements_less_than_m(self):
        a = [9, 8, 7, 6]
        n = len(a)
        m = 10
        self.assertEqual(get_Position(a, n, m), 4)

    def test_edge_case_with_negative_elements(self):
        a = [-10, -20, -30, -40]
        n = len(a)
        m = -10
        self.assertEqual(get_Position(a, n, m), 4)

    def test_edge_case_with_zero_elements(self):
        a = [0, 0, 0, 0]
        n = len(a)
        m = 0
        self.assertEqual(get_Position(a, n, m), 1)
