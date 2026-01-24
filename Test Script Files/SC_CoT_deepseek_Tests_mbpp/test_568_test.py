import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(empty_list(5), [{} for _ in range(5)])

    def test_boundary_case(self):
        self.assertEqual(empty_list(0), [])

    def test_edge_case(self):
        self.assertEqual(empty_list(1), [{}] )

    def test_negative_case(self):
        with self.assertRaises(Exception):
            empty_list(-1)
