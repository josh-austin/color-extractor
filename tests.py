import unittest
from extract import Extractor

class ExtractorTest(unittest.TestCase):
    def setUp(self):
        self.extractor = Extractor()
        f = open('test.css')
        self.lines = f.readlines()
        f.close()        
        self.converted = list(self.extractor.scan(self.lines))
        
    def test_scan(self):        
        self.assertEqual(len(self.lines) + 1, len(self.converted))
        
    def test_find_variable_name(self):
        self.assertEqual('@var1', self.extractor.find_variable_name('#FFF;'))
        self.assertEqual('@var2', self.extractor.find_variable_name('#E83E26;'))
        self.assertEqual(None, self.extractor.find_variable_name('#000'))
    
    def test_get_variables(self):
        self.assertEqual(2, len(list(self.extractor.get_variables())))
 
if __name__ == '__main__':
    unittest.main()