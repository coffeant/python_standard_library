#!/usr/bin/env python

import os
import sys 
import random

def shuffle(source, to):
    with open('./nameinfo.txt','r') as source:
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open('./nameinfo_shuffle.txt','w') as target:
        for _, line in data:
            target.write(line)


if __name__ == '__main__':
    _from = 'nameinfo.txt'
    _to = 'nameinfo_shuffle.txt'
    shuffle(_from , _to)
