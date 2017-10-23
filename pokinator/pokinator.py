# -*- coding: utf-8 -*-

import re
from random import choice, randint
from .pokemons import firstgen
from .pokemons import secondgen
from .pokemons import thirdgen
from .pokemons import fourthgen
from .pokemons import fifthgen
from .pokemons import sixthgen
from .pokemons import seventhgen

RE_DASH = re.compile('-+')
RE_WORD = re.compile('[\W_]+')


class Pokinator:
    @classmethod
    def generate(self, token_range=9999, delimiter='-', digit=None, generation=1, lowercase=False):
        if not isinstance(token_range, int) or token_range < 0:
            raise RuntimeError('Token range must be a nonnegative integer')
        if not isinstance(delimiter, str):
            raise RuntimeError('Delimiter must be a string')

        if generation == 1:
            _name1 = firstgen._name1
            _name2 = firstgen._name2
        elif generation == 2:
            _name1 = secondgen._name1
            _name2 = secondgen._name2
        elif generation == 2:
            _name1 = secondgen._name1
            _name2 = secondgen._name2
        elif generation == 3:
            _name1 = thirdgen._name1
            _name2 = thirdgen._name2
        elif generation == 4:
            _name1 = fourthgen._name1
            _name2 = fourthgen._name2
        elif generation == 5:
            _name1 = fifthgen._name1
            _name2 = fifthgen._name2
        elif generation == 6:
            _name1 = sixthgen._name1
            _name2 = sixthgen._name2
        elif generation == 7:
            _name1 = seventhgen._name1
            _name2 = seventhgen._name2
        else:
            raise RuntimeError('Only generations 1-7 are supported, {0} specified'.format(generation))

        generated = [choice(_name1), choice(_name2)]
        generated = [RE_DASH.sub('', RE_WORD.sub('', g)) for g in generated]

        if digit is not None:
            if not isinstance(digit, int) or (digit < 1) or (digit < len(str(token_range))):
                raise RuntimeError('Digit must be more than 0')
            format_str = '%0.' + str(digit) + 'd'
            result = format_str % randint(0, token_range)
        else:
            result = randint(0, token_range)
        generated.append(str(result))

        result = delimiter.join(generated)
        if lowercase is True:
            result = result.lower()
        return result
