import unittest
from mbpp_748_code import capital_words_spaces

class TestCapitalWordsSpaces(unittest.TestCase):

    def test_normal_case(self):
        self.assertEqual(capital_words_spaces("HelloWorld"), "Hello World")
        self.assertEqual(capital_words_spaces("PythonIsFun"), "Python Is Fun")
        self.assertEqual(capital_words_spaces("JavaScriptRocks"), "JavaScript Rocks")

    def test_edge_cases(self):
        self.assertEqual(capital_words_spaces(""), "")
        self.assertEqual(capital_words_spaces("A"), "A "
                         )
        self.assertEqual(capital_words_spaces("Z"), "Z "
                         )
        self.assertEqual(capital_words_spaces("Aa"), "A a"
                         )
        self.assertEqual(capital_words_spaces("Zz"), "Z z"
                         )

    def test_boundary_cases(self):
        self.assertEqual(capital_words_spaces("HelloWorld!"), "Hello World!"
                         )
        self.assertEqual(capital_words_spaces("PythonIsFun!"), "Python Is Fun!"
                         )
        self.assertEqual(capital_words_spaces("JavaScriptRocks!"), "JavaScript Rocks!"
                         )
        self.assertEqual(capital_words_spaces("HelloWorld123"), "Hello World 123"
                         )
        self.assertEqual(capital_words_spaces("PythonIsFun123"), "Python Is Fun 123"
                         )
        self.assertEqual(capital_words_spaces("JavaScriptRocks123"), "JavaScript Rocks 123"
                         )

    def test_special_cases(self):
        self.assertEqual(capital_words_spaces("HeLLoWoRlD"), "He LLo Wo Rl D"
                         )
        self.assertEqual(capital_words_spaces("PyThOnIsFun"), "Py Th On Is Fun"
                         )
        self.assertEqual(capital_words_spaces("JavaScRiptRoCKs"), "Java Sc Ript Ro Cks"
                         )
