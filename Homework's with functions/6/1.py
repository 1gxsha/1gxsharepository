# -- coding: utf-8 --
from re import subn
def GSH(s):
    s=';;;:::'
    res = subn(':', '%', s)
GSH(GSH(input()))
