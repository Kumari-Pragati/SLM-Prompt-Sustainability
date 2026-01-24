import unittest
from mbpp_932_code import remove_duplic_list

class TestRemoveDuplicList(unittest.TestCase):

    def test_remove_duplic_list(self):
        self.assertEqual(remove_duplic_list([1, 2, 2, 3, 4, 4, 5, 6, 6]), [1, 2, 3, 4, 5, 6])
        self.assertEqual(remove_duplic_list(['a', 'b', 'b', 'c', 'd', 'd', 'e', 'f', 'f']), ['a', 'b', 'c', 'd', 'e', 'f'])
        self.assertEqual(remove_duplic_list([1, 1, 2, 2, 3, 3, 4, 4, 5, 5]), [1, 2, 3, 4, 5])
        self.assertEqual(remove_duplic_list([]), [])
        self.assertEqual(remove_duplic_list([1]), [1])
        self.assertEqual(remove_duplic_list([1, 1, 1, 1]), [1])
        self.assertEqual(remove_duplic_list([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_remove_duplic_list_edge_case(self):
        self.assertEqual(remove_duplic_list([1, 1, 1, 1, 1]), [1])

    def test_remove_duplic_list_invalid_input(self):
        with self.assertRaises(TypeError):
            remove_duplic_list(None)
        with self.assertRaises(TypeError):
            remove_duplic_list('')
