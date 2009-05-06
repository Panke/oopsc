# coding: utf-8 

"""
This module implements the parser for OOPS. Its main entry point is
the function ''parse'' which takes a stream of tokens and returns
the abstract syntax tree of the program or raises an InvalidSyntaxError.

All parsing functions do have one invariant: They expect that the very next
token in the stream is the first token of the syntax element they parse
and they consume all tokens of the element that they are parsing.

"""

from errors import UnexpectedToken
import declarations
from declarations import *
from expressions import *
from statements import *
from lexer import Token

class AST(object):
    """
    The abstract syntax tree.
    """

    def __init__(self, main_class):
        self.main_class = main_class

    def generate_code(self):
        pass

    def context_analysis(self):
        pass

    def __str__(self):
        return str(self.main_class)



        
def parse(stream):
    # Every simple OOPS/0 program starts with the declartion of the
    # main class
    main = class_decl(stream)
    stream.token('EOF')

    return AST(main)
    

def class_decl(stream):
    """
    This functions parses a class declaration
    """
    stream.keyword('CLASS')
    # Read the name of the class 
    decl = ClassDeclaration(stream.identifier())
    stream.keyword('IS')
    # read member (vars or methods) of the class
    while(stream.seek() != 'END'):
        decl.add_member(member_decl(stream))
    stream.keyword('END')
    stream.keyword('CLASS')

    return decl
    
def member_decl(stream):
    """
    This class parses the declaration of a class member, which
    can either be a method or a variable

    """

    # check if we parse a attribute or a method
    token = stream.seek()
    if token == 'METHOD':
        return method_decl(stream)
    else:
        vars = var_decl(stream)
        stream.token('SEMICOLON')
        return vars

    
def method_decl(stream):
    """
    Parse a method declaration.
    """

    stream.keyword('METHOD')
    method = MethodDeclaration(stream.identifier())
    # parse the local variable declarations
    stream.keyword('IS')
    while(stream.seek().id != 'BEGIN'):
        method.add_var(var_decl(stream))
        stream.token('SEMICOLON')
    
    stream.keyword('BEGIN')

    while(stream.seek().id != 'END'):
        method.add_statement(statement(stream))

    stream.keyword('END')
    stream.keyword('METHOD')
    
    return method

def var_decl(stream):
    """
    Parse a variable declaration.
    It returns a list of variable declarations since
    more than one variable with one type may be declared
    in one rush
    """

    var_decls = []
    var_decls.append(VariableDeclaration(stream.identifier()))
    while stream.seek() != "COLON":
        stream.token('COMMA')
        var_decls.append(VariableDeclaration(stream.indentifier()))

    stream.token('COLON')
    typename = stream.identifier()

    # add the typename to the variable declarations 
    for decl in var_decls:
        decl.type = typename
    return var_decls



              

def statement(stream):
    """
    Parse a statement and return the approiate statement type
    """
    t = stream.seek()
    # call the right function for the statement
    # statements is a dict containing them
    try:
        return statements[t.id](stream)
    except KeyError:
        e = member_access(stream)
        if stream.seek() == 'BECOMES':
            stream.next()
            stmt = Assignment(e, expression(stream))
        else:
            stmt = CallStatement(e)

        stream.token('SEMICOLON')
        return stmt

def read_stmt(stream):
    """
    Parse a read statement
    """
    stream.keyword('READ')
    stmt = ReadStatement(member_access(stream))
    stream.token('SEMICOLON')
    return stmt

def write_stmt(stream):
    stream.keyword('WRITE')
    stmt = WriteStatement(expression(stream))
    stream.token('SEMICOLON')

def if_stmt(stream):
    stream.keyword('IF')
    stmt = IfStatement(relation(stream))
    stream.keyword('THEN')
    while(stream.seek() != 'END'):
        stmt.add_to_if(statement(stream))
    stream.keyword('END')
    stream.keyword('IF')

def while_stmt(stream):
    stream.keyword('WHILE')
    stmt = WhileStatement(relation(stream))
    stream.keyword('DO')
    while(stream.seek() != 'END'):
        stmt.add(statement(stream))
    stream.keyword('END')
    stream.keyword('WHILE')

statements = {'READ' : read_stmt, 'WRITE' : write_stmt,
              'IF' : if_stmt, 'WHILE' : while_stmt}

    
def relation(stream):
    lhs = expression(stream)
    next_token = stream.seek()
    if next_token in ('EQ', 'NEQ', 'GT', "GTEQ", "LT",
                          "LTEQ"):
        op = stream.next()
        rhs = expression(stream)
        return BinaryExpression(lhs, op, rhs)
    else:
        return lhs

def expression(stream):
    e = term(stream)
    while stream.seek() in ('PLUS', 'MINUS'):
        op = stream.next()
        e = BinaryExpression(e, op, expression(stream))

    return e


def term(stream):
    e = factor(stream)
    while stream.seek() in ('TIMES', 'DIV', 'MOD'):
        op = stream.next()
        e = BinaryExpression(e, op, factor(stream))

    return e

def factor(stream):
    if stream.seek() == 'MINUS':
        return UnaryExpression(stream.next(), factor(stream))
    else:
        return member_access(stream)
    
def member_access(stream):
    e = literal(stream)
    while(stream.seek() == 'PERIOD'):
        stream.next()
        e = AccessExpression(e, VarOrCallExpression(stream.identifier()))

    return e

def literal(stream):
    next = stream.next()
    
    if next == 'NUMBER':
        return LiteralExpression(next, declarations.intType)
    elif next == 'NULL':
        return LiteralExpression(0, declarations.nullType)
                             
    elif next == 'SELF':
        return VarOrCallExpression(Token('IDENT', next.position, '_self'))
    
    elif next == 'NEW':
        return NewExpression(stream.identifier())

    elif next == 'LPAREN':
        exp = expression(stream)
        stream.token('RPAREN')
        return exp
    
    elif next == 'IDENT':
        return VarOrCallExpression(next)

    else:
        raise UnexpectedToken(next)
                                 


if __name__ == '__main__':
    from utils import *
    from lexer import lex
    f = open("/home/tobias/uebersetzerbau/OOPSC-0/Examples/code.oops").read()
    stream = Stream(unicode(f, 'utf8'))
    parse(TokenStream(lex(stream)))

