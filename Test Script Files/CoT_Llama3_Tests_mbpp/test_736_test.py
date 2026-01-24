import unittest
from mbpp_736_code import left_insertion

class TestLeftInsertion(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 3), 2)
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 2), 1)
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 5), 4)

    def test_edge(self):
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 1), 0)
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 5), 4)
        self.assertEqual(left_insertion([1, 2, 3, 4, 5], 6), 5)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            left_insertion(None, 1)
        with self.assertRaises(TypeError):
            left_insertion([1, 2, 3, 4, 5], None)
        with self.assertRaises(TypeError):
            left_insertion([1, 2, 3, 4, 5], 'a')
