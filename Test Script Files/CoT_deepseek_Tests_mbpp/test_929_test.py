import unittest
from mbpp_929_code import count_tuplex

class TestCountTuplex(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(count_tuplex((1, 2, 2, 3, 4, 2), 2), 3)

    def test_single_value(self):
        self.assertEqual(count_tuplex((1,), 1), 1)
        self.assertEqual(count_tuplex((1,), 2), 0)

    def test_empty_tuplex(self):
        self.assertEqual(count_tuplex((), 1), 0)

    def test_no_value(self):
        self.assertEqual(count_tuplex((1, 2, 3), None), 0)

    def test_large_tuplex(self):
        tuplex = tuple(range(1, 10001))
        self.assertEqual(count_tuplex(tuplex, 5000), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            count_tuplex(123, 2)
        with self.assertRaises(TypeError):
            count_tuplex((1, 2, 3), 'a')
