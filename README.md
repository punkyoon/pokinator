# namegen

## Introduction

Heroku like random pokemon name generator for python.

There is an pokemon name list and it generate random name joining them by user provided delimiter.

And can generate `n-digit` random number.

## Install

using pip:

`$ pip install namegen`

## Guide

```python
from namegen import NameGen

NameGen.generate()    # 'munchlax-snorlax-2910'
NameGen.generate(9)    # 'ditto-pikachu-4' ; token_range=9
NameGen.generate(delimiter='*')    # 'eevee*zubet*312'
NameGen.generate(token_range=999, digit=3)    # 'goomy-onix-021'
```

## License

[MIT license](https://github.com/punkyoon/namegen/blob/master/LICENSE)

Copyright (c) 2017 punkyoon(Jiyoon Ha)

