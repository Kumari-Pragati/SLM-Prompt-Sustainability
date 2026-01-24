import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5, 6)), [(2, 4), (3, 5), (1, 6)])

    def test_edge_case1(self):
        self.assertEqual(zip_tuples((1, 2), (3, 4)), [(2, 3), (1, 4)])

    def test_edge_case2(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5)), [(2, 4), (3, 5), (1, 4)])

    def test_edge_case3(self):
        self.assertEqual(zip_tuples((1, 2), (3)), [(2, 3)])

    def test_edge_case4(self):
        self.assertEqual(zip_tuples((), (4, 5, 6)), [])

    def test_edge_case5(self):
        self.assertEqual(zip_tuples((1, 2, 3), ()), [])

    def test_error_case1(self):
        with self.assertRaises(TypeError):
            zip_tuples(1, (4, 5, 6))

    def test_error_case2(self):
        with self.assertRaises(TypeError):
            zip_tuples((1, 2, 3), 4)
