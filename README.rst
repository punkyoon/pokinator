==========================
pokinator
==========================
.. image:: https://travis-ci.org/punkyoon/pokinator.svg?branch=master
    :target: https://travis-ci.org/punkyoon/pokinator

.. image:: https://badge.fury.io/py/pokinator.svg
    :target: https://pypi.python.org/pypi/pokinator/1.1.2

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

License
=======

`MIT license`_

.. _MIT license: https://github.com/punkyoon/pokinator/blob/master/LICENSE

Copyright (c) 2017 punkyoon(Jiyoon Ha)
