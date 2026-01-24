import unittest
from mbpp_779_code import unique_sublists

class TestUniqueSublists(unittest.TestCase):

    def test_typical_case(self):
        self.assertEqual(unique_sublists([[1, 2], [3, 4], [1, 2]]), {(1, 2): 1, (3, 4): 1})

    def test_empty_list(self):
        self.assertEqual(unique_sublists([]), {})

    def test_single_element(self):
        self.assertEqual(unique_sublists([[1]]), {(1,): 1})

    def test_duplicate_sublists(self):
        self.assertEqual(unique_sublists([[1, 2], [1, 2]]), {(1, 2): 2})

    def test_sublists_with_same_elements(self):
        self.assertEqual(unique_sublists([[1, 2], [2, 1]]), {(1, 2): 1, (2, 1): 1})

    def test_large_sublists(self):
        self.assertEqual(unique_sublists([[i for i in range(1, 1001)], [i for i in range(1001, 2001)]]), {(1, 1000): 1, (1001, 2000): 1})

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            unique_sublists(123)
