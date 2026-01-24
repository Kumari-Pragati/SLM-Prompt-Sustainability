import unittest
from mbpp_10_code import small_nnum

class TestSmallNnum(unittest.TestCase):
    def test_typical_case(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 3), [1, 2, 3])

    def test_edge_case(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 1), [1])

    def test_edge_case2(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 5), [1, 2, 3, 4, 5])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            small_nnum("hello", 3)

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            small_nnum([1, 2, 3], "hello")

    def test_edge_case3(self):
        self.assertEqual(small_nnum([-1, -2, -3, -4, -5], 3), [-5, -4, -3])

    def test_edge_case4(self):
        self.assertEqual(small_nnum([1, 2, 3, 4, 5], 0), [])
