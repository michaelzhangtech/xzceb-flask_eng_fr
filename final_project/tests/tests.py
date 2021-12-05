import unittest
from ..machinetranslation.translator import englishToFrench,frenchToEnglish 

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self):         
        self.assertEqual(englishToFrench('Hello'), 'Bonjour') 
        self.assertNotEqual(englishToFrench("Hello"), 'bon') 

class TestFrenchToEnglish(unittest.TestCase): 
    def test2(self): 
        self.assertEqual(frenchToEnglish('Bonjour'), 'Hello') 
        self.assertNotEqual(englishToFrench("Bonjour"), 'hel') 

unittest.main()