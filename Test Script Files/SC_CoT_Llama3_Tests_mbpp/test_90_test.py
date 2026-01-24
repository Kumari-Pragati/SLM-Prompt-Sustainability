import unittest
from mbpp_90_code import len_log

class TestLenLog(unittest.TestCase):
    def test_typical_inputs(self):
        self.assertEqual(len_log([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), 3)
        self.assertEqual(len_log([['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i']]), 3)
        self.assertEqual(len_log([['j', 'k', 'l','m'], ['n', 'o', 'p', 'q'], ['r','s', 't', 'u']]), 4)

    def test_edge_cases(self):
        self.assertEqual(len_log([[]]), 0)
        self.assertEqual(len_log([['']]), 1)
        self.assertEqual(len_log([['', '']]), 2)

    def test_special_cases(self):
        self.assertEqual(len_log([['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l','m', 'n', 'o', 'p', 'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y', 'z']]), 1)

    def test_invalid_inputs(self):
        with self.assertRaises(TypeError):
            len_log(None)
        with self.assertRaises(TypeError):
            len_log(123)
