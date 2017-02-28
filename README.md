# pokinator

[![Build Status](https://travis-ci.org/punkyoon/pokinator.svg?branch=master)](https://travis-ci.org/punkyoon/pokinator) [![PyPI version](https://badge.fury.io/py/pokinator.svg)](https://pypi.python.org/pypi/pokinator/1.0)

## Introduction

Heroku like random pokemon name generator for python.

There is an pokemon name list and it generate random name joining them by user provided delimiter.

And can generate `n-digit` random number.

## Install

using pip:

`$ pip install pokinator`

## Guide

```python
from pokinator import Pokinater

Pokinator.generate()    # 'munchlax-snorlax-2910'
Pokinator.generate(9)    # 'ditto-pikachu-4' ; token_range=9
Pokinator.generate(delimiter='*')    # 'eevee*zubet*312'
Pokinator.generate(token_range=999, digit=3)    # 'goomy-onix-021'
```

## License

[MIT license](https://github.com/punkyoon/pokinator/blob/master/LICENSE)

Copyright (c) 2017 punkyoon(Jiyoon Ha)

