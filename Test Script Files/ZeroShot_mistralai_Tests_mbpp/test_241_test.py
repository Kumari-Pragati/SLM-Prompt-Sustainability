import unittest
from mbpp_241_code import array_3d

class TestArray3D(unittest.TestCase):

    def test_empty_array(self):
        expected = []
        result = array_3d(0, 0, 0)
        self.assertEqual(expected, result)

    def test_single_row(self):
        expected = [['*'] * 3 for _ in range(3)]
        result = array_3d(3, 1, 1)
        self.assertEqual(expected, result)

    def test_single_column(self):
        expected = [['*'] for _ in range(3)]
        result = array_3d(1, 3, 3)
        self.assertEqual(expected, result)

    def test_multiple_rows_columns(self):
        expected = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
        result = array_3d(3, 3, 1)
        self.assertEqual(expected, result)
