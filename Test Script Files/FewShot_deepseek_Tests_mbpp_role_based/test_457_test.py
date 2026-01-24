import unittest
from mbpp_457_code import Find_Min

class TestFindMin(unittest.TestCase):
    def test_typical_use_case(self):
        self.assertEqual(Find_Min([3, 1, 2]), 1)

    def test_edge_case_single_element(self):
        self.assertEqual(Find_Min([5]), 5)

    def test_boundary_case_empty_list(self):
        with self.assertRaises(ValueError):
            Find_Min([])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Find_Min("not a list")
