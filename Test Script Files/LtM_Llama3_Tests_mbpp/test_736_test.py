import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):
    def test_simple_insertion(self):
        self.assertEqual(left_insertion([1, 2, 3], 2), 1)
        self.assertEqual(left_insertion([1, 2, 3], 1), 0)
        self.assertEqual(left_insertion([1, 2, 3], 3), 2)
        self.assertEqual(left_insertion([1, 2, 3], 4), 3)
        self.assertEqual(left_insertion([1, 2, 3], 0), 0)

    def test_empty_input(self):
        self.assertEqual(left_insertion([], 1), 0)

    def test_single_element_input(self):
        self.assertEqual(left_insertion([1], 1), 0)
        self.assertEqual(left_insertion([1], 2), 1)

    def test_edge_cases(self):
        self.assertEqual(left_insertion([1, 2, 3], 1.5), 0)
        self.assertEqual(left_insertion([1, 2, 3], 3.5), 2)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            left_insertion('a', 1)
