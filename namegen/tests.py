import re
import unittest

from namegen import NameGen

class NameGenTest(unittest.TestCase):
    def test_generate(self):
        self.assertTrue(re.match(r'\w+-\w+-\d+', NameGen.generate()))
    
    def test_not_equal_in_repeated_call(self):
        self.assertNotEqual(NameGen.generate(), NameGen.generate())
    
    def test_configurable_range(self):
        # some error generation..
        self.assertTrue(re.match(r'\w+-\w+-\d$', NameGen.generate(9)))
    
    def test_drops_range_if_zero(self):
        self.assertTrue(re.match(r'\w+ \w+$', NameGen.generate(0, ' ')))
    
    def test_wrong_range(self):
        with self.assertRaises(RuntimeError):
            NameGen.generate('1')
        with self.assertRaises(RuntimeError):
            NameGen.generate(-1)
    
    def test_wrong_delimiter(self):
        with self.assertRaises(RuntimeError):
            NameGen.generate(delimiter=1)
    
    def test_wrong_digit(self):
        with self.assertRaises(RuntimeError):
            NameGen.generate(digit=3)
            NameGen.generate(token_range=999, digit=4)

if __name__ == '__main__':
    print('first result : ' + NameGen.generate())
    unittest.main()

