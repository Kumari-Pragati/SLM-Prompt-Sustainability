import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_tuplex((1, 2, 3, 2, 4, 2), 2), 3)

    def test_edge_case(self):
        self.assertEqual(count_tuplex((), 2), 0)
        self.assertEqual(count_tuplex((1, 2, 3, 4), None), 0)

    def test_corner_case(self):
        self.assertEqual(count_tuplex((1, 2, 3, 2, 4, 2), 1), 1)
        self.assertEqual(count_tuplex((1, 2, 3, 2, 4, 2), 5), 0)

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            count_tuplex(123, 2)
        with self.assertRaises(TypeError):
            count_tuplex((1, 2, 3), '2')
