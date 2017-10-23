==========================
pokinator
==========================
.. image:: https://travis-ci.org/punkyoon/pokinator.svg?branch=master
    :target: https://travis-ci.org/punkyoon/pokinator

.. image:: https://badge.fury.io/py/pokinator.svg
    :target: https://pypi.python.org/pypi/pokinator/1.2.0

Introduction
============

Heroku like random pokemon name generator for python.

There is an pokemon name list and it generate random name joining them by user provided delimiter.

And can generate ``n-digit`` random number.

Install
=======

using pip::

    $ pip install pokinator

Guide
=====

.. code-block:: python

    from pokinator import Pokinator
    
    Pokinator.generate()                            # 'Wigglytuff-Snorlax-2910'
    Pokinator.generate(9)                           # 'Ditto-Pikachu-4' ; token_range=9
    Pokinator.generate(delimiter='*')               # 'Eevee*Zubat*312'
    Pokinator.generate(token_range=999, digit=3)    # 'Diglett-Onix-021'
    Pokinator.generate(generation=2)                # 'Mareep-Piloswine-5034'
    Pokinator.generate(lowercase=True)              # 'dugtrio-marowak-3121'

    # you can also force the same output
    # for a given generation sequence
    import random
    random.seed(5)
    Pokinator.generate()                           # 'Pidgey-Farfetchd-6594'
    Pokinator.generate()                           # 'Vileplume-Jynx-3548'

License
=======

`MIT license`_

.. _MIT license: https://github.com/punkyoon/pokinator/blob/master/LICENSE

Copyright (c) 2017 punkyoon(Jiyoon Ha)
