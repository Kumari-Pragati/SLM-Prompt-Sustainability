import unittest
from mbpp_568_code import empty_list

class TestEmptyList(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(empty_list(1), [{}])
        self.assertEqual(empty_list(3), [{}, {}, {}])

    def test_edge_and_boundary_conditions(self):
        self.assertEqual(empty_list(0), [])
        self.assertEqual(empty_list(-1), [])
        self.assertEqual(empty_list(10000), [{}] * 10000)

    def test_complex_scenarios(self):
        self.assertEqual(empty_list(2) + empty_list(3), [{}, {}, {}, {}, {}])
        self.assertEqual(empty_list(0) + empty_list(1), [{}])
