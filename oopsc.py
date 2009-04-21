#!/usr/bin/env python
# coding: utf-8 

import sys, os, logging
from optparse import OptionParser
import lexer


def generate_parser():
    usage = "%prog [options] source [dest]"
    parser = OptionParser(usage=usage)

    parser.add_option("-c", "--print-context", dest="p_context",
                      action="store_true", default=False,
                      help='print the outcome of the context analysis')

    parser.add_option('--heapsize', dest="heapsize", action='store',
                      type='int', default=100, metavar='LONGWORDS',
                      help='set the size of the heap to x LONGWORDS (4 Byte)')

    parser.add_option('--stacksize', dest='stacksize', action='store',
                      type='int', default=50, metavar='LONGWORDS',
                      help='set the size of the stack to x LONDWORDS (4 Byte)')

    parser.add_option('-i', '--print-identifier', dest='p_identifier',
                      action='store_true', default=False, help='print the '
                      'identifier map')

    parser.add_option('-I', '--print-lexical', dest='p_lexical',
                      action='store_true', default=False,
                      help='print the outcome of the lexical analysis')

    parser.add_option('-s', '--print-syntax', dest='p_syntax',
                      action='store_true', default=False,
                      help='print the outcome of the syntax analysis')

    return parser
    

if __name__ == '__main__':
    parser = generate_parser()
    options, args = parser.parse_args()

