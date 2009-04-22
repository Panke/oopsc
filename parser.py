# coding: utf-8 

"""
This module implements the parser for OOPS. It's main entry point is
the function ''parse'' which takes a stream of tokens and returns
the abstract syntax tree of the program or raises an InvalidSyntaxError.
"""
        
def parse(stream):
    # Every simple OOPS/0 program starts with the declartion of the
    # main class
    class_decl(stream)
    symbol('EOF')
