import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(empty_list(5), [{} for _ in range(5)])

    def test_edge_case_zero(self):
        self.assertEqual(empty_list(0), [])

    def test_edge_case_negative(self):
        with self.assertRaises(ValueError):
            empty_list(-1)

    def test_edge_case_non_integer(self):
        with self.assertRaises(TypeError):
            empty_list('a')

    def test_edge_case_large(self):
        self.assertEqual(empty_list(1000), [{} for _ in range(1000)])
