import unittest
from mbpp_625_code import len
from six.moves.range import range

class TestSwapList(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(swap_List([]), [])

    def test_single_element_list(self):
        for element in [1, 'a', (1, 2, 3)]:
            self.assertEqual(swap_List([element]), [element])

    def test_two_elements_list(self):
        for element1 in [1, 'a', (1, 2, 3)]:
            for element2 in [2, 'b', (2, 3, 4)]:
                self.assertEqual(swap_List([element1, element2]), [element2, element1])

    def test_multiple_elements_list(self):
        for elements in [
            [1, 2, 3],
            ['a', 'b', 'c'],
            [(1, 2, 3), (4, 5, 6)]
        ]:
            reversed_elements = elements[::-1]
            self.assertEqual(swap_List(elements), reversed_elements)

    def test_negative_index(self):
        self.assertEqual(swap_List([1, 2, 3]), [3, 1])
        self.assertEqual(swap_List([-1, -2, -3]), [-3, -1])

    def test_list_with_duplicates(self):
        self.assertEqual(swap_List([1, 1, 2]), [2, 1, 1])
        self.assertEqual(swap_List(['a', 'a', 'b']), ['b', 'a', 'a'])

    def test_list_with_non_iterable_element(self):
        self.assertRaises(TypeError, swap_List, [1, 2, 3, 'non_iterable_object'])
