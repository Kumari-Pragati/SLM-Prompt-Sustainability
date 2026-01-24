import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):
    def test_normal_input(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [1, 2, 4, 3])
        self.assertEqual(insert_element([], 1), [1])
        self.assertEqual(insert_element([1], 2), [1, 2])

    def test_edge_cases(self):
        self.assertEqual(insert_element([1, 2], 0), [0, 1, 2])
        self.assertEqual(insert_element([1, 2], 3), [1, 2, 3])
        self.assertEqual(insert_element([1, 2], 4), [1, 2, 3, 4])
        self.assertEqual(insert_element([1, 2], 5), [1, 2, 3, 4, 5])

    def test_boundary_cases(self):
        self.assertEqual(insert_element([1, 2, 3, 4, 5], 0), [0, 1, 2, 3, 4, 5])
        self.assertEqual(insert_element([1, 2, 3, 4, 5], 6), [1, 2, 3, 4, 5, 6])
        self.assertEqual(insert_element([1, 2, 3, 4, 5], 7), [1, 2, 3, 4, 5, 6, 7])

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            insert_element(1, 2)
        with self.assertRaises(TypeError):
            insert_element([], 1.5)
