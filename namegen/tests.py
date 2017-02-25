import re
import unitest

from generate import Namegen

class NamegenTest(unittest.TestCase):
    def test_generate(self):
	    self.assertTrue(re.match(r'\w+-\w+-\d+', generate())
	
	def test_not_equal_in_repeated_call(self):
	    self.assertNotEqual(generate(), generate())
	
	def test_configurable_range(self):
	    self.assertTrue(re.match(r'\w+-\w+-\d$', generate(9))
	
	def test_drops_range_if_zero(self):
	    self.assertTrue(re.match(r'\w+ \w+$', generate(0, ' '))
	
	def test_wrong_range(self):
	    with self.assertRaises(RuntimeError):
		    generate('1')
		with self.assertRaises(RuntimeError):
		    generate(-1)
	
	def test_wrong_delimiter(self):
	    with self.assertRaises(RuntimeError):
		    generate(delimiter=1)
	
	def test_wrong_digit(self):
	    with self.assertRaises(RuntimeError):
		    generate(digit=3)
			generate(token_range=999, digit=4)

if __name__ == '__main__':
	unittest.main()

