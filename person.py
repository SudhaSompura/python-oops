#!/usr/bin/python

### Copyright Cloud Infra ###

import sys

class Person():
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age


    def get_name(self):
        return '{} {}'.format(self.first, self.last)

def main(args):
    p1 = Person('Sudha', 'Sompura', 24)
    p2 = Person('Lakshmi', 'Gonsalves', 28)

    print p1.get_name()
    print p2.get_name()


if __name__=='__main__':
    main(sys.argv)

