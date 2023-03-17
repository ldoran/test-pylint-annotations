import urllib
import json
from itertools import (
    chain,
    combinations,
    cycle,
    groupby,
    ifilter,
    ifilterfalse,
    imap,
    izip,
    tee,
    takewhile,
    starmap,
)


def first_function(a, b, c, d=None):
    return (a + b + d)

def second_function():
    return "testing" # a test



def third_function(first_arg, second_arg, third_arg, fourth_arg, fifth_arg, sixth_arg, seventh_arg, eighth_arg):
    return 5


def fourthFunction(first_arg, second_arg, third_arg, fourth_arg, fifth_arg, sixth_arg, seventh_arg, eighth_arg):
    return first_arg + second_arg + third_arg + fourth_arg + fifth_arg+sixth_arg + seventh_arg + eighth_arg
    return first_arg


