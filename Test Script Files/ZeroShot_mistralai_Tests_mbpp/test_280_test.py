import unittest
from mbpp_280_code import List

def sequential_search(dlist: List[any], item: any) -> tuple[bool, int]:
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos = pos + 1
    return found, pos

class TestSequentialSearch(unittest.TestCase):

    def test_empty_list(self):
        self.assertFalse(sequential_search([], 1))

    def test_single_item(self):
        self.assertTrue(sequential_search([1], 1))
        self.assertEqual(sequential_search([1], 2), (False, len([1])))

    def test_multiple_items(self):
        self.assertTrue(sequential_search([1, 2, 3, 4, 5], 3))
        self.assertFalse(sequential_search([1, 2, 3, 4, 5], 6))
        self.assertEqual(sequential_search([1, 2, 3, 4, 5], 1), (True, 0))
        self.assertEqual(sequential_search([1, 2, 3, 4, 5], 5), (True, 4))
