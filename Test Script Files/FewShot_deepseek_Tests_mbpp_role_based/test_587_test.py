import unittest
from mbpp_587_code import list_tuple

class TestListTuple(unittest.TestCase):
    def test_typical_use_case(self):
        listx = [1, 2, 3, 4, 5]
        expected_output = (1, 2, 3, 4, 5)
        self.assertEqual(list_tuple(listx), expected_output)

    def test_empty_list(self):
        listx = []
        expected_output = ()
        self.assertEqual(list_tuple(listx), expected_output)

    def test_single_element_list(self):
        listx = [1]
        expected_output = (1,)
        self.assertEqual(list_tuple(listx), expected_output)

    def test_invalid_input(self):
        listx = "not a list"
        with self.assertRaises(TypeError):
            list_tuple(listx)
