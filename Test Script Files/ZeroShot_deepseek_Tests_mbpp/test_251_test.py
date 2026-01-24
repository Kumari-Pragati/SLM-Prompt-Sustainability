import unittest
from mbpp_251_code import insert_element

class TestInsertElement(unittest.TestCase):

    def test_insert_element(self):
        self.assertEqual(insert_element([1, 2, 3], 4), [4, 1, 2, 3])
        self.assertEqual(insert_element(['a', 'b', 'c'], 'd'), ['d', 'a', 'b', 'c'])
        self.assertEqual(insert_element([True, False], True), [True, True, False])
        self.assertEqual(insert_element([], 5), [5])
        self.assertEqual(insert_element([1, 2, 3], 0), [0, 1, 2, 3])
