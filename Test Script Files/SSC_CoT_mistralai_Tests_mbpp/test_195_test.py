import unittest
from mbpp_195_code import MagicMock

from195_code import first

class TestFirstFunction(unittest.TestCase):

    def test_normal_input(self):
        arr = [1, 2, 3, 4, 5]
        x = 3
        n = len(arr)
        self.assertEqual(first(arr, x, n), 2)

    def test_edge_cases(self):
        arr = [1, 2, 3]
        x = 0
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

        arr = [1, 2, 3]
        x = 4
        n = len(arr)
        self.assertEqual(first(arr, x, n), -1)

        arr = [1, 2, 3]
        x = 3
        n = 0
        self.assertEqual(first(arr, x, n), -1)

    def test_boundary_conditions(self):
        arr = [1, 1, 2, 3, 4]
        x = 1
        n = len(arr)
        self.assertEqual(first(arr, x, n), 0)

        arr = [1, 1, 2, 3, 4]
        x = 2
        n = len(arr)
        self.assertEqual(first(arr, x, n), 1)

        arr = [1, 1, 2, 3, 4]
        x = 4
        n = len(arr)
        self.assertEqual(first(arr, x, n), 4)

    def test_invalid_input(self):
        arr = MagicMock()
        arr.__len__.side_effect = ValueError("Invalid array length")
        x = 1
        n = len(arr)
        with self.assertRaises(ValueError):
            first(arr, x, n)
