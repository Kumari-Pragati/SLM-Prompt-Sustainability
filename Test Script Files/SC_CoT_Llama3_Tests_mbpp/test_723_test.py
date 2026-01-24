import unittest
from mbpp_723_code import count_same_pair

class TestCountSamePair(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(count_same_pair([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]), 5)
        self.assertEqual(count_same_pair([1, 2, 2, 3, 3], [1, 2, 2, 3, 3]), 3)
        self.assertEqual(count_same_pair([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]), 5)

    def test_edge_cases(self):
        self.assertEqual(count_same_pair([], []), 0)
        self.assertEqual(count_same_pair([1, 2, 3], []), 0)
        self.assertEqual(count_same_pair([], [1, 2, 3]), 0)

    def test_empty_input(self):
        self.assertEqual(count_same_pair([], []), 0)
        self.assertEqual(count_same_pair([], [1, 2, 3]), 0)
        self.assertEqual(count_same_pair([1, 2, 3], []), 0)

    def test_single_element_input(self):
        self.assertEqual(count_same_pair([1], [1]), 1)
        self.assertEqual(count_same_pair([1], [2]), 0)
        self.assertEqual(count_same_pair([1, 2], [1]), 1)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_same_pair("a", [1, 2, 3])
        with self.assertRaises(TypeError):
            count_same_pair([1, 2, 3], "a")
