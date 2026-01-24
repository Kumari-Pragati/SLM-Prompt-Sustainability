import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_simple_input(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 4, 3])
        self.assertEqual(insert_element([], 1), [1])
        self.assertEqual(insert_element([1], 2), [1, 2])

    def test_edge_cases(self):
        self.assertEqual(insert_element([1, 2, 3], 0), [0, 1, 2, 3])
        self.assertEqual(insert_element([1, 2, 3], [4, 5]), [1, 2, 4, 5, 3])
        self.assertEqual(insert_element([1, 2, 3], None), [None, 1, 2, 3])

    def test_complex_cases(self):
        self.assertEqual(insert_element([1, 2, [3, 4]], 5), [1, 2, [3, 4, 5], 3])
        self.assertEqual(insert_element([1, [2, 3]], 4), [1, [2, 3, 4]])
        self.assertEqual(insert_element([[1, 2], 3], 4), [[1, 2], 3, 4])
