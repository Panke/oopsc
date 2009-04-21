# coding: utf-8

"""
This module offers lexing capabilities for the OOPS programming language.
It's designed closely after the original OOPS compiler written in Java
by Thomas Röfer
"""

import re

keywords = ['BEGIN', 'END', 'CLASS', 'IS', 'METHOD', 'READ', 'WRITE',
            'IF', 'THEN', 'ELSE', 'WHILE', 'DO', 'MOD', 'NEW', 'SELF',
            'NULL', 'TRUE', 'FALSE']

#operators
ops = {'.' : 'PERIOD', ';' : 'SEMICOLON', ',' : 'COMMA', ')' : 'RPAREN',
       '(' : 'LPAREN', '=' : 'EQ', '#' : 'NEQ', '>' : 'GT', '+' : 'PLUS',
       '-' : 'MINUS', '*' : 'TIMES', '/' : 'DIV', ':' : 'COLON', '<' : 'LT'
       }
#operators with len == 2
long_ops = {':' : ('=', 'BECOMES'), '>' : ('=', 'GTEQ'), '<' : ('=', 'LTEQ')}


whitespace = re.compile('\s')
letter = re.compile('[a-zA-Z]')
letter_or_digit = re.compile('[a-zA-Z0-9]')
digit = re.compile('[0-9]')

class Stream(unicode):
    def __init__(self, source, encoding='utf8', errors='strict'):
        unicode.__init__(self, source, encoding, errors)
        self.position = (0, 0)
        self._iter = iter(self)

    def __next__(self):
        c = self._iter.next()
        x, y = self.position
        self.position = (x+1, 0) if c == '\n' else (x, y+1)
        return c
    def next(self):
        return self.__next__()

class Token(object):
    """
    Represents a token of OOPS.
    It is essentialy a tuple of (TokenID, position, value).
    """

    def __init__(self, id, pos, value=None):
        """
        The initializer.
        id is a token id, one of the global id field.
        pos should be a sequenz like (x, y) and value
        the string representation of the number or identifier
        """
        
        self.id = id
        self.position = pos
        self.value = value

    def __str__(self):
        return "%s: %s at %s" % (self.id, self.value, self.position)

def lex(source):
    """
    Lexical analysis the source and return the found tokens.
    Source should be the source code as a unicode string.
    """

    # count the number of '{' to allow nested comments
    comment_count = 0
    
    char_stream = Stream(source)
    try:
        c = char_stream.next()
        while True:
            #ignore whitespace
            if whitespace.match(c):
                c = char_stream.next()

            #ignore comments    
            elif c == '{':
                comment_count += 1
                while(comment_count != 0):
                    c = char_stream.next()
                    if c == '{':
                        comment_count += 1
                    elif c == '}':
                        comment_count -= 1
                c = char_stream.next()

            elif c == '|':
                while(c != '\n'):
                    c = char_stream.next()
                    
            #identifiers and keywords
            elif letter.match(c):
                # read the hole word
                word = c
                c = char_stream.next()
                while letter_or_digit.match(c):
                    word += c
                    c = char_stream.next()
                # check if its an keyword
                if word in keywords:
                    yield Token(word, char_stream.position)
                else:
                    yield Token('IDENT', char_stream.position, word)

                # no need to read the next character. Already done in the
                # while loop

            # integers / numbers
            elif digit.match(c):
                #read the hole number
                word = c
                c = char_stream.next()
                while digit.match(c):
                    word += c
                    c = char_stream.next()
                yield Token('NUMBER', char_stream.position, int(word))

            #operators

            elif c in ops:
                yield Token(ops[c], char_stream.position)
                c = char_stream.next()
                
            elif c in long_ops:
                # only handle the special case that no two long operators
                # start with the same symbol
                
                op = long_ops[c]
                next_one = char_stream.next()
                # is next_one equal to the second char of the op?
                if next_one == op[0]: 
                    yield Token(op[1], char_stream.position)
                    c = char_stream.next()
                
                else:
                    raise UnexpectedSymbol(c, char_stream.position)
                    
                
            else:
                raise UnexpectedSymbol(c, char_stream.position)
    except StopIteration:
        yield Token('EOF', char_stream.position)

                
        
      
