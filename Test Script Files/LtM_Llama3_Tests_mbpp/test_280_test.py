import unittest
from mbpp_280_code import sequential_search

class TestSequentialSearch(unittest.TestCase):
    def test_found_at_first_position(self):
        dlist = [1, 2, 3, 4, 5]
        item = 2
        found, pos = sequential_search(dlist, item)
        self.assertTrue(found)
        self.assertEqual(pos, 1)

    def test_found_at_last_position(self):
        dlist = [1, 2, 3, 4, 5]
        item = 5
        found, pos = sequential_search(dlist, item)
        self.assertTrue(found)
        self.assertEqual(pos, 4)

    def test_not_found(self):
        dlist = [1, 2, 3, 4, 5]
        item = 6
        found, pos = sequential_search(dlist, item)
        self.assertFalse(found)
        self.assertEqual(pos, 5)

    def test_empty_list(self):
        dlist = []
        item = 1
        found, pos = sequential_search(dlist, item)
        self.assertFalse(found)
        self.assertEqual(pos, 0)

    def test_single_element_list(self):
        dlist = [1]
        item = 1
        found, pos = sequential_search(dlist, item)
        self.assertTrue(found)
        self.assertEqual(pos, 0)

    def test_found_at_middle_position(self):
        dlist = [1, 2, 3, 4, 5]
        item = 3
        found, pos = sequential_search(dlist, item)
        self.assertTrue(found)
        self.assertEqual(pos, 2)
