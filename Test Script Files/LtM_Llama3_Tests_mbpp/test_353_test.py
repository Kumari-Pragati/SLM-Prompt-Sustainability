import unittest
from mbpp_353_code import remove_column

class TestRemoveColumn(unittest.TestCase):
    def test_remove_column_typical(self):
        list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        n = 1
        result = remove_column(list1, n)
        self.assertEqual(result, [[1, 3], [4, 6], [7, 9]])

    def test_remove_column_edge(self):
        list1 = []
        n = 0
        result = remove_column(list1, n)
        self.assertEqual(result, [])

    def test_remove_column_edge2(self):
        list1 = [[1, 2, 3]]
        n = 3
        result = remove_column(list1, n)
        self.assertEqual(result, [[1, 2]])

    def test_remove_column_edge3(self):
        list1 = [[1, 2, 3]]
        n = 0
        result = remove_column(list1, n)
        self.assertEqual(result, [[1, 2, 3]])

    def test_remove_column_edge4(self):
        list1 = [[1, 2, 3]]
        n = 4
        result = remove_column(list1, n)
        self.assertEqual(result, [[1, 2, 3]])

    def test_remove_column_edge5(self):
        list1 = [[1, 2, 3]]
        n = 3.5
        with self.assertRaises(TypeError):
            remove_column(list1, n)
