# -- coding: utf-8 --
from re import subn
s=';;;:::'
res = subn(':', '%', s)
print(f'Result: {res[0]}\nmatches: {res[1]}')
