import re
import unittest

from namegen import NameGen

class NameGenTest(unittest.TestCase):
    def test_generate(self):
        self.assertTrue(re.match(r'\w+-\w+-\d+', NameGen.generate()))
    
    def test_not_equal_in_repeated_call(self):
        self.assertNotEqual(NameGen.generate(), NameGen.generate())
    
    def test_configurable_range(self):
        self.assertTrue(re.match(r'\w+-\w+-\d$', NameGen.generate(9)))
    
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
    print('#1 value test : ' + NameGen.generate())
    print('#2 value test : ' + NameGen.generate(9))
    print('#3 value test : ' + NameGen.generate(delimiter='*'))
    print('#4 value test : ' + NameGen.generate(token_range=999, digit=3))
    
    unittest.main()

