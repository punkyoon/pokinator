import re
import unittest

from pokinator import Pokinator

class NameGenTest(unittest.TestCase):
    def test_generate(self):
        self.assertTrue(re.match(r'\w+-\w+-\d+', Pokinator.generate()))
    
    def test_not_equal_in_repeated_call(self):
        self.assertNotEqual(Pokinator.generate(), Pokinator.generate())
    
    def test_configurable_range(self):
        self.assertTrue(re.match(r'\w+-\w+-\d$', Pokinator.generate(9)))
    
    def test_wrong_range(self):
        with self.assertRaises(RuntimeError):
            Pokinator.generate('1')
        with self.assertRaises(RuntimeError):
            Pokinator.generate(-1)
    
    def test_wrong_delimiter(self):
        with self.assertRaises(RuntimeError):
            Pokinator.generate(delimiter=1)
    
    def test_wrong_digit(self):
        with self.assertRaises(RuntimeError):
            Pokinator.generate(digit=3)
            Pokinator.generate(token_range=999, digit=4)

if __name__ == '__main__':
    print('#1 value test : ' + Pokinator.generate())
    print('#2 value test : ' + Pokinator.generate(9))
    print('#3 value test : ' + Pokinator.generate(delimiter='*'))
    print('#4 value test : ' + Pokinator.generate(token_range=999, digit=3))
    
    unittest.main()

