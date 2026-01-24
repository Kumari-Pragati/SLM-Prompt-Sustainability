import unittest
from mbpp_81_code import zip_tuples

class TestZipTuples(unittest.TestCase):

    def test_typical(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5, 6)), [(3, 6), (2, 5), (1, 4)])

    def test_edge1(self):
        self.assertEqual(zip_tuples((1, 2, 3), (4, 5)), [(3, 5), (2, 4)])

    def test_edge2(self):
        self.assertEqual(zip_tuples((1, 2), (3, 4, 5)), [(2, 5), (1, 4)])

    def test_edge3(self):
        self.assertEqual(zip_tuples((), (1, 2, 3)), [])

    def test_edge4(self):
        self.assertEqual(zip_tuples((1, 2, 3), ()), [])

    def test_edge5(self):
        self.assertEqual(zip_tuples((1, 2), (1, 2)), [(2, 2), (1, 1)])

    def test_edge6(self):
        self.assertEqual(zip_tuples((1, 2, 3), (1, 2, 3)), [(3, 3), (2, 2), (1, 1)])

    def test_invalid_input1(self):
        with self.assertRaises(TypeError):
            zip_tuples('a', (1, 2, 3))

    def test_invalid_input2(self):
        with self.assertRaises(TypeError):
            zip_tuples((1, 2, 3), 'a')

    def test_invalid_input3(self):
        with self.assertRaises(TypeError):
            zip_tuples(None, (1, 2, 3))

    def test_invalid_input4(self):
        with self.assertRaises(TypeError):
            zip_tuples((1, 2, 3), None)
