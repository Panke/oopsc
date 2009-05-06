# coding: utf8

class WriteStatement(object):
    """
    This class represents the while statement in the
    abstract syntax tree
    """
    def __init__(self, op):
        # the expression that will be written to standard output
        self.operand = op
    
class ReadStatement(object):
    """
    This class represents the read statement, which is
    reading one integer from standard input
    """

    def __init__(self, op):
        self.operand = op

class IfStatement(object):

    def __init__(self, cond):
        self.condition = cond
        self.then = []

    def add_to_if(self, stmt):
        self.then.append(stmt)

class WhileStatement(object):

    def __init__(self, cond):
        self.condition = cond
        self.statements = []

    def add(self, stmt):
        self.statements.append(stmt)
        
class Assignment(object):

    def __init__(self, to, what):
        self.lhs = to
        self.rhs = what

class CallStatement(object):

    def __init__(self, expression):
        self.call = expression


