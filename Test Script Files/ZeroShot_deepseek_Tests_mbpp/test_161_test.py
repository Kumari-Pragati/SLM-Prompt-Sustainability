import unittest
from mbpp_161_code import remove_elements

class TestRemoveElements(unittest.TestCase):

    def test_remove_elements(self):
        self.assertEqual(remove_elements([1, 2, 3, 4], [2, 4]), [1, 3])
        self.assertEqual(remove_elements(['a', 'b', 'c'], ['b', 'c']), ['a'])
        self.assertEqual(remove_elements([1, 2, 2, 3, 4, 2], [2]), [1, 3, 4])
        self.assertEqual(remove_elements([], [1, 2, 3]), [])
        self.assertEqual(remove_elements([1, 2, 3, 4], []), [1, 2, 3, 4])
