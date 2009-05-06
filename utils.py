# coding: utf-8

from errors import UnexpectedToken

class Stream(object):
    """
    This class is a thin wrapper around an iterable, which offers the ability
    to look at (seek) the next element
    """

    def __init__(self, iterable, end_of_line='\n'):
        self.stack = []
        self._iter = iter(iterable)
        self.position = (0,0)
        self.newline = end_of_line
        
    def __next__(self):
        n = self.stack.pop() if self.stack else self._iter.next()
        x,y = self.position
        self.position = (x+1, 0) if n == self.newline else (x, y+1)
        return n

    def next(self):
        
        n = self.__next__()
        return n

    def seek(self):
        # reteurn the first element on the stack (index = -1)
        if self.stack:
            return self.stack[-1]
        else:
            # nothing on the stack, read the next one and put it on the stack
            # so the next call to next() will return this object to
            s = self.next()
            self.stack.append(s)
            return s

    def __iter__(self):
        return self._iter


class TokenStream(Stream):
    
    def keyword(self, kw):
        import grammar
        next = self.next()
        if next in grammar.keywords and next == kw:
            return next
        else:
            raise UnexpectedToken(next, 'Expected Keyword: ' + kw)

    def identifier(self):
        next = self.next()
        if next.id == 'IDENT':
            return next
        else:
            raise UnexpectedToken(next,'Expected Identifier')

    def token(self, type):
        next = self.next()
        if next == type:
            return next
        else:
            raise UnexpectedToken(next, 'Expected ' + type)
