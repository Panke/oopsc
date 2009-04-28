# coding: utf-8 

class Expression(object):
    """
    An Expression in the Abstract Syntax Tree.
    """

    def __init__(self, ident):
        # is it in l-value?
        self.l_value = False
        # the position in sourcce
        self.position = pos

    def __str__(self):
        return "EXP at Position: \d \d"  % pos


class UnaryExpression(Expression):
    """
    An unary expression.
    """

    def __init__(self, pos, operator, operand):
        Expression.__init__(self, pos)
        self.operator = operator
        self.operand = operand
        
    
class BinaryExpression(Expression):
    """
    An binary expression.
    """

    def __init__(self, operator, lhs, rhs):
        Expression.__init__(self, lhs.position)
        self.operator = operator
        self.lhs = lhs
        self.rhs = rhs

class AccessExpression(Expression):
    """
    Object Acces via the dot operator
    """

    def __init__(self, object, attribute):
        Expression.__init__(self, object.position)
        self.object = object
        self.attribute = attribute

class LiteralExpression(Expression):
    """
    A literal is an expression, too.
    """
    def __init__(self, value, type, pos):
        Expression.__init__(self, pos)
        self.value = valie
        self.type = type

