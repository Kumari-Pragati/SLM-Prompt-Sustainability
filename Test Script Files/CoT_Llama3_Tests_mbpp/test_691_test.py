import unittest
from mbpp_691_code import group_element

class TestGroupElement(unittest.TestCase):
    def test_group_element(self):
        self.assertEqual(group_element([("a", 1), ("b", 1), ("c", 2), ("d", 2)]), {1: ['a', 'b'], 2: ['c', 'd']})
        self.assertEqual(group_element([("a", 1), ("b", 1), ("c", 1), ("d", 1)]), {1: ['a', 'b', 'c', 'd']})
        self.assertEqual(group_element([("a", 1), ("b", 2), ("c", 2), ("d", 3)]), {1: ['a'], 2: ['b', 'c'], 3: ['d']})
        self.assertEqual(group_element([]), {})
        self.assertEqual(group_element([("a", 1), ("b", 1)]), {1: ['a', 'b']})
