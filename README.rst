.. image:: https://travis-ci.org/IGITUGraz/sdict.svg?branch=master
    :target: https://travis-ci.org/IGITUGraz/sdict
    
==========
 The sdict
==========

The sdict package contains the classes `sdictm` and `sdict` which provide an interface
that allows for the use of attribute access syntax to access elements of a recursive
dictionary. `sdictm` is a mutable sdict whose members can be updated. sdict is an
immutable version of sdictm

Installation
============

The following command can be run from the directory containing this file in order to
install it::

    pip install https://github.com/IGITUGraz/sdict/archive/master.zip

Dependencies
============

None. Tested on Python 3.5.

Usage
=====

.. code:: python

    from sdict import sdict, sdictm
    
    d = dict(a=1, b=2, c=dict(d=3))
    
    # sdict is the immutable version
    sd = sdict(d)
    print(sd.a)  # -> prints 1
    print(sd.c.d)  # -> prints 3
    
    # sdictm is the mutable version
    sd = sdictm(d)
    sd.a = 4  # -> a is now 4
