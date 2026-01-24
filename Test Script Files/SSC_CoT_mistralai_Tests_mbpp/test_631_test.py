import unittest
from mbpp_631_code import str
from six.moves.urllib.parse import quote
from 631_code import replace_spaces

class TestReplaceSpaces(unittest.TestCase):

    def test_normal_input(self):
        self.assertEqual(replace_spaces("Python Exercises"), "Python_Exercises")
        self.assertEqual(replace_spaces("Hello World"), "Hello_World")
        self.assertEqual(replace_spaces(""), "")

    def test_edge_and_boundary_cases(self):
        self.assertEqual(replace_spaces(" "), "_")
        self.assertEqual(replace_spaces("_"), " ")
        self.assertEqual(replace_spaces("Python_Exercises"), "Python_Exercises")
        self.assertEqual(replace_spaces("Hello_World"), "Hello_World")
        self.assertEqual(replace_spaces("Python_Exercises_"), "Python_Exercises_")
        self.assertEqual(replace_spaces("Hello_World_"), "Hello_World_")

    def test_special_cases(self):
        self.assertEqual(replace_spaces("Python Exercises"), "Python_Exercises")
        self.assertEqual(replace_spaces("PythonExercises"), "PythonExercises")
        self.assertEqual(replace_spaces("Python-Exercises"), "Python_-Exercises")
        self.assertEqual(replace_spaces("Python Exercises 123"), "Python_Exercises_123")
        self.assertEqual(replace_spaces("Python Exercises 123_"), "Python_Exercises_123_")

    def test_invalid_input(self):
        self.assertRaises(TypeError, replace_spaces, 123)
        self.assertRaises(TypeError, replace_spaces, None)
        self.assertRaises(TypeError, replace_spaces, [])
        self.assertRaises(TypeError, replace_spaces, (1, 2, 3))
        self.assertRaises(TypeError, replace_spaces, {"key": "value"})
        self.assertRaises(TypeError, replace_spaces, float("nan"))
        self.assertRaises(TypeError, replace_spaces, complex(1, 2))
