import unittest
from mbpp_941_code import count_elim

class TestCountElim(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(count_elim([]), 1)

    def test_single_element(self):
        self.assertEqual(count_elim([1]), 1)
        self.assertEqual(count_elim([(1, 2)]), 0)

    def test_multiple_elements(self):
        self.assertEqual(count_elim([1, 2, 3]), 3)
        self.assertEqual(count_elim([(1, 2), 3]), 1)
        self.assertEqual(count_elim([1, (2, 3)]), 2)

    def test_list_with_tuple(self):
        self.assertEqual(count_elim([(1, 2), (3, 4)]), 2)

    def test_list_with_invalid_input(self):
        self.assertRaises(TypeError, count_elim, [1, "2", (1, 2)])
        self.assertRaises(TypeError, count_elim, [(1, 2), 3, "4"])
