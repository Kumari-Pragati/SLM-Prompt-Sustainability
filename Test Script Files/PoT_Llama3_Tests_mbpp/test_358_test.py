import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(moddiv_list([10, 20, 30], [2, 3, 4]), [1, 2, 0])

    def test_edge(self):
        self.assertEqual(moddiv_list([10, 20, 30], [1, 2, 3]), [0, 0, 0])
        self.assertEqual(moddiv_list([10, 20, 30], [4, 4, 4]), [0, 0, 0])

    def test_invalid(self):
        with self.assertRaises(TypeError):
            moddiv_list('a', [1, 2, 3])
        with self.assertRaises(TypeError):
            moddiv_list([1, 2, 3], 'a')

    def test_empty(self):
        self.assertEqual(moddiv_list([], []), [])

    def test_single(self):
        self.assertEqual(moddiv_list([10], [2]), [0])
        self.assertEqual(moddiv_list([10], []), [])
