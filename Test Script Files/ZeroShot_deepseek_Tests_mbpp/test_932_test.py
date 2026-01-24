import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_remove_duplic_list(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 4, 4, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplic_list(['a', 'b', 'b', 'c', 'd', 'd', 'e']), ['a', 'b', 'c', 'd', 'e'])
        self.assertEqual(remove_duplic_list([True, False, False, True]), [True, False])
        self.assertEqual(remove_duplic_list([]), [])
        self.assertEqual(remove_duplic_list([1]), [1])
