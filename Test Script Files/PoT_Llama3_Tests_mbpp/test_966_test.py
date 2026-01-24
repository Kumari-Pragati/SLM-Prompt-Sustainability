import unittest
from mbpp_966_code import remove_empty

class TestRemoveEmpty(unittest.TestCase):
    def test_typical(self):
        self.assertEqual(remove_empty(("",)), ())
        self.assertEqual(remove_empty(("a", "b", "c")), ("a", "b", "c"))
        self.assertEqual(remove_empty(("a", "b", "c", "d")), ("a", "b", "c", "d"))

    def test_edge(self):
        self.assertEqual(remove_empty(()), ())
        self.assertEqual(remove_empty(("a")), ("a"))

    def test_corner(self):
        self.assertEqual(remove_empty(("a", "", "b")), ("a", "b"))
        self.assertEqual(remove_empty(("a", "b", "", "c")), ("a", "b", "c"))

    def test_invalid(self):
        with self.assertRaises(TypeError):
            remove_empty(None)
        with self.assertRaises(TypeError):
            remove_empty(123)
