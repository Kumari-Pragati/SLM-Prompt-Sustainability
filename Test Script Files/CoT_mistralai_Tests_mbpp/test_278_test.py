import unittest
from mbpp_278_code import count_first_elements

class TestCountFirstElements(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(count_first_elements([]), 0)

    def test_single_element(self):
        self.assertEqual(count_first_elements([1]), 0)
        self.assertEqual(count_first_elements([(1, 2)]), 0)
        self.assertEqual(count_first_elements([(1, 2), 1]), 0)

    def test_multiple_elements(self):
        self.assertEqual(count_first_elements([1, 2]), 0)
        self.assertEqual(count_first_elements([(1, 2), 1, 2]), 1)
        self.assertEqual(count_first_elements([(1, 2), (3, 4), 1, 2]), 0)

    def test_tuple_as_first_element(self):
        self.assertEqual(count_first_elements([(1, 2)]), 0)
        self.assertEqual(count_first_elements([(1, 2), (1, 2)]), 0)

    def test_list_of_tuples(self):
        self.assertEqual(count_first_elements([(1, 2), (3, 4)]), 0)
        self.assertEqual(count_first_elements([(1, 2), (3, 4), (1, 2)]), 0)

    def test_list_of_mixed_types(self):
        self.assertEqual(count_first_elements([1, (1, 2), 3]), 0)
        self.assertEqual(count_first_elements([(1, 2), 1, (3, 4)]), 1)

    def test_invalid_input(self):
        self.assertRaises(TypeError, count_first_elements, [1, 'a'])
        self.assertRaises(TypeError, count_first_elements, ['a', 1])
        self.assertRaises(TypeError, count_first_elements, [1, [1, 2]])
