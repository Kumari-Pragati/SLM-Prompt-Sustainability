import unittest
from mbpp_642_code import remove_similar_row

class TestRemoveSimilarRow(unittest.TestCase):

    def test_typical_case(self):
        test_list = [[1, 2, 3], [2, 1, 3], [3, 2, 1]]
        self.assertEqual(remove_similar_row(test_list), {(1, 2, 3)})

    def test_empty_list(self):
        test_list = []
        self.assertEqual(remove_similar_row(test_list), set())

    def test_single_element(self):
        test_list = [[1]]
        self.assertEqual(remove_similar_row(test_list), {(1,)})

    def test_duplicate_rows(self):
        test_list = [[1, 2, 3], [1, 2, 3], [3, 2, 1]]
        self.assertEqual(remove_similar_row(test_list), {(1, 2, 3)})

    def test_large_list(self):
        test_list = [[i%3 for i in range(1000)]]
        self.assertEqual(remove_similar_row(test_list), {(0, 1, 2)})

    def test_mixed_types(self):
        test_list = [['a', 1, 2.0], [1, 'a', 2.0], [2.0, 1, 'a']]
        self.assertEqual(remove_similar_row(test_list), {('a', 1, 2.0)})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_similar_row(123)
