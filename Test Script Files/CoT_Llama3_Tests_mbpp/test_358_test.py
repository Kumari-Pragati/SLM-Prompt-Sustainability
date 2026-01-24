import unittest
from mbpp_358_code import moddiv_list

class TestModdivList(unittest.TestCase):

    def test_moddiv_list_typical(self):
        self.assertEqual(moddiv_list([10, 20, 30], [2, 3, 4]), [1, 2, 0])

    def test_moddiv_list_edge(self):
        self.assertEqual(moddiv_list([10, 20, 30], [0, 0, 0]), [10, 20, 30])

    def test_moddiv_list_edge2(self):
        self.assertEqual(moddiv_list([10, 20, 30], [1, 2, 3]), [0, 1, 1])

    def test_moddiv_list_invalid_input1(self):
        with self.assertRaises(TypeError):
            moddiv_list('a', [1, 2, 3])

    def test_moddiv_list_invalid_input2(self):
        with self.assertRaises(TypeError):
            moddiv_list([1, 2, 3], 'a')

    def test_moddiv_list_invalid_input3(self):
        with self.assertRaises(TypeError):
            moddiv_list('a', 'b')
