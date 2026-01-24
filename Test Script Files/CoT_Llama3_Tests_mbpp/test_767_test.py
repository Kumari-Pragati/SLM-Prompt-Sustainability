import unittest
from mbpp_767_code import get_Pairs_Count

class TestGetPairsCount(unittest.TestCase):
    def test_get_Pairs_Count_typical(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3, 4, 5], 5, 7), 2)

    def test_get_Pairs_Count_edge(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3], 3, 3), 1)

    def test_get_Pairs_Count_zero_sum(self):
        self.assertEqual(get_Pairs_Count([1, 2, 3], 3, 0), 0)

    def test_get_Pairs_Count_empty_array(self):
        self.assertEqual(get_Pairs_Count([], 0, 5), 0)

    def test_get_Pairs_Count_single_element_array(self):
        self.assertEqual(get_Pairs_Count([1], 1, 5), 0)

    def test_get_Pairs_Count_invalid_input(self):
        with self.assertRaises(TypeError):
            get_Pairs_Count(None, 5, 7)
