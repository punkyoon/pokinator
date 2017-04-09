from random import choice, randint
from pokemons import firstgen

class Pokinator:
    _name1 = firstgen._name1
    _name2 = firstgen._name2
    
    @classmethod
    def generate(self, token_range=9999, delimiter='-', digit=None):
        if not isinstance(token_range, int) or token_range < 0:
            raise RuntimeError('Token range must be a nonnegative integer')
        if not isinstance(delimiter, str):
            raise RuntimeError('Delimiter must be a string')
        
        generated = [choice(self._name1), choice(self._name2)]
        
        if digit != None:
            if not isinstance(digit, int) or (digit < 1) or (digit < len(str(token_range))):
                raise RuntimeError('Digit must be more than 0')
            format_str = '%0.' + str(digit) + 'd'
            result = format_str % randint(0, token_range)
        else:
            result = randint(0, token_range)
        generated.append(str(result))
        
        return delimiter.join(generated)

