import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):
    def test_insert_element_at_start(self):
        original_list = [1, 2, 3]
        new_list = insert_element(original_list, 0)
        self.assertEqual(new_list, [0, 1, 2, 3])

    def test_insert_element_at_end(self):
        original_list = [1, 2, 3]
        new_list = insert_element(original_list, 3)
        self.assertEqual(new_list, [1, 2, 3, 3])

    def test_insert_element_multiple_times(self):
        original_list = [1, 2, 3]
        new_list = insert_element(original_list, 1)
        new_list = insert_element(new_list, 2)
        self.assertEqual(new_list, [1, 1, 2, 2, 3])

    def test_insert_element_empty_list(self):
        original_list = []
        new_list = insert_element(original_list, 0)
        self.assertEqual(new_list, [0])

    def test_insert_element_single_element_list(self):
        original_list = [1]
        new_list = insert_element(original_list, 2)
        self.assertEqual(new_list, [1, 2])
