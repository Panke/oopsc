# coding: utf-8 

class Expression(object):
    """
    An Expression in the Abstract Syntax Tree.
    """

    def __init__(self, token):
        # is it in l-value?
        self.l_value = False
        # the position in sourcce
        self.position = token.position

    def __str__(self):
        return "EXP at Position: \d \d"  % pos



class LiteralExpression(Expression):

    def __init__(self, token, typ):
        Expression.__init__(self, token)
        self.value = token.value
        self.type = typ

class VarOrCallExpression(Expression):

    def __init__(self, token):
        Expression.__init__(self, token)

class NewExpression(Expression):

    def __init__(self, token):
        Expression.__init__(self, token)
        self.type = token.value


        
class UnaryExpression(Expression):
    """
    An unary expression.
    """

    def __init__(self,  operator, operand):
        Expression.__init__(self, operator)
        self.operator = operator
        self.operand = operand
        
    
class BinaryExpression(Expression):
    """
    An binary expression.
    """

    def __init__(self, lhs, op, rhs):
        Expression.__init__(self, op)
        self.operator = op
        self.lhs = lhs
        self.rhs = rhs

class AccessExpression(Expression):
    """
    Object Acces via the dot operator
    """

    def __init__(self, object, attribute):
        Expression.__init__(self, attribute)
        self.object = object
        self.attribute = attribute

# class LiteralExpression(Expression):
#     """
#     A literal is an expression, too.
#     """
#     def __init__(self, value, type, pos):
#         Expression.__init__(self, pos)
#         self.value = valie
#         self.type = type

