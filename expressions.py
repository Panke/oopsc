# coding: utf-8 

class Expression(object):
    """
    An Expression in the Abstract Syntax Tree.
    """

    def __init__(self, pos):
        # is it in l-value?
        self.l_value = False
        # the position in sourcce
        self.position = pos

    def __str__(self):
        x, y = pos
        return "EXP
